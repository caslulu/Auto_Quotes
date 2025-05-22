from flask import Blueprint, render_template, redirect, url_for
from app.forms.cotacao_form import CotacaoForm
from app.forms.seguradora_form import SeguradoraForm
from app.models.cotacao_db import Cotacao
from app.services.cotacao_service import extrair_dados_formulario
from app.services.trello_service import Trello
from app.util.data_funcoes import veiculo_vin
from app.extensions import db

cotacao_bp = Blueprint('cotacao', __name__)

@cotacao_bp.route('/', methods=['GET', 'POST'])
def cotacao():
    cotacao_form = CotacaoForm()
    seguradora_form = SeguradoraForm()
    if cotacao_form.validate_on_submit():
        print("Formulário enviado com sucesso!")
        dados = extrair_dados_formulario(cotacao_form)
        print("Dados extraídos:", dados)

        if cotacao_form.colocar_trello.data:
            print("Checkbox 'Colocar Trello' marcado.")
            trello = Trello()
            veiculos = veiculo_vin(dados["vin"])
            email = f"{dados["nome"].lower().replace(" ", "")}@outlook.com"
            trello.criar_carta(**dados, veiculos=veiculos, email=email)
            print("Carta criada no Trello.")

        cotacao = Cotacao(**dados)
        db.session.add(cotacao)
        db.session.commit()
        print("Dados salvos no banco de dados.")

        return redirect(url_for('cotacao.cotacao'))
    else:
        print("Erro na validação do formulário:", cotacao_form.errors)
    cotacoes = Cotacao.query.all()    

    return render_template('cotacao.html', form=cotacao_form, cotacoes=cotacoes, form_seguradora=seguradora_form)