from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.cotacao_db import Cotacao
from app.forms.cotacao_form import CotacaoForm
from app import db

editar_bp = Blueprint('editar', __name__)

@editar_bp.route('/editarCotacao/<int:cotacao_id>', methods=['GET', 'POST'])
def editarCotacao(cotacao_id):
    cotacao = Cotacao.query.get_or_404(cotacao_id)
    form = CotacaoForm(obj=cotacao)

    if form.validate_on_submit():
        form.populate_obj(cotacao)
        db.session.commit()
        flash('Cotação atualizada com sucesso!', 'success')
        return redirect(url_for('cotacao.cotacao'))

    return render_template('editar.html', form=form, cotacao=cotacao)