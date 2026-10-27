import cv2
from .detection import Camera, detect, detect_filtered   
from .vision_robot import VisionRobot, get_drapeau_info, get_repere_info
def main():
    cam = Camera(0)

    print("=== TEST DETECT / DETECT_FILTERED ===")
    print("Appuie sur 'q' pour quitter")

    while True:
        frame = cam.read()
        if frame is None:
            print("[ERREUR] image NULL")
            break

        # test non filtré
        """res = detect(frame)
        print("detect():", res)"""

        # test filtré
        res2 = detect_filtered(frame) 
        print("detect_filtered():", res2)

        """res3 = get_drapeau_proche(frame) 
        print("get_drapeau_info():", res3)"""

        """res4 = get_repere_proche(frame) 
        print("get_repere_info():", res4)"""

        """res5 = get_drapeaux(frame)
        print("get_drapeaux():", res5")"""

        # pour quitter proprement
        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
