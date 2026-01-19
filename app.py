# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Expect: {"features": [sepal length, sepal width, petal length, petal width]}
    features = np.array(data['features']).reshape(1, -1)
    pred = int(model.predict(features)[0])
    return jsonify({"prediction": pred})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

