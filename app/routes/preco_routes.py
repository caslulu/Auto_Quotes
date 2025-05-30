from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.cotacao_db import Cotacao
from app.models.cotacao_preco_ml import CotacaoPrecoML
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
        if cotacao:
            # Salva/atualiza registro no novo banco ML ao preencher preço
            dados_cotacao = {
                'genero': cotacao.genero,
                'nome': cotacao.nome,
                'documento': cotacao.documento,
                'endereco': cotacao.endereco,
                'tempo_de_seguro': cotacao.tempo_de_seguro,
                'data_nascimento': cotacao.data_nascimento,
                'tempo_no_endereco': cotacao.tempo_no_endereco,
                'estado_civil': cotacao.estado_civil,
                'nome_conjuge': cotacao.nome_conjuge,
                'data_nascimento_conjuge': cotacao.data_nascimento_conjuge,
                'documento_conjuge': cotacao.documento_conjuge,
                'veiculos': cotacao.vehicles_json,
                'pessoas': getattr(cotacao, 'pessoas_json', '[]')
            }
        if form_type == 'financiado' and preco_form_financiado.validate_on_submit():
            dados = processar_preco_financiado(preco_form_financiado, seguradora_form=seguradora_form)
            seguradora = request.form.get('seguradora')
            usar_previsao = request.form.get('usar_previsao') == 'on'
            if usar_previsao:
                from ml.predict_endpoint import model as ml_model
                import json as _json
                # Monta dados para ML (ajuste conforme seu pipeline)
                ml_input = dict(dados_cotacao)
                ml_input['veiculos'] = _json.loads(ml_input['veiculos']) if isinstance(ml_input['veiculos'], str) else ml_input['veiculos']
                ml_input['pessoas'] = _json.loads(ml_input['pessoas']) if isinstance(ml_input['pessoas'], str) else ml_input['pessoas']
                ml_input['num_veiculos'] = len(ml_input.get('veiculos', []))
                ml_input['num_pessoas'] = len(ml_input.get('pessoas', []))
                for k in ['veiculos', 'pessoas', 'nome', 'documento', 'data_nascimento', 'nome_conjuge', 'data_nascimento_conjuge', 'documento_conjuge']:
                    ml_input.pop(k, None)
                import pandas as pd
                preco_previsto = ml_model.predict(pd.DataFrame([ml_input]))[0]
                preco_previsto_final = 400 + preco_previsto * 1.2  # taxa + 20% margem
                # Adiciona na imagem (exemplo: campo mensal_completo)
                dados['mensal_completo'] = f"R$ {preco_previsto_final:,.2f} (previsto)"
            image_path = imagem.financiado(**dados, seguradora=seguradora)
            if cotacao:
                sucesso = anexar_imagem_a_cotacao(trello, cotacao, image_path)
                if sucesso:
                    flash('Imagem anexada ao Trello com sucesso!', 'success')
                else:
                    flash('Falha ao anexar imagem ao Trello.', 'danger')
            else:
                flash('Imagem gerada, mas nenhum card do Trello foi selecionado. Imagem não anexada.', 'warning')
            return redirect(url_for('colocarPreco.colocarPreco'))

        elif form_type == 'quitado' and preco_form_quitado.validate_on_submit():
            seguradora = request.form.get('seguradora')
            dados = processar_preco_quitado(preco_form_quitado, seguradora_form=seguradora_form)
            usar_previsao = request.form.get('usar_previsao') == 'on'
            if usar_previsao:
                from ml.predict_endpoint import model as ml_model
                import json as _json
                ml_input = dict(dados_cotacao)
                ml_input['veiculos'] = _json.loads(ml_input['veiculos']) if isinstance(ml_input['veiculos'], str) else ml_input['veiculos']
                ml_input['pessoas'] = _json.loads(ml_input['pessoas']) if isinstance(ml_input['pessoas'], str) else ml_input['pessoas']
                ml_input['num_veiculos'] = len(ml_input.get('veiculos', []))
                ml_input['num_pessoas'] = len(ml_input.get('pessoas', []))
                for k in ['veiculos', 'pessoas', 'nome', 'documento', 'data_nascimento', 'nome_conjuge', 'data_nascimento_conjuge', 'documento_conjuge']:
                    ml_input.pop(k, None)
                import pandas as pd
                preco_previsto = ml_model.predict(pd.DataFrame([ml_input]))[0]
                preco_previsto_final = 400 + preco_previsto * 1.2  # taxa + 20% margem
                dados['mensal_basico'] = f"R$ {preco_previsto_final:,.2f} (previsto)"
            image_path = imagem.quitado(**dados, seguradora=seguradora)
            if cotacao:
                sucesso = anexar_imagem_a_cotacao(trello, cotacao, image_path)
                if sucesso:
                    flash('Imagem anexada ao Trello com sucesso!', 'success')
                else:
                    flash('Falha ao anexar imagem ao Trello.', 'danger')
            else:
                flash('Imagem gerada, mas nenhum card do Trello foi selecionado. Imagem não anexada.', 'warning')
            return redirect(url_for('colocarPreco.colocarPreco'))
        else:
            flash('Preencha corretamente o formulário.', 'warning')

    return render_template('preco.html', **context)