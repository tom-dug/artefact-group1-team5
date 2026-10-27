import cv2
import numpy as np
import glob

# === PARAMÈTRES DU DAMIER ===
CHECKERBOARD = (10, 7)

# Préparation des points 3D pour le damier
objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

objpoints = []  # points 3D
imgpoints = []  # points 2D

# Charger les images
images = glob.glob('calib_images/*.png')

if len(images) == 0:
    print("❌ Aucune image trouvée dans calib_images/*.png")
    exit()

print(f"📸 {len(images)} images trouvées pour la calibration.")

for img_name in images:
    img = cv2.imread(img_name)
    if img is None:
        print(f"⚠️ Impossible de lire : {img_name}")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Détection du damier
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if ret:
        # Raffinement sous-pixel
        criteria = (
            cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
            30,
            0.001,
        )

        refined = cv2.cornerSubPix(
            gray,
            corners,
            (11, 11),
            (-1, -1),
            criteria
        )

        imgpoints.append(refined)
        objpoints.append(objp)

    else:
        print(f"❌ Damier NON détecté dans : {img_name}")

# Vérifications
if len(objpoints) == 0:
    print("❌ Aucun damier détecté dans TOUTES les images.")
    exit()

print(f"\n✔ {len(objpoints)} images utilisables pour la calibration.")

# === Calibration ===
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    objpoints,
    imgpoints,
    gray.shape[::-1],
    None,
    None
)

print("\n===== CALIBRATION TERMINÉE =====")
print("📌 Camera Matrix :\n", camera_matrix)
print("\n📌 Distortion Coefficients :\n", dist_coeffs)

# Sauvegarde
np.save("camera_matrix.npy", camera_matrix)
np.save("dist_coeffs.npy", dist_coeffs)

print("\n💾 Fichiers enregistrés : camera_matrix.npy et dist_coeffs.npy")
