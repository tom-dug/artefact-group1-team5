
'''
Ce fichier contient toutes les fonctions nécessaires à la communication avec
le serveur de suivi.
'''

import requests
import math
import asyncio

"""
Ressources utiles :
https://requests.readthedocs.io/en/latest/user/quickstart/
https://realpython.com/python-f-strings/
"""

"""
Les fonctions suivantes sont celles qui s'occupent
d'intéragir avec le serveur de l'école
"""

URL_ECOLE = "http://proj103.r2.enst.fr/api"

def liste_balises():
    """Demande au serveur la liste des balises à trouver"""
    try:
        r = requests.get(URL_ECOLE + "/list")
        # Vérification du code HTTP
        r.raise_for_status()
        data = r.json()
        print(f"Retour de requête liste_balises : data = {data}")
        print(f"Balises à chercher : {data['markers']}")
        return data["markers"]
    except Exception as e:
        print(f"Erreur de requête de la liste des balises : {e}")
        return None

def envoyer_position(XVAL, YVAL, ANGLE = 0):
    """Envoie la position du robot au serveur"""
    try:
        r = requests.post(f"{URL_ECOLE}/pos?x={XVAL}&y={YVAL}&angle={ANGLE}")
        # print("Envoi position : succès")
        return True
    except Exception as e:
        # print(f"Echec d'envoi de la position : {e}")
        return False

def balise_capturee(MID, MSEC, MINNER):
    """
    Envoie au serveur qu'une balise à été capturée
    MID = indentifiant du marqueur trouvé ([5;16])
    MSEC = nom du secteur où se trouve le marqueur ([A;H])
    MINNER = 1 si le marqueur est dans le cercle intérieur, 0 sinon
    """
    try:
        r = requests.post(f"{URL_ECOLE}/marker?id={MID}&sector={MSEC}&inner={MINNER}")
        print("Capture : succès")
        return True
    except Exception as e:
        print(f"Echec de capture : {e}")
        return False

def etat_course():
    """Récupérer l'état de la course (status, positions des robots,
    drapeaux capturés)"""
    try:
        r = requests.get(f"{URL_ECOLE}/status")
        data = r.json()
        return data
    except Exception as e:
        print(f"Echec de status de course : {e}")
        return None

"""
Les fonctions suivantes servent à tester l'épreuve finale,
le serveur doit être en mode test. Certaines fonctions doivent
encore être ajoutées
"""

def demarrer_course():
    """Démarrer une course lorsque le serveur est en mode test"""
    if etat_course()["status"] == 2:
        r = requests.post(f"{URL_ECOLE}/start")
        print("Serveur en mode test, démarrage")
        return None
    else:
        print("Erreur, le serveur n'est pas en mode test")
        return None

def arreter_course():
    """Arreter une course lorsque le serveur est en mode test"""
    if etat_course()["status"] == 1:
        r = requests.post(f"{URL_ECOLE}/stop")
        print("Serveur démarré, arrêt en cours")
        return None
    else:
        print("Erreur, le serveur n'est pas démarré")
        return None
