from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)  # Esto habilita CORS para todas las rutas



# Cargar el modelo
with open('random_forest.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def Home():
    return 'La pagina prende'
        

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener datos de la solicitud
    data = request.get_json()

    # Crear un DataFrame con los datos recibidos
    new_data = pd.DataFrame({
        'Ranking': [data['Ranking']],
        'Ranking.1': [data['Ranking.1']],
        'RankingDif': [data['RankingDif']]
    })

    # Hacer predicciones
    prediction = model.predict(new_data)
    prediction_proba = model.predict_proba(new_data)

    # Crear una respuesta JSON
    response = {
        'prediction': int(prediction[0]),
        'probability': prediction_proba[0].tolist(),
        'Empate': prediction_proba[0][0],
        'Derrota': prediction_proba[0][1],
        'Victoria': prediction_proba[0][2]
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
