from flask import Blueprint, render_template, redirect, url_for
from app.forms.cotacao_form import CotacaoForm
from app.forms.seguradora_form import SeguradoraForm
from app.models.cotacao_db import Cotacao
from app.services.cotacao_service import CotacaoService

cotacao_bp = Blueprint('cotacao', __name__)
cotacao_service = CotacaoService()

@cotacao_bp.route('/', methods=['GET', 'POST'])
def cotacao():
    cotacao_form = CotacaoForm()
    seguradora_form = SeguradoraForm()


    if cotacao_form.validate_on_submit():
        adicionar_conjuge = getattr(cotacao_form, "adicionar_conjuge", None)
        if adicionar_conjuge and adicionar_conjuge.data:
            erros = False
            if not cotacao_form.nome_conjuge.data:
                cotacao_form.nome_conjuge.errors.append("Campo obrigatório.")
                erros = True
            if not cotacao_form.data_nascimento_conjuge.data:
                cotacao_form.data_nascimento_conjuge.errors.append("Campo obrigatório.")
                erros = True
            if not cotacao_form.documento_conjuge.data:
                cotacao_form.documento_conjuge.errors.append("Campo obrigatório.")
                erros = True
            if erros:
                cotacoes = Cotacao.query.all()
                return render_template('cotacao.html', form=cotacao_form, cotacoes=cotacoes, form_seguradora=seguradora_form)
        cotacao_service.criar_cotacao(cotacao_form)
        return redirect(url_for('cotacao.cotacao'))

    if cotacao_form.errors:
        print("Erro na validação do formulário:", cotacao_form.errors)

    cotacoes = Cotacao.query.all()
    return render_template('cotacao.html', form=cotacao_form, cotacoes=cotacoes, form_seguradora=seguradora_form)