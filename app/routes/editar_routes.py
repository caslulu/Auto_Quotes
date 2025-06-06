from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.cotacao_db import Cotacao
from app.forms.cotacao_form import CotacaoForm
from app import db
import json

editar_bp = Blueprint('editar', __name__)

@editar_bp.route('/editarCotacao/<int:cotacao_id>', methods=['GET', 'POST'])
def editarCotacao(cotacao_id):
    cotacao = Cotacao.query.get_or_404(cotacao_id)
    # Carrega dados de veículos e pessoas
    veiculos = []
    if cotacao.vehicles_json:
        try:
            data = json.loads(cotacao.vehicles_json)
            if isinstance(data, list):
                veiculos = data
            elif isinstance(data, dict):
                veiculos = data.get('veiculos', [])
        except Exception:
            veiculos = []
    pessoas = []
    if hasattr(cotacao, 'pessoas_json') and cotacao.pessoas_json:
        try:
            pessoas = json.loads(cotacao.pessoas_json)
        except Exception:
            pessoas = []
    # Instancia o formulário corretamente
    if request.method == 'POST':
        form = CotacaoForm(request.form)
    else:
        form = CotacaoForm(obj=cotacao, veiculos=veiculos, pessoas=pessoas)

    if form.validate_on_submit():
        # Popula manualmente os campos simples
        cotacao.genero = form.genero.data
        cotacao.nome = form.nome.data
        cotacao.documento = form.documento.data
        cotacao.endereco = form.endereco.data
        cotacao.tempo_de_seguro = form.tempo_de_seguro.data
        cotacao.data_nascimento = form.data_nascimento.data
        cotacao.tempo_no_endereco = form.tempo_no_endereco.data
        cotacao.estado_civil = form.estado_civil.data
        cotacao.nome_conjuge = form.nome_conjuge.data
        cotacao.data_nascimento_conjuge = form.data_nascimento_conjuge.data
        cotacao.documento_conjuge = form.documento_conjuge.data
        # Salva veículos e pessoas como JSON
        veiculos = []
        for v in form.veiculos.entries:
            veiculos.append({
                'vin': v.form.vin.data,
                'tempo_com_veiculo': v.form.tempo_com_veiculo.data,
                'financiado': v.form.financiado.data,
                'placa': v.form.placa.data
            })
        cotacao.vehicles_json = json.dumps(veiculos)
        pessoas = []
        for p in form.pessoas.entries:
            pessoas.append({
                'nome': p.form.nome.data,
                'documento': p.form.documento.data,
                'data_nascimento': p.form.data_nascimento.data,
                'parentesco': p.form.parentesco.data,
                'genero': p.form.genero.data
            })
        cotacao.pessoas_json = json.dumps(pessoas)
        db.session.commit()
        flash('Cotação atualizada com sucesso!', 'success')
        return redirect(url_for('cotacao.cotacao'))

    return render_template('editar.html', form=form, cotacao=cotacao)