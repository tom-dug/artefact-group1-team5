
from controle import controller
import asyncio
import math
from camera import vision_robot
from controle import utils
from controle import config
from controle import communication
from web import console

class Robot:
    def __init__(self):
        self.c = controller.Controller()
        self.vision = vision_robot.VisionRobot()
        self.v_ar = config.default_v_ar
        self.v_gd = config.default_v_gd
        self.ticks_par_cm = config.default_ticks_par_cm
        self.ticks_par_rad = config.default_ticks_par_rad
        self.v_gauche_avance = 0
        self.v_droite_avance = 0
        self.v_gauche_tourne = 0
        self.v_droite_tourne = 0
        self.block = True
        self.relative = self.c.new_relative()
        self.mode_auto = False
        self.pos = config.default_pos
        self.dir = config.default_dir
        self.ratio_v_roues = config.default_ratio_v_roues
    
    '''
    Prend aucun argument.
    Renvoie None.
    Actualise la vitesse des moteurs en fonction de la vitesse indiquée dans
    self. Cette fonction est la seule qui modifie la 'vraie' vitesse des moteurs.
    '''
    def actualiser(self):
        self.c.set_motor_shutdown_timeout(10)
        if self.block:
            self.c.set_raw_motor_speed(
                0,
                0
            )
            self.c.standby()
        else:
            self.c.set_raw_motor_speed(
                (self.v_gauche_avance + self.v_gauche_tourne) / self.ratio_v_roues,
                (self.v_droite_avance + self.v_droite_tourne) * self.ratio_v_roues
            )
    
    '''
    Les 8 fonctions suivantes sont pour le contrôle manuel du robot.
    Elles prennent aucun argument.
    Elles renvoient None.
    Elles modifient la valeur 'théorique' des moteurs et font appel à
    actualiser pour faire la la 'vraie' modification de vitesse.
    '''

    def debut_avancer(self):
        self.v_gauche_avance = self.v_ar
        self.v_droite_avance = self.v_ar
        self.actualiser()
    
    def debut_reculer(self):
        self.v_gauche_avance = -self.v_ar
        self.v_droite_avance = -self.v_ar
        self.actualiser()
    
    def debut_tourner_gauche(self):
        self.v_gauche_tourne = self.v_gd
        self.v_droite_tourne = -self.v_gd
        self.actualiser()
    
    def debut_tourner_droite(self):
        self.v_gauche_tourne = -self.v_gd
        self.v_droite_tourne = self.v_gd
        self.actualiser()
    
    def fin_avancer(self):
        self.v_gauche_avance = 0
        self.v_droite_avance = 0
        self.actualiser()
    
    def fin_tourner_gauche(self):
        self.v_gauche_tourne = 0
        self.v_droite_tourne = 0
        self.actualiser()
    
    def fin_reculer(self):
        self.v_gauche_avance = 0
        self.v_droite_avance = 0
        self.actualiser()
    
    def fin_tourner_droite(self):
        self.v_gauche_tourne = 0
        self.v_droite_tourne = 0
        self.actualiser()

    '''
    Prend aucun argument.
    Renvoie None.
    Met toutes les vitesses à 0 et actualise les moteurs. Modifie l'attribut
    self.block à True pour blocker les commandes qui suivent.
    '''
    def stop(self):
        self.v_gauche_avance = 0
        self.v_droite_avance = 0
        self.v_gauche_tourne = 0
        self.v_droite_tourne = 0
        self.block = True
        self.actualiser()

    '''
    Prend aucun argument.
    Renvoie None.
    Modifie l'attribut self.block pour accepter les commandes qui suivent.
    '''
    def start(self):
        self.block = False
        self.actualiser()

    '''
    Les 4 fonctions suivantes sont pour le contrôle automatique du robot.
    Elles prennent aucun argument.
    Elles renvoient None.
    Elles actualisent la vitesse des moteurs et font des tests réguliers du
    nombre de ticks effectués pour contrôler la distance parcourue. Ces
    fonctions terminent une fois le mouvement effectué et peuvent prendre
    plusieurs secondes à exécuter. Elles sont toutes asynchronées, ce qui évite
    de blocker le processus durant leur exécution.
    '''

    async def avancer(self, dist):
        console.log(f"Appel à avancer")
        self.relative = self.c.new_relative()
        self.v_gauche_tourne = self.v_ar
        self.v_droite_tourne = self.v_ar
        self.actualiser()
        pos0 = self.pos
        dir = self.dir
        x0, y0 = pos0
        ticks_voulus = self.ticks_par_cm * dist
        while (ticks := self.ticks_moyen(self.c.get_relative_encoder_ticks_no_update(self.relative))) < ticks_voulus:
            x = x0 + (ticks / self.ticks_par_cm) * math.cos(dir)
            y = y0 + (ticks / self.ticks_par_cm) * math.sin(dir)
            self.pos = (x, y)
            await asyncio.sleep(0.01)
        self.v_gauche_tourne = 0
        self.v_droite_tourne = 0
        self.actualiser()
        # console.log(f"Déplacement : {pos0} -> {self.pos}")
        console.log(f"Fin avancer")
    
    async def reculer(self, dist):
        console.log(f"Appel à reculer")
        self.relative = self.c.new_relative()
        self.v_gauche_tourne = -self.v_ar
        self.v_droite_tourne = -self.v_ar
        self.actualiser()
        pos0 = self.pos
        dir = self.dir
        x0, y0 = pos0
        ticks_voulus = self.ticks_par_cm * dist
        while (ticks := self.ticks_moyen(self.c.get_relative_encoder_ticks_no_update(self.relative))) < ticks_voulus:
            x = x0 - (ticks / self.ticks_par_cm) * math.cos(dir)
            y = y0 - (ticks / self.ticks_par_cm) * math.sin(dir)
            self.pos = (x, y)
            await asyncio.sleep(0.01)
        self.v_gauche_tourne = 0
        self.v_droite_tourne = 0
        self.actualiser()
        # console.log(f"Déplacement : {pos0} -> {self.pos}")
        console.log(f"Fin reculer")
    
    async def tourner_gauche(self, angle):
        console.log(f"Appel à tourner gauche")
        self.relative = self.c.new_relative()
        self.v_gauche_tourne = self.v_gd
        self.v_droite_tourne = -self.v_gd
        self.actualiser()
        dir0 = self.dir
        ticks_voulus = self.ticks_par_rad * angle
        while (ticks := self.ticks_moyen(self.c.get_relative_encoder_ticks_no_update(self.relative))) < ticks_voulus:
            dir = dir0 + (ticks / self.ticks_par_rad)
            self.dir = dir
            await asyncio.sleep(0.01)
        self.v_gauche_tourne = 0
        self.v_droite_tourne = 0
        self.actualiser()
        # console.log(f"Déplacement : {dir0} -> {dir}")
        console.log(f"Fin tourner_gauche")
    
    async def tourner_droite(self, angle):
        console.log(f"Appel à tourner droite")
        self.relative = self.c.new_relative()
        self.v_gauche_tourne = -self.v_gd
        self.v_droite_tourne = self.v_gd
        self.actualiser()
        dir0 = self.dir
        ticks_voulus = self.ticks_par_rad * angle
        while (ticks := self.ticks_moyen(self.c.get_relative_encoder_ticks_no_update(self.relative))) < ticks_voulus:
            dir = dir0 - (ticks / self.ticks_par_rad)
            self.dir = dir
            await asyncio.sleep(0.01)
        self.v_gauche_tourne = 0
        self.v_droite_tourne = 0
        self.actualiser()
        # console.log(f"Déplacement : {dir0} -> {dir}")
        console.log(f"Fin tourner_droite")

    '''
    Prend un angle.
    Renvoie None.
    Accepte un angle algébrique, et fait un appel à tourner_gauche ou
    tourner_droite en fonction du signe de l'angle donné.
    '''
    async def tourner(self, angle):
        if angle >= 0:
            await self.tourner_gauche(abs(angle))
        else:
            await self.tourner_droite(abs(angle))

    '''
    Prend aucun argument.
    Renvoie None.
    Fait un 360 pour indiquer qu'une balise a été capturée.
    '''
    async def danse(self):
        console.log("Appel à danse")
        await self.tourner_gauche(360)
        console.log("Fin danse")
    
    '''
    Prend un couple (ticks_gauche, ticks_droite).
    Renvoie une moyenne des valeurs absolues.
    '''
    def ticks_moyen(self, ticks):
        ticks_gauche, ticks_droite = ticks
        return (abs(ticks_gauche) + abs(ticks_droite)) / 2
    
    '''
    Les quatre fonctions suivantes servent à ajuster les valeurs de ticks par
    centimètre ou radian.
    '''

    def augmenter_calibrage_ar(self):
        self.ticks_par_cm += 1

    def baisser_calibrage_ar(self):
        self.ticks_par_cm -= 1

    def augmenter_calibrage_gd(self):
        self.ticks_par_rad += 10

    def baisser_calibrage_gd(self):
        self.ticks_par_rad -= 10

    '''
    Prend aucun argument.
    Renvoie None.
    Renvoie un dictionnaire contennant les information utiles du robot.
    '''
    def get_status(self):
        return {
            "x": self.pos[0],
            "y": self.pos[1],
            "dir": self.dir,
            "v_ar": self.v_ar,
            "v_gd": self.v_gd,
            "ticks_par_cm": self.ticks_par_cm,
            "ticks_par_rad": self.ticks_par_rad,
            "v_gauche_avance": self.v_gauche_avance,
            "v_droite_avance": self.v_droite_avance,
            "v_gauche_tourne": self.v_gauche_tourne,
            "v_droite_tourne": self.v_droite_tourne,
            "block": self.block,
            "mode_auto": self.mode_auto,
            "ratio_v_roues": self.ratio_v_roues
        }

    '''
    Les deux fonctions suivantes servent à ajuster le ratoi de vitesse entre
    la roue gauche et la roue droite.
    Elles prennent aucun argument.
    Elles renvoient None.
    '''

    def increase_ratio(self):
        self.ratio_v_roues += 0.001
    
    def decrease_ratio(self):
        self.ratio_v_roues -= 0.001


    '''
    Prend aucun argument.
    Renvoie None.
    On suppose que le robot peut voir 3 balises de repérage. Il fait un tour
    sur lui même jusqu'à scanner les 3 premières balises de repérage. Une fois
    les 3 balises repérées, il fait des calculs et met à jour self.pos et
    self.dir.
    '''
    async def calibrer(self):
        console.log("\nDEBUT CALIBRER")

        # Information des balises repère
        balises_repere = []

        # Faire un tour sur lui même à intervalles de 30°
        while True:
            for _ in range(config.nombre_captures):
                balise = self.vision.get_repere_proche()
                await asyncio.sleep(config.temps_entre_captures)
                if balise is not None:
                    balise_id = balise.id
                    if not any(x.id == balise_id for x in balises_repere):
                        console.log(f"Balise repérée, balise_id = {balise_id}", color="green")
                        balises_repere.append(balise)
            if len(balises_repere) == 3: # on arrête de tourner dès qu'on trouve les 3 balises
                break
            await self.tourner_gauche(config.angle_calibration)

        # Trouver x, y
        x, y = utils.position_depuis_balises(balises_repere[0], balises_repere[1], balises_repere[2])

        # Récupération de l'orientation par rapport à la dernière balise
        derniere_balise = balises_repere[-1]
        alpha = derniere_balise.yaw
        
        # Dijonction de cas en fonction de la dernière balise scannée
        orientation = 0
        if derniere_balise.id == 2:
            orientation = alpha
        if derniere_balise.id == 1:
            orientation = alpha + math.pi/2
        if derniere_balise.id == 4: 
            orientation = alpha + math.pi
        if derniere_balise.id == 3:
            orientation = alpha + (3*math.pi)/2
        
        self.pos = (x, y)
        self.dir = orientation

    '''
    Prend en argument x, y les coordonnées de la destination.
    Renvoie None.
    Déplace le robot à cette destination. Attention : le robot ne garantie aucune
    orientation particulière à l'arrivée.
    '''
    async def goto(self, destination):
        console.log("\nDEBUT GOTO")
        x, y = destination
        # Déterminer la position actuelle
        pos_x, pos_y = self.pos
        # Calcul de l'angle à tourner et la distance à avancer
        mov_x, mov_y = x - pos_x, y - pos_y
        angle_absolu = math.atan2(mov_y, mov_x) # ATTENTION donner y en premier
        angle = angle_absolu - self.dir
        dist = math.sqrt(mov_x ** 2 + mov_y ** 2)
        console.log(f"Calcul, angle_absolu = {angle_absolu}, angle = {angle}, dist = {dist}")
        # Se déplacer
        await self.tourner(angle)
        await self.avancer(dist)
        # Actualiser position intérieure
        self.pos = (x, y)
        self.dir = angle_absolu
        console.log("FIN GOTO")

    '''
    Prend un angle relatif au 0 absolu.
    Renvoie None.
    Oriente le robot vers l'angle absolu et actualise self.dir.
    '''
    async def orienter(self, angle_absolu):
        console.log(f"\nDEBUT ORIENTER angle_absolu = {angle_absolu}")
        # Calculer l'angle à tourner
        angle = angle_absolu - self.dir
        # Tourner
        await self.tourner(angle)
        # Actualiser la position intérieure
        self.dir = angle_absolu
        console.log("FIN ORIENTER") 

    '''
    Prend aucun argument.
    Renvoie None.
    Augmente la vitesse du robot.
    '''
    def debut_boost(self):
        self.v_ar = config.boost_v_ar
        self.v_gd = config.boost_v_gd

    '''
    Prend aucun argument.
    Renvoie None.
    Rétablit la vitesse de base du robot.
    '''
    def fin_boost(self):
        self.v_ar = config.default_v_ar
        self.v_gd = config.default_v_gd

    async def decouverte_drapeaux(self):
        console.log("Début de la découverte", color="purple")

        # Dictionnaire contenant toute l'information des drapeaux
        info_drapeaux = {}
        # Recherche exhaustive
        for secteur in range(0, 4):
            await self.calibrer()
            position = config.positions_reference[0][secteur]
            await self.goto(position)
            for cercle in range(0, 2):
                orientation = config.orientations_reference[cercle][secteur]
                await asyncio.sleep(0.5)
                await self.orienter(orientation)
                balises_info = await self.vision.get_balises_safe()
                drapeaux_info = [b for b in balises_info if b.id > 4]
                drapeaux_info = [b for b in drapeaux_info if abs(b.yaw) <= 0.7]
                if len(drapeaux_info) >= 1:
                    drapeau_info = min(drapeaux_info, key=lambda b: b.distance)
                    id_drapeau = drapeau_info.id
                    console.log(f"Drapeau trouvé, id_drapeau = {id_drapeau}, position = {position}, zone = {(cercle, secteur)}", color="green")
                    info_drapeaux[id_drapeau] = {
                        "id": id_drapeau,
                        "cercle": cercle,
                        "secteur": secteur,
                        "zone": (cercle, secteur)
                    }
                else:
                    console.log(f"Drapeau non trouvé, position = {position}, zone = {(cercle, secteur)}", color="red")
        # Bilan de la recherche
        console.log(f"Fin de la découverte des drapeaux\ninfo_drapeaux = {info_drapeaux}", color="purple")
        return info_drapeaux


    '''
    Prend aucun argument.
    Renvoie None.
    Fait la partie capture de l'évaluation finale.
    '''
    async def strategie(self):
        console.log("Début de la stratégie", color="purple")
        '''
        Avancer 1m pour rentrer dans le demi-disque.
        '''
        await self.avancer(100)     

        '''
        En boucle, demander la prochaine balise, y aller, danser.
        '''
        while True:
            # Cartographier notre zone
            cartographie = await self.decouverte_drapeaux()
            # Attendre 1s à chaque nouvelle instruction
            await asyncio.sleep(1)
            # Demander la prochaine cible
            id_cibles = communication.liste_balises()
            # Protection contre erreurs
            if id_cibles is None:
                console.log("Erreur : id_cibles is None, nouvel essai dans 1s", color="red")
                await asyncio.sleep(1)
                continue
            # Vérifier qu'une cible est donnée
            if len(id_cibles) == 0:
                console.log("Erreur : Aucune entrée, nouvel essai dans 1s", color="red")
                await asyncio.sleep(1)
                continue
            console.log(f"id_cibles = {id_cibles}", color="purple")
            # On garde les cibles qu'on connait
            id_cibles = [i for i in id_cibles if i in [x.id for x in cartographie]]
            # Plusieurs cibles sont données
            for id_cible in id_cibles:
                console.log(f"Nouvelle cible, id_cible = {id_cible}", color="purple")
                # Récupérer les informations sur cette cible
                info_cible = cartographie[id_cible]
                cercle_cible = info_cible["cercle"]
                secteur_cible = info_cible["secteur"]
                position_cible = config.positions_reference[cercle_cible][secteur_cible]
                orientation_cible = config.orientations_reference[cercle_cible][secteur_cible]
                # Se déplacer vers la zone
                await self.goto(position_cible)
                await self.orienter(orientation_cible)
                # Capturer la balise
                self.danse()
                succes = communication.balise_capturee(id_cible, utils.secteur_to_msec(secteur_cible), utils.cercle_to_minner(cercle_cible))
                if succes:
                    console.log("Succès de l'envoi de la balise au serveur de suivi", color="green")
                else:
                    console.log("Échec de l'envoi de la balise au serveur de suivi", color="red")

