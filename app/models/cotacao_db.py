from app.extensions import db

class Cotacao(db.Model):
    __tablename__ = 'cotacao'

    id = db.Column(db.Integer, primary_key=True)
    genero = db.Column(db.String(50), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    financiado = db.Column(db.String(50), nullable=False)
    tempo_de_seguro = db.Column(db.String(50), nullable=False)
    vin = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.String(50), nullable=False)
    tempo_com_veiculo = db.Column(db.String(50), nullable=False)
    tempo_no_endereco = db.Column(db.String(50), nullable=False)
    trello_card_id = db.Column(db.String(100))
    