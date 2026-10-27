from flask import Flask, Response, render_template, request
from flask_socketio import SocketIO, emit
import json
from controle import main
from batterie import controle_batterie
import asyncio
import cv2
import math
from web import console
from controle import communication
from tests import test_controle
from controle import puppet
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(
    app,
    cors_allowed_origins="*"
)

robot = main.Robot()

'''cap = robot.vision.cam.cap

def gen_frames():
    while True:
        time.sleep(0.1) # Cet appel à time.sleep ne bloque pas le reste du code
        ok, frame = cap.read()

        if not ok or frame is None:
            continue

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        if frame_bytes is not None:
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
            )'''


@app.route('/')
def home():
    return render_template('index.html')

'''@app.route("/video_feed")
def video_feed():
    return Response(
        gen_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )'''

async def upd_regulier():
    while True:
        await asyncio.sleep(0.2)
        console.log("Status update", color="purple")
        emit('upd', robot.get_status())
        handle_refresh_battery()

async def pos_regulier():
    while True:
        await asyncio.sleep(1)
        console.log("Pos update", color="purple")
        x, y = robot.pos
        communication.envoyer_position(x, y, int(robot.dir * 360 / (2 * math.pi)))

@socketio.on('command')  # Le serveur reçoit une commande du client
def handle_command(data):
    action = data.get('action')
    console.log_action(action)  # Affichage de la commande faite par l'utilisateur
    commandes = { # Relie les actions à la commande controlleur (TODO: remplacer avancer_test par autres commandes)
        "start_forward": robot.debut_avancer,
        "start_left": robot.debut_tourner_gauche,
        "start_backward": robot.debut_reculer,
        "start_right": robot.debut_tourner_droite,
        "end_forward": robot.fin_avancer,
        "end_left": robot.fin_tourner_gauche,
        "end_backward": robot.fin_reculer,
        "end_right": robot.fin_tourner_droite,
        "increase_calibrage_ar": robot.augmenter_calibrage_ar,
        "decrease_calibrage_ar": robot.baisser_calibrage_ar,
        "increase_calibrage_gd": robot.augmenter_calibrage_gd,
        "decrease_calibrage_gd": robot.baisser_calibrage_gd,
        "stop": robot.stop,
        "start": robot.start,
        "activate_status_upd": (lambda: asyncio.run(upd_regulier())),
        "activate_send_pos": (lambda: asyncio.run(pos_regulier())),
        "increase_ratio": robot.increase_ratio,
        "decrease_ratio": robot.decrease_ratio,
        "start_boost": robot.debut_boost,
        "end_boost": robot.fin_boost
    }
    commande = commandes[action]
    commande()
    emit('upd', robot.get_status()) # Update les infos robot après éxécution de l'action

@socketio.on('async_command')  # Le serveur reçoit une commande du client
def handle_do_async_command(data):
    action = data.get('action')
    console.log_action(action)  # Affichage de la commande faite par l'utilisateur
    commandes = { # Relie les actions à la commande controlleur (TODO: remplacer avancer_test par autres commandes)
        "forward": (lambda: robot.avancer(100)),
        "left": (lambda: robot.tourner_gauche(math.pi / 2)),
        "backward": (lambda: robot.reculer(100)),
        "right": (lambda: robot.tourner_droite(math.pi / 2)),
        "test_controle": (lambda: test_controle.lancer_test_controle(robot)),
        "lancer_puppet": (lambda: puppet.start_puppet(robot)),
        "lancer_strategie": (lambda: robot.strategie())
    }
    commande = commandes[action]
    asyncio.run(commande())
    emit('upd', robot.get_status()) # Update les infos robot après éxécution de l'action

@socketio.on('refresh_battery')
def handle_refresh_battery():
    soc = controle_batterie.update_soc()
    conso_mw = controle_batterie.update_conso()
    console.log_action('battery')
    emit('bat', {'status': 'ok', 'soc': soc, 'conso_mw': conso_mw})

print(">>> Serveur Flask-SocketIO en cours de démarrage sur http://127.0.0.1:5000/")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)

