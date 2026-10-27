from flask import Flask, Response, render_template
import cv2
import time

app = Flask(__name__)

# OUVERTURE DIRECTE DE LA CAMÉRA SANS VisionRobot
cap = cv2.VideoCapture(0)

def gen_frames():
    while True:
        time.sleep(0.05)
        ok, frame = cap.read()
        print("FRAME:", ok, frame is not None)  # DEBUG IMPORTANT

        if not ok or frame is None:
            continue

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
        )

@app.route("/")
def index():
    return render_template("test_camera.html")

@app.route("/video_feed")
def video_feed():
    return Response(
        gen_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)

