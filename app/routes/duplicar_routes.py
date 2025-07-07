from flask import Blueprint, render_template, redirect, url_for
from app.models.cotacao_db import Cotacao
from app.services.cotacao_service import CotacaoService
from app.extensions import db

duplicar_bp = Blueprint('duplicar', __name__)
cotacao_service = CotacaoService()

@duplicar_bp.route('/duplicar/<int:cotacao_id>', methods=['POST'])
def duplicarCotacao(cotacao_id):
    cotacao = Cotacao.query.get(cotacao_id)
    if not cotacao:
        return redirect(url_for('index'))

    nova_cotacao = cotacao_service.duplicar_cotacao(cotacao)

    db.session.add(nova_cotacao)
    db.session.commit()

    return redirect(url_for('cotacao.cotacao'))