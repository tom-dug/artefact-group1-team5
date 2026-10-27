import cv2
import numpy as np

CAMERA_ID = 1  # Webcam intégrée

# Charger la matrice caméra et la distorsion
camera_matrix = np.load("camera_matrix.npy")
dist_coeffs = np.load("dist_coeffs.npy")

cap = cv2.VideoCapture(CAMERA_ID)

print("=== Test Calibration ===")
print("Appuie sur 'q' pour quitter.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Image corrigée (undistortion)
    undistorted = cv2.undistort(frame, camera_matrix, dist_coeffs)

    # Affichages
    cv2.imshow("Original", frame)
    cv2.imshow("Corrected (Undistorted)", undistorted)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
