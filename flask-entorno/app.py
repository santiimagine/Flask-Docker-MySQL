from flask import Flask
import os

app = Flask(__name__)

# Detectar entorno desde variable ENVIRONMENT
environment = os.getenv("ENVIRONMENT", "development")

if environment == "development":
    app.config["DEBUG"] = True
else:
    app.config["DEBUG"] = False

@app.route("/")
def home():
    return f"Servidor Flask corriendo en entorno: {environment}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
