from flask import Blueprint, render_template, request
from app.models.cotacao_db import Cotacao
from app.forms.preco_form import PrecoForm_quitado, PrecoForm_financiado
from app.forms.seguradora_form import SeguradoraForm

from app.services.Canva_Banner.preco_automatico import PrecoAutomatico

from app.services.cotacao_service import processar_preco_quitado, processar_preco_financiado

colocarPreco_bp = Blueprint('colocarPreco', __name__)




@colocarPreco_bp.route('/colocarPreco', methods=['GET', 'POST'])
def colocarPreco():
    # Crie instâncias dos formulários e do modelo de cotação

    imagem = PrecoAutomatico()
    preco_form_financiado = PrecoForm_financiado()
    preco_form_quitado = PrecoForm_quitado()
    seguradora_form = SeguradoraForm()


    context = {
        'form_financiado': preco_form_financiado,
        'form_quitado': preco_form_quitado,
        'form_seguradora': seguradora_form
    }

    # Verifique se o formulário foi enviado
    form_type = None
    if 'form_type' in request.form:
        form_type = request.form['form_type']

    # Verifique se o tipo de formulário é 'financiado' ou 'quitado'
    if form_type == 'financiado' and preco_form_financiado.validate_on_submit():
        print("FINANCIADO")
        dados = processar_preco_financiado(preco_form_financiado, seguradora_form=seguradora_form)
        seguradora = request.form.get('seguradora')
        imagem.financiado(**dados, seguradora=seguradora)


    elif form_type == 'quitado' and preco_form_quitado.validate_on_submit():
        print("QUITADO")
        seguradora = request.form.get('seguradora')
        dados = processar_preco_quitado(preco_form_quitado, seguradora_form=seguradora_form)
        imagem.quitado(**dados, seguradora=seguradora)

    return render_template('preco.html', **context) 