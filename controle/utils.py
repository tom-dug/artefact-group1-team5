
'''
Ce fichier contient des fonctions diverses, indépendantes, mais utiles pour
les autres fichiers du module controle.
'''

import math
from controle import config

'''
Les deux fonctions suivantes servent à passer de la convention du robot à la
convention du serveur de suivi pour l'identification de secteurs.
'''

def secteur_to_msec(secteur):
    return ["A", "B", "C", "D", "E", "F", "G", "H"][secteur]

def cercle_to_minner(cercle):
    return [1, 0][cercle]

'''
Prend en argument deux couples de forme (x, y).
Renvoie la distance entre les deux positions.
'''
def distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def trilateration(c1, d1, c2, d2):
    """
    Calcule les points d'intersection de deux cercles.
    Retourne une liste de 0, 1 ou 2 solutions (coordonnées x, y).
    """
    x1, y1 = c1
    x2, y2 = c2
    
    # Calcul de la distance d entre les deux balises (points)
    d = distance(c1, c2)
    
    # Cas d'erreurs et de non-intersection
    if d > d1 + d2 or d < abs(d1 - d2):
        print("Erreur trilatération: Cercles disjoints ou inclus.")
        return []

    # Calcul des coordonnées du point P3 (intersection des cercles avec l'axe B1-B2)
    a = (d1**2 - d2**2 + d**2) / (2 * d)
    
    # h est la distance entre P3 et les points d'intersection (X, Y)
    try:
        h = math.sqrt(d1**2 - a**2)
    except ValueError:
        print("Erreur: Erreur de mesure trop importante (sqrt(nombre négatif)).")
        return []

    # Calcul des coordonnées de P3 (projection)
    x3 = x1 + a * (x2 - x1) / d
    y3 = y1 + a * (y2 - y1) / d

    # Calcul des deux solutions (rotation du point P3 par h)
    solution1 = (
        x3 + h * (y2 - y1) / d,
        y3 - h * (x2 - x1) / d
    )
    solution2 = (
        x3 - h * (y2 - y1) / d,
        y3 + h * (x2 - x1) / d
    )
    
    return [solution1, solution2]

def position_depuis_balises(b1, b2, b3):
    """
    Calcule la position du robot par trilatération, en utilisant 
    les deux plus grandes distances pour l'intersection et la plus petite 
    pour la vérification.
    
    b1, b2, b3: trois objets balises dans l'ordre quelconque
    """
    dico_pos_balise = {
        1: config.POS_BALISE_1,
        2: config.POS_BALISE_2,
        3: config.POS_BALISE_3,
        4: config.POS_BALISE_4
    }

    balises = [b1, b2, b3]

    # Trier par distance décroissante
    balises_sorted = sorted(balises, key=lambda b: b.distance, reverse=True)
    
    # Les deux plus grandes distances pour la trilatération
    B_MAJEURE_1 = balises_sorted[0]
    B_MAJEURE_2 = balises_sorted[1]
    
    # La plus petite distance pour la vérification
    B_MINEURE = balises_sorted[2]
    
    # Calculer les deux points d'intersection (Trilatération)
    solutions = trilateration(
        dico_pos_balise[B_MAJEURE_1.id], B_MAJEURE_1.distance,
        dico_pos_balise[B_MAJEURE_2.id], B_MAJEURE_2.distance
    )
    
    if not solutions:
        return None

    # Vérification et sélection du point (Utilisation de la balise mineure)
    meilleure_solution = None
    min_erreur = float('inf')

    for solution in solutions:
        d_calcule = distance(solution, dico_pos_balise[B_MINEURE.id])
        erreur = abs(d_calcule - B_MINEURE.distance) # Erreur entre distance calculée et mesurée
        
        # On choisit le point qui minimise l'erreur
        if erreur < min_erreur:
            min_erreur = erreur
            meilleure_solution = solution     
    # Ajout d'un seuil de tolérance ?

    return meilleure_solution