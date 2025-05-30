# Exemplo de endpoint Flask para previsão de preço de cotação usando modelo ML
from flask import Blueprint, request, jsonify
import joblib
import pandas as pd
from ml.preprocessing import preprocess_cotacao_features

predict_bp = Blueprint('predict', __name__)

# Carregue o modelo uma vez ao iniciar
model = joblib.load('ml/modelo_preco_cotacao.pkl')

@predict_bp.route('/api/prever_preco', methods=['POST'])
def prever_preco():
    dados = request.get_json()
    dados = preprocess_cotacao_features(dados)
    X = pd.DataFrame([dados])
    preco_predito = model.predict(X)[0]
    return jsonify({'preco_predito': float(preco_predito)})