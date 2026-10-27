from flask import Flask
import controller

"""
Ressources utiles :
https://flask.palletsprojects.com/en/stable/quickstart/
"""

app = Flask(__name__)

try:
    c = controller.Controller()
    c.set_motor_shutdown_timeout(2)
except Exception as e:
    print(f"Une erreur est survenue : {e}")


@app.route("/")
def hello():
    return("Bienvenue sur le serveur")


@app.route("/avance")
def avancer():
    print("Appel fonction Avancer")
    try:
        c.set_motor_speed(50, 50)
        return("Avancer : succès")
    except Exception as e:
        return("Erreur dans avancer : {e}")


@app.route("/")
def gauche():
    print("Appel fonction Gauche")
    try:
        c.set_motor_speed(-50,50)
        return("Gauche : succès")
    except Exception as e:
        return("Erreur dans gauche : {e}")

"""
A faire : vérifier les fonction et ajouter droite/recul
"""

if __name__ == "__main__":
    print("Lancement du serveur de controle (mode manuel)")
    app.run(host='0.0.0.0', port=5000)