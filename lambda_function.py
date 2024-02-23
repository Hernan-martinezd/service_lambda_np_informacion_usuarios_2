import awsgi
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_data():
    """Endpoint para obtener los datos de salud."""
        health_metrics = {
            "frecuencia cardíaca": 72,        # bpm 
            "potencia umbral funcional": 250,  # en watts 
            "saturación de oxígeno": 98,       # Porcentaje
            "velocidad": 5.5,                  # en km/h
            "distancia recorrida": 10.2        # en km
        }
        return jsonify(status=200, data=health_metrics)

def lambda_handler(event, context):
    """Handler para AWS Lambda."""
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
