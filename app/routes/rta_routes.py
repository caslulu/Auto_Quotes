from flask import Blueprint, render_template, send_file
from app.forms.rta_form import RTAForm
from app.services.rta_service import RTAService

rta_bp = Blueprint('rta', __name__)
rta_service = RTAService()

@rta_bp.route('/rta', methods=['GET', 'POST'])
def rta():
    form = RTAForm()
    if form.validate_on_submit():
        pdf_io = rta_service.preencher_rta(form)
        return send_file(
            pdf_io,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='rta_preenchido.pdf'
        )
    return render_template('rta.html', form=form)
