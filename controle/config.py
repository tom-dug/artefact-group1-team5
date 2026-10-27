
'''
Ce fichier contient un ensemble de constantes utiles pour les autres fichiers
du dossier controle.
'''

import math

# Position des balises
POS_BALISE_1 = (0, 150)
POS_BALISE_2 = (150, 0)
POS_BALISE_3 = (0, -150)
POS_BALISE_4 = (-150, 0)

# Orientations des secteurs
or_A = 3*math.pi/8
or_B = math.pi/8
or_C = -math.pi/8
or_D = -3*math.pi/8
or_E = -5*math.pi/8
or_F = -7*math.pi/8
or_G = -9*math.pi/8
or_H = -11*math.pi/8
# Orientations intérieures
orientations_reference_int = [
    math.pi + or_A,
    math.pi + or_B,
    math.pi + or_C,
    math.pi + or_D,
    math.pi + or_E,
    math.pi + or_F,
    math.pi + or_G,
    math.pi + or_H
]
# Orientations extérieures
orientations_reference_ext = [
    or_A,
    or_B,
    or_C,
    or_D,
    or_E,
    or_F,
    or_G,
    or_H
]
# Toutes les orientations de référence
orientations_reference = [orientations_reference_int, orientations_reference_ext]
# Positions intérieures
positions_reference_int = [
    ((0.5 * 150 * math.cos(or_A)), 0.5 * 150 * math.sin(or_A)),
    ((0.5 * 150 * math.cos(or_B)), 0.5 * 150 * math.sin(or_B)),
    ((0.5 * 150 * math.cos(or_C)), 0.5 * 150 * math.sin(or_C)),
    ((0.5 * 150 * math.cos(or_D)), 0.5 * 150 * math.sin(or_D)),
    ((0.5 * 150 * math.cos(or_E)), 0.5 * 150 * math.sin(or_E)),
    ((0.5 * 150 * math.cos(or_F)), 0.5 * 150 * math.sin(or_F)),
    ((0.5 * 150 * math.cos(or_G)), 0.5 * 150 * math.sin(or_G)),
    ((0.5 * 150 * math.cos(or_H)), 0.5 * 150 * math.sin(or_H))
]
# Positions extérieures
positions_reference_ext = [
    ((0.5 * 150 * math.cos(or_A)), 0.5 * 150 * math.sin(or_A)),
    ((0.5 * 150 * math.cos(or_B)), 0.5 * 150 * math.sin(or_B)),
    ((0.5 * 150 * math.cos(or_C)), 0.5 * 150 * math.sin(or_C)),
    ((0.5 * 150 * math.cos(or_D)), 0.5 * 150 * math.sin(or_D)),
    ((0.5 * 150 * math.cos(or_E)), 0.5 * 150 * math.sin(or_E)),
    ((0.5 * 150 * math.cos(or_F)), 0.5 * 150 * math.sin(or_F)),
    ((0.5 * 150 * math.cos(or_G)), 0.5 * 150 * math.sin(or_G)),
    ((0.5 * 150 * math.cos(or_H)), 0.5 * 150 * math.sin(or_H))
]
# Toutes les positions de référence
positions_reference = [positions_reference_int, positions_reference_ext]

# ATTENTION ces valeurs sont aussi présentes dans camera/config.py

# Nombre de captures effectués par la caméra pour être sûr de scanner la balise
nombre_captures = 15
# Temps entre captures, en secondes
temps_entre_captures = 0.01
# Angle à tourner pour la calibration
angle_calibration = math.pi / 12

# Valeurs de base de la classe Robot
default_v_ar = -50
default_v_gd = -30
default_ticks_par_cm = 185
default_ticks_par_rad = 1430
default_pos = (170.0, 50.0)
default_dir = math.pi
default_ratio_v_roues = 1.030
# Valeurs boost
boost_v_ar = -90
boost_v_gd = -20