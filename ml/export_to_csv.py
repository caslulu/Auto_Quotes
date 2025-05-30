# Script para exportar dados do banco para CSV para uso em ML
import pandas as pd
from app import create_app
from app.models.cotacao_preco_ml import CotacaoPrecoML
from app.extensions import db

app = create_app()

with app.app_context():
    cotacoes = CotacaoPrecoML.query.all()
    dados = []
    for c in cotacoes:
        row = dict(
            id=c.id,
            cotacao_id=c.cotacao_id,
            preco=c.preco,
            data_registro=c.data_registro,
            observacao=c.observacao
        )
        # Adiciona os campos do JSON de dados_cotacao
        try:
            import json
            dados_json = json.loads(c.dados_cotacao)
            for k, v in dados_json.items():
                row[k] = v
        except Exception:
            pass
        dados.append(row)
    df = pd.DataFrame(dados)
    df.to_csv('cotacoes_ml.csv', index=False)
    print('Exportado para cotacoes_ml.csv')
