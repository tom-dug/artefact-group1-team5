from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import datetime

def log(text, color="black"):
    print(f"Console : {text}")
    now = datetime.datetime.now()
    now_str = now.strftime("%H:%M:%S")
    emit('csl', {'text': f"{now_str} - {text}", 'color': color, 'raw_text': text})

def log_action(action):
    log(f"Commande reçue : {action}", color="blue")
