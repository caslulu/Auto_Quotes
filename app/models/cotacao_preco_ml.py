from app.extensions import db

class CotacaoPrecoML(db.Model):
    __tablename__ = 'cotacao_preco_ml'

    id = db.Column(db.Integer, primary_key=True)
    # Dados principais da cotação
    genero = db.Column(db.String(50), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    tempo_de_seguro = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.String(50), nullable=False)
    tempo_no_endereco = db.Column(db.String(50), nullable=False)
    estado_civil = db.Column(db.String(20), nullable=False, default='Solteiro')
    nome_conjuge = db.Column(db.String(100))
    data_nascimento_conjuge = db.Column(db.String(50))
    documento_conjuge = db.Column(db.String(50))
    vehicles_json = db.Column(db.Text, nullable=False)
    pessoas_json = db.Column(db.Text, nullable=False, default='[]')
    trello_card_id = db.Column(db.String(100))
    # Preços
    preco_basico = db.Column(db.Float)  # Preço do seguro básico
    preco_full = db.Column(db.Float)    # Preço do seguro completo/full
    tipo_veiculo = db.Column(db.String(20))  # 'financiado' ou 'quitado'
    # Timestamp
    criado_em = db.Column(db.DateTime, server_default=db.func.now())
