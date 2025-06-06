"""
Exporta dados de cotações do banco para um arquivo CSV para uso em Machine Learning.
"""
import pandas as pd
from app.models.cotacao_db import Cotacao
from app import db
import json

def exportar_cotacoes_para_csv(csv_path='cotacoes_ml.csv'):
    cotacoes = Cotacao.query.all()
    registros = []
    for cot in cotacoes:
        d = {
            'genero': cot.genero,
            'nome': cot.nome,
            'documento': cot.documento,
            'endereco': cot.endereco,
            'tempo_de_seguro': cot.tempo_de_seguro,
            'data_nascimento': cot.data_nascimento,
            'tempo_no_endereco': cot.tempo_no_endereco,
            'estado_civil': cot.estado_civil,
            'nome_conjuge': cot.nome_conjuge,
            'data_nascimento_conjuge': cot.data_nascimento_conjuge,
            'documento_conjuge': cot.documento_conjuge,
            'veiculos': cot.vehicles_json,
            'pessoas': cot.pessoas_json,
            # Adicione outros campos relevantes
        }
        # Se houver campo de preço real, inclua
        if hasattr(cot, 'preco'):
            d['preco'] = cot.preco
        registros.append(d)
    df = pd.DataFrame(registros)
    df.to_csv(csv_path, index=False)
    print(f'Exportado para {csv_path}')

if __name__ == '__main__':
    exportar_cotacoes_para_csv()
