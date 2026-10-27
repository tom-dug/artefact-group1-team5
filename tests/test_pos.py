import sys
from controle import communication

"""
On teste ici la capacité à envoyer une requête de mise à jour de la position X, Y
ainsi que de l'orientation alpha au serveur de suivi.
"""

def main():
    if len(sys.argv) < 4:
        print("ERREUR : Arguments manquants")
        print("Usage : python3 test_communication.py <X> <Y> <Angle>")
        return

    try:
        x_val = float(sys.argv[1])
        y_val = float(sys.argv[2])
        angle_val = float(sys.argv[3])
    except ValueError:
        print("ERREUR : X, Y et Angle doivent être des nombres")
        return

    print(f"Tentative d'envoi : X={x_val}, Y={y_val}, Angle={angle_val}")

    succes = communication.envoyer_position(x_val, y_val, angle_val)

    if succes:
        print("[SUCCÈS] La fonction envoyer_position a retourné True")
        print("Le serveur a probablement reçu la requête (code 200)")
    else:
        print("[ÉCHEC] La fonction envoyer_position a retourné False")
        print("Vérifiez que le serveur est lancé et l'URL correcte")

main()