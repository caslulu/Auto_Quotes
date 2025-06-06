# Exemplo de pipeline para Machine Learning
# Use este script para treinar e salvar um modelo de previsão de preço de cotação

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from ml.preprocessing import preprocess_cotacao_features

# Carregue seu dataset (exemplo: exportado do banco para CSV)
df = pd.read_csv('cotacoes_ml.csv')

# Selecione features e target
X = df.drop(['preco'], axis=1)
y = df['preco']

# Pré-processamento das features para cada linha do DataFrame
X = X.apply(lambda row: preprocess_cotacao_features(row.to_dict()), axis=1, result_type='expand')

# Divida em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treine o modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avalie
score = model.score(X_test, y_test)
print(f'R2 Score: {score:.2f}')

# Salve o modelo
joblib.dump(model, 'modelo_preco_cotacao.pkl')
print('Modelo salvo em modelo_preco_cotacao.pkl')
