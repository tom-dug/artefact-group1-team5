import cv2
import numpy as np
import math

# === LOAD CAMERA CALIBRATION ===
camera_matrix = np.load("camera/camera_matrix.npy")
dist_coeffs   = np.load("camera/dist_coeffs.npy")

# === ARUCO SETUP (API compatible OpenCV 4.6.0) ===
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
parameters = cv2.aruco.DetectorParameters_create()

def rvec_to_euler(rvec):
    """Convertit le vecteur de rotation en angles roll/pitch/yaw."""
    R, _ = cv2.Rodrigues(rvec)
    sy = math.sqrt(R[0,0]**2 + R[1,0]**2)

    if sy < 1e-6:
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
    else:
        x = math.atan2(R[2,1], R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])

    return np.degrees([x, y, z])

# === CAMERA ===
cap = cv2.VideoCapture(1)
print("=== ArUco Pose (OpenCV 4.6.0 Compatible) ===")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    corners, ids, _ = cv2.aruco.detectMarkers(frame, arucoDict, parameters=parameters)

    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for i, marker_id in enumerate(ids.flatten()):
            imgp = corners[i].reshape((4, 2)).astype(np.float32)

            # Taille du marker selon type
            if marker_id in [1, 2, 3]:      # Repères fixes
                marker_length = 10.0        # cm
            else:
                marker_length = 2.0         # Drapeaux

            # Construction 3D du carré
            s = marker_length / 2
            objp = np.array([
                [-s,  s, 0],
                [ s,  s, 0],
                [ s, -s, 0],
                [-s, -s, 0]
            ], dtype=np.float32)

            ok, rvec, tvec = cv2.solvePnP(objp, imgp, camera_matrix, dist_coeffs)

            if ok:
                x, y, z = tvec.flatten()
                distance = np.linalg.norm(tvec)
                roll, pitch, yaw = rvec_to_euler(rvec)

                print(f"\n=== ID {marker_id} ===")
                print(f"Type : {'Repère' if marker_id in [1,2,3] else 'Drapeau'}")
                print(f"Distance = {distance:.2f} cm")
                print(f"tvec = X={x:.2f}, Y={y:.2f}, Z={z:.2f}")
                print(f"Angles° : Roll={roll:.1f} | Pitch={pitch:.1f} | Yaw={yaw:.1f}")

                cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvec, tvec, marker_length)


    cv2.imshow("Aruco Pose - OpenCV 4.6.0", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
