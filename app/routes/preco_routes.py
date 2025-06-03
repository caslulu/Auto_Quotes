from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.cotacao_db import Cotacao
from app.forms.preco_form import PrecoForm_quitado, PrecoForm_financiado
from app.forms.seguradora_form import SeguradoraForm
from app.services.trello_service import Trello
from app.services.Canva_Banner.preco_automatico import PrecoAutomatico
from app.services.cotacao_service import processar_preco_quitado, processar_preco_financiado
from sqlalchemy.orm.exc import NoResultFound

colocarPreco_bp = Blueprint('colocarPreco', __name__)

def anexar_imagem_a_cotacao(trello, cotacao, image_path):
    """Anexa uma imagem à carta do Trello vinculada à cotação e retorna True/False."""
    if cotacao and cotacao.trello_card_id:
        response = trello.anexar_imagem_trello(cotacao.trello_card_id, image_path)
        if response and (getattr(response, 'status_code', None) == 200 or response.get('status_code', None) == 200):
            return True
        else:
            print(f"Erro ao anexar imagem ao Trello: {getattr(response, 'text', response)}")
    return False

@colocarPreco_bp.route('/colocarPreco', methods=['GET', 'POST'])
def colocarPreco():
    trello = Trello()
    imagem = PrecoAutomatico()
    preco_form_financiado = PrecoForm_financiado()
    preco_form_quitado = PrecoForm_quitado()
    seguradora_form = SeguradoraForm()

    cotacoes = Cotacao.query.filter(Cotacao.trello_card_id.isnot(None)).all()

    context = {
        'form_financiado': preco_form_financiado,
        'form_quitado': preco_form_quitado,
        'form_seguradora': seguradora_form,
        'cotacoes': cotacoes
    }

    form_type = request.form.get('form_type')
    cotacao_id = request.form.get('cotacao_id')

    if request.method == 'POST':
        cotacao = Cotacao.query.get(cotacao_id) if cotacao_id else None
        seguradora = request.form.get('seguradora')
        if form_type == 'financiado' and preco_form_financiado.validate_on_submit():
            dados = processar_preco_financiado(preco_form_financiado, seguradora_form=seguradora_form)
            image_path = imagem.financiado(**dados, seguradora=seguradora)
        elif form_type == 'quitado' and preco_form_quitado.validate_on_submit():
            dados = processar_preco_quitado(preco_form_quitado, seguradora_form=seguradora_form)
            image_path = imagem.quitado(**dados, seguradora=seguradora)
        else:
            flash('Preencha corretamente o formulário.', 'warning')
            return render_template('preco.html', **context)

        if cotacao:
            sucesso = anexar_imagem_a_cotacao(trello, cotacao, image_path)
            if sucesso:
                flash('Imagem anexada ao Trello com sucesso!', 'success')
            else:
                flash('Falha ao anexar imagem ao Trello.', 'danger')
        else:
            flash('Imagem gerada, mas nenhum card do Trello foi selecionado. Imagem não anexada.', 'warning')
        return redirect(url_for('colocarPreco.colocarPreco'))

    return render_template('preco.html', **context)