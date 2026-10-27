import cv2
import os
import time

# ------------------------ #
#   PARAMÈTRES À MODIFIER
# ------------------------ #

NB_IMAGES = 30
DELAY_MS = 1000          # 1 seconde
PATTERN_SIZE = (10,7)    # damier officiel
CAMERA_ID = 0            # USB = 1, webcam PC = 0

# ------------------------ #

save_dir = "calib_images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(CAMERA_ID)

if not cap.isOpened():
    print("❌ Erreur : impossible d'ouvrir la caméra.")
    exit()

print("=== Début de la capture ===")
print("Montre le damier à la caméra.")
print("Appuie sur 'q' pour quitter.\n")

count = 0

while count < NB_IMAGES:
    ret, frame = cap.read()
    if not ret:
        print("❌ Erreur capture caméra.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Lissage pour meilleure détection
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Détection du damier
    found, corners = cv2.findChessboardCorners(gray_blur, PATTERN_SIZE, None)
    
    # Affichage pour feedback
    display = frame.copy()
    if found:
        cv2.drawChessboardCorners(display, PATTERN_SIZE, corners, found)

    cv2.putText(
        display,
        f"Image {count}/{NB_IMAGES}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # cv2.imshow("Capture calibration", display)
    
    # Sauvegarde image si damier détecté
    if found:
        print(f"✔ Damier trouvé → capture dans {DELAY_MS/1000:.1f}s...")
        time.sleep(DELAY_MS / 1000.0)

        filename = os.path.join(save_dir, f"calib_{count}.png")
        cv2.imwrite(filename, frame)

        print(f"💾 Image enregistrée : {filename}")
        count += 1

    key = cv2.waitKey(1)
    if key == ord('q'):
        print("📌 Capture interrompue par l'utilisateur.")
        break

cap.release()
#cv2.destroyAllWindows()

print("\n=== Capture terminée ===")
print(f"{count}/{NB_IMAGES} images ont été enregistrées dans '{save_dir}'")
