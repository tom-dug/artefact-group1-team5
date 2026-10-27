import asyncio
import math
from web import console

from maestro_puppet import MaestroPuppet
from maestro_puppet.tasks import (
    register_move_forward_distance,
    register_rotate_angle,
    register_check_for_arucos,
    register_get_pos_function,
    register_set_pos_function,
    MoveForwardDistanceTask,
    RotateAngleTask,
    XYRotation,
    TaskUpdateResult,
    CheckForArucosTask,
    ArucoData
)

'''
Prend en argument le robot.
Renvoie None.
Définit les tâches pour le puppet et execute le puppet.
'''
async def start_puppet(robot):

    @register_move_forward_distance
    class MoveForwardDistanceTaskImpl(MoveForwardDistanceTask):
        initial_x: float = 0.0
        initial_y: float = 0.0
        task = None

        def start(self):
            console.log("Move forward task - start", color="pink")
            robot.start()
            x_cm, y_cm = robot.pos
            self.initial_x, self.initial_y = x_cm/100, y_cm/100
            dist_en_m = self.distance
            dist_en_cm = dist_en_m * 100
            if dist_en_cm >= 0:
                self.task = asyncio.create_task(robot.avancer(abs(dist_en_cm)))
            else:
                self.task = asyncio.create_task(robot.reculer(abs(dist_en_cm)))

        def update(self) -> TaskUpdateResult:
            if self.task is not None and self.task.done():
                return TaskUpdateResult.SUCCESS
            else:
                return TaskUpdateResult.RUNNING

        def stop(self):
            console.log("Move forward task - stop", color="pink")
            robot.stop()


    @register_rotate_angle
    class RotateAngleTaskImpl(RotateAngleTask):
        initial_rotation: float = 0.0
        task = None

        def start(self):
            console.log("Rotate angle task - start", color="pink")
            robot.start()
            self.initial_rotation = robot.dir
            self.task = asyncio.create_task(robot.tourner(self.angle))

        def update(self) -> TaskUpdateResult:
            if self.task is not None and self.task.done():
                return TaskUpdateResult.SUCCESS
            else:
                return TaskUpdateResult.RUNNING

        def stop(self):
            console.log("Rotate angle task - stop", color="pink")
            robot.stop()

    @register_check_for_arucos
    class CheckForArucoTaskImpl(CheckForArucosTask):
        arucos_detected = {}
        task = None

        def start(self) -> None:
            console.log("Check for aruco task - start", color="pink")
            self.task = asyncio.create_task(robot.vision.get_balises_safe())

        def update(self) -> TaskUpdateResult:
            if self.task is not None and self.task.done():
                balises = self.task.result()
                for balise in balises:
                    console.log("Check for aruco task - detected balise", color="green")
                    console.log(f"aruco_id = {balise.id}", color="green")
                    console.log(f"distance = {balise.distance/100}", color="green")
                    self.arucos_detected[balise.id] = ArucoData(
                        aruco_id=balise.id,
                        distance=balise.distance/100,
                        angle=balise.yaw
                    )
                return TaskUpdateResult.SUCCESS
            else:
                return TaskUpdateResult.RUNNING
            
        def stop(self) -> None:
            console.log("Check for aruco task - stop", color="pink")

    @register_get_pos_function
    def get_xy_rotation():
        x_cm, y_cm = robot.pos
        rot = robot.dir
        return XYRotation(x=x_cm/100, y=y_cm/100, rotation=rot)

    @register_set_pos_function
    def set_x_y_rotation(x_y_rotation):
        robot.pos = (x_y_rotation.x * 100, x_y_rotation.y * 100)
        robot.dir = x_y_rotation.rotation


    puppet = MaestroPuppet(
        robot_id=5,
        robot_address="http://localhost:8001",
    )
    await puppet.start()
