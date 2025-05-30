from app.extensions import db

class CotacaoPrecoML(db.Model):
    __tablename__ = 'cotacao_preco_ml'

    id = db.Column(db.Integer, primary_key=True)
    cotacao_id = db.Column(db.Integer, nullable=False)  # Referência ao id da cotação original
    dados_cotacao = db.Column(db.Text, nullable=False)  # JSON com todos os dados da cotação
    preco = db.Column(db.Float, nullable=True)  # Preço preenchido posteriormente
    data_registro = db.Column(db.DateTime, server_default=db.func.now())
    observacao = db.Column(db.String(255))
