"""
TP COMPOSE — l'API.

Deux adresses sont disponibles :

  GET /api/health  → vérifie que la base de données répond (utilisé par Docker)
  GET /api/hello   → enregistre une visite dans la base et renvoie le message

Aucun mot de passe n'est écrit ici : tout vient des variables d'environnement
déclarées dans docker-compose.yml (elles-mêmes lues dans le fichier .env).
"""

import os

import redis
from flask import Flask, jsonify

app = Flask(__name__)

# On veut des accents lisibles dans le JSON ("données" plutôt que "donn\u00e9es").
app.json.ensure_ascii = False

# --- Connexion à la base de données (Redis) --------------------------------
base = redis.Redis(
    host=os.environ.get("REDIS_HOST", "db"),
    port=int(os.environ.get("REDIS_PORT", "6379")),
    password=os.environ.get("REDIS_PASSWORD"),
    decode_responses=True,  # renvoie du texte au lieu d'octets binaires
)


# --- La route principale ---------------------------------------------------
@app.route("/api/hello")
def hello():
    # 1. On ÉCRIT dans la base : +1 sur le compteur "visites".
    visites = base.incr("visites")

    # 2. On LIT le message de bienvenue.
    #    La première fois il n'existe pas : on le crée.
    message = base.get("message")
    if message is None:
        message = "Hello World, la base de données répond !"
        base.set("message", message)

    # 3. On renvoie ces informations au front, au format JSON.
    return jsonify(message=message, visites=visites)


# --- La route de santé -----------------------------------------------------
@app.route("/api/health")
def health():
    # "ping" répond True si Redis est joignable : c'est notre preuve
    # que la liaison API <-> base de données fonctionne.
    base.ping()
    return jsonify(etat="ok", base="connectée")


if __name__ == "__main__":
    # Serveur de développement Flask : très bien pour un TP,
    # pas pour de la production (on utiliserait gunicorn).
    app.run(host="0.0.0.0", port=5000)
