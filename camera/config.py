
'''
Ce fichier contient un ensemble de constantes utiles pour les autres fichiers
du dossier camera.
'''

import math

# ATTENTION ces valeurs sont aussi présentes dans controle/config.py

# Nombre de captures effectués par la caméra pour être sûr de scanner la balise
nombre_captures = 15
# Temps entre captures, en secondes
temps_entre_captures = 0.01
# Angle à tourner pour la calibration
angle_calibration = math.pi / 12
# Nombre de captures à ignorer
nombre_captures_ignore = 10

# Décalage caméra / centre du robot
decalage_camera = 0.05