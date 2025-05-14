from flask import Blueprint, render_template, request
from app.models.cotacao_db import Cotacao
from app.forms.preco_form import PrecoForm_quitado, PrecoForm_financiado

from app.services.Canva_Banner.preco_automatico import PrecoAutomatico

from app.services.cotacao_service import processar_preco_quitado, processar_preco_financiado

colocarPreco_bp = Blueprint('colocarPreco', __name__)




@colocarPreco_bp.route('/colocarPreco', methods=['GET', 'POST'])
def colocarPreco():
    imagem = PrecoAutomatico()
    preco_form_financiado = PrecoForm_financiado()
    preco_form_quitado = PrecoForm_quitado()

    # Verifique qual formulário foi enviado
    form_type = None
    if 'form_type' in request.form:
        form_type = request.form['form_type']

    if form_type == 'financiado' and preco_form_financiado.validate_on_submit():
        print("FINANCIADO")
        dados = processar_preco_financiado(preco_form_financiado)
        imagem.financiado(**dados)
        return render_template('preco.html', form_financiado=preco_form_financiado, form_quitado=preco_form_quitado)

    elif form_type == 'quitado' and preco_form_quitado.validate_on_submit():
        print("QUITADO")
        dados = processar_preco_quitado(preco_form_quitado)
        imagem.quitado(**dados)
        return render_template('preco.html', form_financiado=preco_form_financiado, form_quitado=preco_form_quitado)

    return render_template('preco.html', form_financiado=preco_form_financiado, form_quitado=preco_form_quitado)