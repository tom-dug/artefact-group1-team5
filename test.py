import asyncio
from camera import vision_robot
import cv2
import math
from controle import main
async def test_camera():
    vision = vision_robot.VisionRobot()
    k = 0
    while True:
        k += 1
        await asyncio.sleep(0.1)
        res = vision.get_repere_proche()
        if res is None:
            print(f"{k} - Rien détecté")
        else:
            id_balise = res.id
            yaw_rad = round(res.yaw, 5)
            yaw_deg = round(yaw_rad * 360 / (2 * math.pi), 5)
            print(f"{k} - Détecté : id_balise = {id_balise}, yaw_rad = {yaw_rad}, yaw_deg = {yaw_deg}")

async def test_balises():
    vision = vision_robot.VisionRobot()
    k = 0
    while True:
        k += 1
        await asyncio.sleep(0.01)
        balises = await vision.get_balises_safe()
        if balises == []:
            print(f"{k} - Rien détecté")
        else:
            for balise in balises:
                id_balise = balise.id
                yaw_rad = round(balise.yaw, 5)
                yaw_deg = round(yaw_rad * 360 / (2 * math.pi), 5)
                distance = round(balise.distance, 5)
                print(f"{k} - Détecté : id_balise = {id_balise}, yaw_rad = {yaw_rad}, yaw_deg = {yaw_deg}, distance = {distance}")

async def test_requete():
    k = 0
    while True:
        k += 1
        print(f"{k} - appel à liste balises")
        l = robot_autonome.liste_balises()
        print(f"Resultat: l = {l}")
        await asyncio.sleep(1)

async def test_deplacements():
    print("Debut du test deplacements")
    robot = main.Robot()
    robot.start()
    await robot.calibrer()
    print(robot.get_status())
    print("Fin du test deplacements")

asyncio.run(test_balises())
