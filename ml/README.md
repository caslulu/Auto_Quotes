# ML Pipeline - Auto Quotes

Este diretório contém scripts e utilitários para exportação de dados, pré-processamento, treino e predição de preços de cotações de seguro.

## Scripts principais

- `export_to_csv.py`: Exporta dados do banco para um arquivo CSV para uso em Machine Learning.
- `preprocessing.py`: Funções utilitárias para pré-processamento de features, usadas tanto no treino quanto na predição.
- `train_model.py`: Treina e salva um modelo de previsão de preço de cotação.
- `predict_endpoint.py`: Endpoint Flask para previsão de preço via modelo ML.

## Como usar

1. **Exportar dados para CSV:**
   ```bash
   python ml/export_to_csv.py
   ```
2. **Treinar o modelo:**
   ```bash
   python ml/train_model.py
   ```
3. **Rodar o endpoint de predição:**
   ```bash
   flask run -m ml.predict_endpoint
   ```

Certifique-se de instalar as dependências:
```bash
pip install pandas scikit-learn joblib flask
```

O arquivo `cotacoes_ml.csv` deve conter as colunas usadas no pipeline, incluindo as listas de veículos e pessoas em formato JSON.
