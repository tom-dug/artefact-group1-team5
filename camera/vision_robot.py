import math
from .detection import Camera, detect_filtered, rvec_to_euler, _make_objp, MARKER_REPERE_CM, MARKER_DRAPEAU_CM, camera_matrix, dist_coeffs
import numpy as np
import asyncio
from camera import config
from web import console

class Balise:
    def __init__(self, id, distance, yaw):
        """
        Objet représentant une balise détectée :
        - id : identifiant ArUco
        - distance : distance au robot (en cm)
        - yaw : angle en radians
        """
        self.id = id
        self.distance = distance
        self.yaw = yaw

class VisionRobot:
    """
    Fournit des fonctions haut niveau :
    - lire un repère (id, distance, yaw)
    - lire un drapeau (id, distance, yaw)
    """

    def __init__(self, cam_id=0):
        self.cam = Camera()

    def grab_frame(self):
        return self.cam.read()

    def close(self):
        self.cam.release()

    # ---------------- TOUTES BALISES  ----------------

    def get_balises(self):
        frame = self.grab_frame()
        if frame is None:
            return []

        res = detect_filtered(frame)
        if not res:
            return []

        infos = []

        for kind, marker_id, dist, yaw, rvec, tvec in res:
            yaw_rad = yaw * math.pi / 180
            balise = Balise(
                id= marker_id,
                distance= dist,
                yaw= yaw_rad 
            )
            infos.append(balise)

        return infos   # Peut contenir 0, 1, 2, ... balises

    async def get_balises_safe(self):
        infos = []
        for i in range(config.nombre_captures_ignore):
            balises_ignore = self.get_balises()
            #console.log(f"{i} - Ignore balises {[balise.id for balise in balises_ignore]}")
            await asyncio.sleep(config.temps_entre_captures)
        for i in range(config.nombre_captures): # TODO mettre cette valeur dans un config
            balises = self.get_balises()
            #console.log(f"{i} - Keep balises {[balise.id for balise in balises]}")
            await asyncio.sleep(config.temps_entre_captures)
            for balise in balises:
                if not any(d.id == balise.id for d in infos):
                    # La balise n'a pas encore été vu
                    infos.append(balise)
        return infos

    # ---------------- DRAPEAUX  ----------------

    
    def get_drapeau_proche(self):
        """
        Retourne un objet Balise correspondant
        au drapeau le plus proche détecté dans l'image.
        Sinon retourne None.
        """
        frame = self.grab_frame()
        if frame is None:
            return None

        res = detect_filtered(frame)
        if not res:
            return None

        balise_proche = None
        min_dist = float("inf")

        for kind, marker_id, dist, yaw, rvec, tvec in res:
        # On ne garde que les drapeaux
            if kind == "drapeau":

                # Conversion du yaw en radians
                yaw_rad = yaw * math.pi / 180

                # Création d'une Balise
                balise = Balise(
                    id=marker_id,
                    distance=dist,
                    yaw=yaw_rad
            )

            # Mise à jour du drapeau le plus proche
                if balise.distance < min_dist:
                    min_dist = balise.distance
                    balise_proche = balise

        return balise_proche
    
    
    def get_drapeaux(self):
        frame = self.grab_frame()
        if frame is None:
            return []

        res = detect_filtered(frame)
        if not res:
            return []

        infos = []

        for kind, marker_id, dist, yaw, rvec, tvec in res:
            if kind == "drapeau":
                yaw_rad = yaw * math.pi / 180
                balise = Balise(
                    id= marker_id,
                    distance= dist,
                    yaw= yaw_rad
                )
                infos.append(balise)

        return infos   # Peut contenir 0, 1, 2, ... drapeaux

    async def get_drapeaux_safe(self):
        infos = []
        for i in range(config.nombre_captures_ignore):
            drapeaux = self.get_drapeaux()
            await asyncio.sleep(config.temps_entre_captures)
        for i in range(config.nombre_captures):
            drapeaux = self.get_drapeaux()
            await asyncio.sleep(config.temps_entre_captures)
            for drapeau in drapeaux:
                if not any(d.id == drapeau.id for d in infos):
                    # Le drapeau n'a pas encore été vu
                    infos.append(drapeau)
        return infos
        

        


    # -------------- REPERES -------------------------

   
    
    def get_repere_proche(self):
        """
        Retourne un objet Balise correspondant
        au repère le plus proche détecté dans l'image.
        Sinon retourne None.
        """
        frame = self.grab_frame()
        if frame is None:
            return None

        res = detect_filtered(frame)
        if not res:
            return None

        balise_proche = None
        min_dist = float("inf")

        for kind, marker_id, dist, yaw, rvec, tvec in res:
        # On ne garde que les drapeaux
            if kind == "repere":

                # Conversion du yaw en radians
                yaw_rad = yaw * math.pi / 180

                # Création d'une Balise
                balise = Balise(
                    id=marker_id,
                    distance=dist,
                    yaw=yaw_rad
                )

            # Mise à jour du drapeau le plus proche
                if balise.distance < min_dist:
                    min_dist = balise.distance
                    balise_proche = balise

        return balise_proche