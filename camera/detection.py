import cv2
import numpy as np
import math
from camera import config

# ================================
#  CALIBRATION CAMERA
# ================================
camera_matrix = np.load("camera/camera_matrix.npy")
dist_coeffs   = np.load("camera/dist_coeffs.npy")

# ================================
#  ARUCO SETUP (compatible OpenCV 4.6.0)
# ================================
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)
parameters = cv2.aruco.DetectorParameters()

# ================================
#  TAILLES DES MARQUEURS (cm) | 
# ================================
MARKER_REPERE_CM  = 10.0 
MARKER_DRAPEAU_CM = 2.0

def _make_objp(size_cm: float):
    """Retourne les 4 coins 3D d'un marker centré
       utile pour calculer le rvec et tvec (rotation vector
       et translation vector)"""
    s = size_cm / 2.0
    return np.array([
        [-s,  s, 0],
        [ s,  s, 0],
        [ s, -s, 0],
        [-s, -s, 0]
    ], dtype=np.float32)


def rvec_to_euler(rvec):
    """Convertit rvec → angles roll/pitch/yaw en degrés.
        rvec = rotation vector obtenu par cv2.SolvePnP, possède
        3 composantes (en coordonnées cartésiennes). Ce vecteur de rotation
        est obtenu en utilisant la position 3D et 2D des 4 coins de la balise"""
    R, _ = cv2.Rodrigues(rvec) # Rodrigues ici permet de convertir un vecteur de rotation en une matrice de rotation
    sy = math.sqrt(R[0,0]**2 + R[1,0]**2) 

    if sy < 1e-6:
        roll  = math.atan2(-R[1,2], R[1,1])
        pitch = math.atan2(-R[2,0], sy)
        yaw   = 0
    else:
        roll  = math.atan2(R[2,1], R[2,2])
        pitch = math.atan2(-R[2,0], sy)
        yaw   = math.atan2(R[1,0], R[0,0])

    return np.degrees([roll, pitch, yaw])


class Camera:
    """Wrapper simple autour de cv2.VideoCapture."""
    def __init__(self, cam_id=0): # Attention : cam_id = 0 sur RPI
        self.cap = cv2.VideoCapture(cam_id, cv2.CAP_V4L2) # Passer par CAP_V4L2

    def read(self):
        ok, frame = self.cap.read()
        return frame if ok else None

    def release(self):
        self.cap.release()


def detect(frame):
    """
    Détecte toutes les ArUco présents dans l’image.
    Retourne une liste de tuples :
       (marker_id, distance_cm, pitch_deg, corners, rvec, tvec)
    ou [] si rien.
    """
    corners, ids, _ = cv2.aruco.detectMarkers(
        frame,
        aruco_dict,
        parameters=parameters
    )

    if ids is None:
        return []

    results = []

    for i, mid in enumerate(ids.flatten()):

        # On ignore les faces arrière ID=0
        if mid == 0:
            continue

        imgp = corners[i].reshape((4, 2)).astype(np.float32)

        # Choix de la taille de la balise
        if mid in (1,2,3,4):
            objp = _make_objp(MARKER_REPERE_CM)
        else:
            objp = _make_objp(MARKER_DRAPEAU_CM)

        ok, rvec, tvec = cv2.solvePnP(
            objp,
            imgp,
            camera_matrix,
            dist_coeffs
        )
        if not ok:
            continue

        dist = float(np.linalg.norm(tvec)) + config.decalage_camera # Attention : on modifie la distance artificiellement
        roll, pitch, yaw = rvec_to_euler(rvec)

        results.append((mid, dist, float(pitch), corners[i], rvec, tvec))

    return results


def detect_filtered(frame):
    detected = detect(frame)
    if len(detected) == 0:
        return []

    final = []

    for (marker_id, dist, yaw, corners, rvec, tvec) in detected:

        if marker_id in (1,2,3,4):
            final.append(("repere", marker_id, dist, yaw, rvec, tvec))

        elif 5 <= marker_id <= 14:
            final.append(("drapeau", marker_id, dist, yaw, rvec, tvec))

    return final
