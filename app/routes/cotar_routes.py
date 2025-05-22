from flask import Blueprint, render_template, redirect, url_for, request
from app.models.cotacao_db import Cotacao
from app.services.cotacao_service import processar_cotacao
from app.services.progressive_service import Progressive
from app.services.geico_services import Geico
from app.services.allstate_services import Allstate
from playwright.sync_api import sync_playwright
import os

cotar_bp = Blueprint('cotar', __name__)

@cotar_bp.route('/cotar/<cotacao_id>', methods=['POST'])
def cotar(cotacao_id):
    try:
        cotacao = Cotacao.query.get_or_404(cotacao_id)
        seguradora = request.form.get('seguradora')
        if cotacao:
            executar_cotacao(cotacao, seguradora=seguradora)
            return "Cotação processada com sucesso!"
        else:
            return redirect(url_for('cotacao.cotacao'))
    except Exception as e:
        print(f"Erro ao processar cotação: {e}")
        return render_template('erro.html', mensagem="Erro ao processar cotação")


def executar_cotacao(cotacao, seguradora):
    dados = processar_cotacao(cotacao)
    email = f"{dados['first_name'].lower()}.{dados['last_name'].lower()}@outlook.com"
    if seguradora == "Progressive":
        p = Progressive()
    elif seguradora == "Geico":
        p = Geico()
    else:
        p = Allstate()
    with sync_playwright() as playwright:
        p.cotacao(playwright, email=email, **dados)