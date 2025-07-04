from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.cotacao_db import Cotacao
from app.models.cotacao_preco_ml import CotacaoPrecoML
from app.forms.preco_form import PrecoForm_quitado, PrecoForm_financiado
from app.forms.seguradora_form import SeguradoraForm
from app.services.trello_service import Trello
from app.services.Canva_Banner.preco_automatico import PrecoAutomatico
from app.services.cotacao_service import CotacaoService
from sqlalchemy.orm.exc import NoResultFound

colocarPreco_bp = Blueprint('colocarPreco', __name__)
cotacao_service = CotacaoService()

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
        taxa_cotacao = request.form.get('taxa_cotacao')
        apenas_prever = bool(request.form.get('apenas_prever'))
        if form_type == 'financiado' and preco_form_financiado.validate_on_submit():
            dados = cotacao_service.processar_preco_financiado(preco_form_financiado, taxa=taxa_cotacao)
            image_path = imagem.financiado(**dados, seguradora=seguradora)
            preco_basico = None
            preco_full = float(dados.get('valor_total_completo', '0').replace(',', '').replace('R$', ''))
            tipo_veiculo = 'financiado'
        elif form_type == 'quitado' and preco_form_quitado.validate_on_submit():
            dados = cotacao_service.processar_preco_quitado(preco_form_quitado, taxa=taxa_cotacao)
            image_path = imagem.quitado(**dados, seguradora=seguradora)
            preco_basico = float(dados.get('valor_total_basico', '0').replace(',', '').replace('R$', ''))
            preco_full = float(dados.get('valor_total_completo', '0').replace(',', '').replace('R$', ''))
            tipo_veiculo = 'quitado'
        else:
            flash('Preencha corretamente o formulário.', 'warning')
            return render_template('preco.html', **context)

        if not apenas_prever and cotacao:
            sucesso = anexar_imagem_a_cotacao(trello, cotacao, image_path)
            if sucesso:
                flash('Imagem anexada ao Trello com sucesso!', 'success')
            else:
                flash('Falha ao anexar imagem ao Trello.', 'danger')
            # Salva no banco de dados ML
            cot_ml = CotacaoPrecoML(
                genero=cotacao.genero,
                nome=cotacao.nome,
                documento=cotacao.documento,
                endereco=cotacao.endereco,
                tempo_de_seguro=cotacao.tempo_de_seguro,
                data_nascimento=cotacao.data_nascimento,
                tempo_no_endereco=cotacao.tempo_no_endereco,
                estado_civil=cotacao.estado_civil,
                nome_conjuge=cotacao.nome_conjuge,
                data_nascimento_conjuge=cotacao.data_nascimento_conjuge,
                documento_conjuge=cotacao.documento_conjuge,
                vehicles_json=cotacao.vehicles_json,
                pessoas_json=cotacao.pessoas_json,
                trello_card_id=cotacao.trello_card_id,
                preco_basico=preco_basico,
                preco_full=preco_full,
                tipo_veiculo=tipo_veiculo
            )
            from app.extensions import db
            db.session.add(cot_ml)
            db.session.commit()
        elif apenas_prever:
            # Apenas previsão: salva imagem no disco, mas não salva no banco nem anexa ao Trello
            flash('Cotação prevista (ML). Imagem gerada e salva, mas não foi salva no banco nem anexada ao Trello.', 'info')
        else:
            flash('Imagem gerada, mas nenhum card do Trello foi selecionado. Imagem não anexada.', 'warning')
        return redirect(url_for('colocarPreco.colocarPreco'))

    return render_template('preco.html', **context)