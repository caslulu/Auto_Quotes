"""
Funções utilitárias para pré-processamento de features de cotação para ML.
Reutilize em treino e predição para garantir consistência.
"""
import json
from datetime import datetime

def preprocess_cotacao_features(dados):
    # Garante que veiculos e pessoas são listas
    if 'veiculos' in dados and isinstance(dados['veiculos'], str):
        try:
            dados['veiculos'] = json.loads(dados['veiculos'])
        except Exception:
            dados['veiculos'] = []
    if 'pessoas' in dados and isinstance(dados['pessoas'], str):
        try:
            dados['pessoas'] = json.loads(dados['pessoas'])
        except Exception:
            dados['pessoas'] = []
    # Contagem
    dados['num_veiculos'] = len(dados.get('veiculos', []))
    dados['num_pessoas'] = len(dados.get('pessoas', []))
    # Idade titular
    idade = None
    if 'data_nascimento' in dados:
        try:
            for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
                try:
                    nasc = datetime.strptime(dados['data_nascimento'], fmt)
                    break
                except Exception:
                    nasc = None
            if nasc:
                hoje = datetime.now()
                idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
        except Exception:
            idade = None
    dados['idade'] = idade if idade is not None else 0
    # Idade cônjuge
    idade_conjuge = None
    if 'data_nascimento_conjuge' in dados and dados['data_nascimento_conjuge']:
        try:
            for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
                try:
                    nasc = datetime.strptime(dados['data_nascimento_conjuge'], fmt)
                    break
                except Exception:
                    nasc = None
            if nasc:
                hoje = datetime.now()
                idade_conjuge = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
        except Exception:
            idade_conjuge = None
    dados['idade_conjuge'] = idade_conjuge if idade_conjuge is not None else 0
    # Idades adicionais
    idades_adicionais = []
    for pessoa in dados.get('pessoas', []):
        idade_p = 0
        if pessoa.get('data_nascimento'):
            try:
                for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
                    try:
                        nasc = datetime.strptime(pessoa['data_nascimento'], fmt)
                        break
                    except Exception:
                        nasc = None
                if nasc:
                    hoje = datetime.now()
                    idade_p = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
            except Exception:
                idade_p = 0
        idades_adicionais.append(idade_p)
    if idades_adicionais:
        dados['idade_adicional_media'] = sum(idades_adicionais) / len(idades_adicionais)
        dados['idade_adicional_min'] = min(idades_adicionais)
        dados['idade_adicional_max'] = max(idades_adicionais)
        dados['idade_adicional_soma'] = sum(idades_adicionais)
    else:
        dados['idade_adicional_media'] = 0
        dados['idade_adicional_min'] = 0
        dados['idade_adicional_max'] = 0
        dados['idade_adicional_soma'] = 0
    # Remove campos não usados
    for k in ['veiculos', 'pessoas', 'nome', 'documento', 'data_nascimento', 'nome_conjuge', 'data_nascimento_conjuge', 'documento_conjuge']:
        dados.pop(k, None)
    return dados
