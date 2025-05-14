from flask import Blueprint, render_template, redirect, url_for
from app.models.cotacao_db import Cotacao
from app.extensions import db

apagar_bp = Blueprint('apagar', __name__)
@apagar_bp.route('/apagar_cotacao/<cotacao_id>', methods=['POST'])
def apagarCotacao(cotacao_id):
    cotacao = Cotacao.query.get_or_404(cotacao_id)
    db.session.delete(cotacao)
    db.session.commit()
    print(f"Cotação com ID {cotacao_id} removida com sucesso.")
    return redirect(url_for('cotacao.cotacao'))
