from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from datetime import datetime
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

from forms import CotacaoForm
from models import db, Cotacao
from progressive import Progressive
from data_funcoes import decodificar_vin, formatar_data, separar_nome, separar_documento, separar_endereco, veiculo_vin
from trello import Trello
load_dotenv()




app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = 'your_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cotacao.db"

# Inicializa o banco de dados
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def cotacao():
    cotacao_form = CotacaoForm()
    if cotacao_form.validate_on_submit():
        genero = cotacao_form.genero.data
        nome = cotacao_form.nome.data
        documento, estado_documento = separar_documento(cotacao_form.documento.data)
        endereco = cotacao_form.endereco.data
        financiado = cotacao_form.financiado.data
        tempo_de_seguro = cotacao_form.tempo_de_seguro.data
        vin = cotacao_form.vin.data
        data_nascimento = datetime.strptime(cotacao_form.data_nascimento.data, '%m/%d/%Y').date()
        tempo_com_veiculo = cotacao_form.tempo_com_veiculo.data
        tempo_no_endereco = cotacao_form.tempo_no_endereco.data
        if cotacao_form.colocar_trello.data:
            trello = Trello()
            veiculos = veiculo_vin(vin)
            trello.criar_carta(nome, estado_documento, veiculos, documento, endereco, vin, financiado, tempo_de_seguro, data_nascimento, tempo_no_endereco, tempo_com_veiculo)


        cotacao = Cotacao(
            genero=genero,
            nome=nome,
            documento=documento,
            endereco=endereco,
            financiado=financiado,
            tempo_de_seguro=tempo_de_seguro,
            vin=vin,
            data_nascimento=data_nascimento,
            tempo_com_veiculo=tempo_com_veiculo,
            tempo_no_endereco=tempo_no_endereco
        )
        with app.app_context():
            db.session.add(cotacao)
            db.session.commit()



        return redirect(url_for('cotacao'))

    return render_template('cotacao.html', form=cotacao_form)


@app.route('/cotar', methods=['GET'])
def cotar():
    try:
        primeiro = Cotacao.query.first()
        if primeiro:
            executar_cotacao(primeiro)
            return "Cotação processada com sucesso!"
        else:
            return render_template('cotar.html', cotacao=None)
    except Exception as e:
        print(f"Erro ao processar cotação: {e}")
        return render_template('erro.html', mensagem="Erro ao processar cotação")


def executar_cotacao(primeiro):
    dados = processar_cotacao(primeiro)
    email = os.getenv("EMAIL")
    if not email:
        raise ValueError("EMAIL não configurado")
    p = Progressive()
    with sync_playwright() as playwright:
        p.cotacao(playwright, email=email, **dados)


def processar_cotacao(primeiro):
    genero = primeiro.genero
    first_name, last_name = separar_nome(primeiro.nome)
    documento, estado_documento = separar_documento(primeiro.documento)
    rua, apt, cidade, zipcode = separar_endereco(primeiro.endereco)
    financiado = primeiro.financiado
    tempo_de_seguro = primeiro.tempo_de_seguro
    lista_vin = decodificar_vin(primeiro.vin)
    nascimento = formatar_data(primeiro.data_nascimento.strftime("%m/%d/%Y"))
    tempo_com_veiculo = primeiro.tempo_com_veiculo
    tempo_no_endereco = primeiro.tempo_no_endereco
    return {
        "genero": genero,
        "first_name": first_name,
        "last_name": last_name,
        "estado_documento": estado_documento,
        "rua": rua,
        "apt": apt,
        "cidade": cidade,
        "zipcode": zipcode,
        "financiado": financiado,
        "tempo_de_seguro": tempo_de_seguro,
        "lista_vin": lista_vin,
        "nascimento": nascimento,
        "tempo_com_veiculo": tempo_com_veiculo,
        "tempo_no_endereco": tempo_no_endereco,
    }

            

if __name__ == '__main__':
    app.run(debug=True)