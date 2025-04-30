from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Date

db = SQLAlchemy()

class Base(DeclarativeBase):
    pass

class Cotacao(db.Model):
    __tablename__ = 'cotacao'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    genero: Mapped[str] = mapped_column(String(50))
    nome: Mapped[str] = mapped_column(String(100))
    documento: Mapped[str] = mapped_column(String(50))
    endereco: Mapped[str] = mapped_column(String(200))
    financiado: Mapped[str] = mapped_column(String(10))
    tempo_de_seguro: Mapped[str] = mapped_column(String(50))
    vin: Mapped[str] = mapped_column(String(50))
    data_nascimento: Mapped[Date] = mapped_column(Date)
    tempo_com_veiculo: Mapped[str] = mapped_column(String(50))
    tempo_no_endereco: Mapped[str] = mapped_column(String(50))