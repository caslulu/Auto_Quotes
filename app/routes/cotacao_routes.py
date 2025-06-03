from flask import Blueprint, render_template, redirect, url_for
from app.forms.cotacao_form import CotacaoForm
from app.forms.seguradora_form import SeguradoraForm
from app.models.cotacao_db import Cotacao
from app.services.cotacao_service import extrair_dados_formulario
from app.services.trello_service import Trello
from app.extensions import db
import json

cotacao_bp = Blueprint('cotacao', __name__)

@cotacao_bp.route('/', methods=['GET', 'POST'])
def cotacao():
    cotacao_form = CotacaoForm()
    seguradora_form = SeguradoraForm()

    # Garante que o FieldList tenha entradas suficientes para todos os veículos enviados
    if cotacao_form.is_submitted():
        veiculos_count = 0
        while f"veiculos-{veiculos_count}-vin" in (cotacao_form.data or {}):
            veiculos_count += 1
        while len(cotacao_form.veiculos.entries) < veiculos_count:
            cotacao_form.veiculos.append_entry()

    if cotacao_form.validate_on_submit():
        dados = extrair_dados_formulario(cotacao_form)
        trello_card_id = None
        if cotacao_form.colocar_trello.data:
            trello = Trello()
            email = f"{dados['nome'].lower().replace(' ', '')}@outlook.com"
            # Remove o campo 'veiculos' apenas para o Trello
            trello_card_id = trello.criar_carta(
                **{k: v for k, v in dados.items() if k != 'veiculos'},
                veiculos=json.dumps(dados['veiculos']),
                email=email
            )
        cotacao = Cotacao(
            genero=dados['genero'],
            nome=dados['nome'],
            documento=dados['documento'],
            endereco=dados['endereco'],
            tempo_de_seguro=dados['tempo_de_seguro'],
            data_nascimento=dados['data_nascimento'],
            tempo_no_endereco=dados['tempo_no_endereco'],
            estado_civil=dados['estado_civil'],
            nome_conjuge=dados['nome_conjuge'],
            data_nascimento_conjuge=dados['data_nascimento_conjuge'],
            documento_conjuge=dados['documento_conjuge'],
            vehicles_json=json.dumps(dados['veiculos']),
            pessoas_json=json.dumps(dados.get('pessoas', [])),
            trello_card_id=trello_card_id
        )
        db.session.add(cotacao)
        db.session.commit()
        return redirect(url_for('cotacao.cotacao'))

    if cotacao_form.errors:
        print("Erro na validação do formulário:", cotacao_form.errors)

    cotacoes = Cotacao.query.all()
    return render_template('cotacao.html', form=cotacao_form, cotacoes=cotacoes, form_seguradora=seguradora_form)