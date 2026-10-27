'''
Ce fichier contient le test du module de controle du robot.
Le test effectue :
- une calibration
- un déplacement vers la balise 2
- un test de la calibration G/D
    - un tour sur lui même
    - une vérification de l'angle à la balise 2
- un test de la calibration A/R
    - un déplacement vers l'arrière
    - une verification de la distance à la balise 2
Le résultat du test est montré sur la console
'''
from web import console
import math
import asyncio
from controle import config

async def lancer_test_controle(robot):
    console.log("Début du test controle", color="gray")
    await robot.calibrer()
    await robot.goto((50, 0))
    await robot.orienter(0)

    # Test G/D
    balises = await robot.vision.get_balises_safe()
    if len(balises) == 0:
        console.log("Erreur - rien scanné", color="red")
        return
    if len(balises) > 1:
        console.log("Erreur - trop scanné", color="red")
        return
    balise = balises[0]
    yaw0 = balise.yaw
    console.log(f"yaw0 = {yaw0}", color="gray")
    await robot.tourner(2 * math.pi)
    balises = await robot.vision.get_balises_safe()
    if len(balises) == 0:
        console.log("Erreur - rien scanné", color="red")
        return
    if len(balises) > 1:
        console.log("Erreur - trop scanné", color="red")
        return
    balise = balises[0]
    yaw1 = balise.yaw
    console.log(f"yaw1 = {yaw1}", color="gray")
    yaw_delta = yaw1 - yaw0
    console.log(f"yaw_delta = {yaw_delta}", color="gray")
    if abs(yaw_delta) < math.pi / 8: # TODO mettre cette valeur arbitraire dans un config
        console.log("Test G/D réussi", color="green")
    else:
        console.log("Test G/D échoué", color="red")
        if yaw_delta > 0:
            console.log("Augmenter ticks/rad G/D !", color="orange")
        else:
            console.log("Baisser ticks/rad G/D !", color="orange")
    
    # Test A/R

    console.log("Fin du test controle", color="gray")
