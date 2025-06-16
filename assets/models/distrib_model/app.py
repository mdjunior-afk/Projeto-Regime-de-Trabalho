import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder='templates')

random_model = pickle.load(open('random_model.pkl', 'rb'))
tree_model = pickle.load(open('tree_model.pkl', 'rb'))

@app.route("/", methods=['GET'])
def verifica_api_online():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    random_pred = random_model.predict([data])
    tree_pred = tree_model.predict([data])
    random_result = int(random_pred[0])
    tree_result = int(tree_pred[0])

    mapping = {
       0: 'Modelo 100% presencial',
       1: 'Modelo 100% remoto',
       2: 'Modelo híbrido'
    }

    response = {'Trabalho ideal (Random)': mapping.get(random_result, 'Desconhecido'),
                'Trabalho ideal (DecisionTree)': mapping.get(tree_result, 'Desconhecido')}
    return jsonify(response)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)