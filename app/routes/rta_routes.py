from flask import Blueprint, render_template, request, send_file, flash
from app.forms.rta_form import RTAForm
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import io

rta_bp = Blueprint('rta', __name__)

def preencher_rta(form):
    # Carrega o template do RTA (imagem do formulário vazio)
    template_path = 'app/static/rta_template.png'  # Ajuste o caminho conforme necessário
    image = Image.open(template_path).convert('RGB')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 16)  # Ajuste a fonte conforme necessário

    # Coordenadas ajustadas para o campo B4 (Colors)
    color_radios = {
        'Black': (155, 265),
        'White': (205, 265),
        'Brown': (255, 265),
        'Blue': (305, 265),
        'Yellow': (355, 265),
        'Gray': (405, 265),
        'Purple': (455, 265),
        'Green': (505, 265),
        'Orange': (555, 265),
        'Red': (605, 265),
        'Silver': (655, 265),
        'Gold': (705, 265),
    }
    # Marca o radio da cor selecionada
    cor = form.color.data
    if cor in color_radios:
        x, y = color_radios[cor]
        draw.ellipse((x-8, y-8, x+8, y+8), fill='black')

    # Preenche os campos principais (ajuste as coordenadas conforme o template)
    draw.text((120, 90), form.vin.data, fill='black', font=font)
    draw.text((120, 150), str(form.miles.data), fill='black', font=font)
    draw.text((120, 180), form.purchase_date.data.strftime('%m/%d/%Y'), fill='black', font=font)
    draw.text((120, 210), form.model.data, fill='black', font=font)
    draw.text((120, 240), str(form.year.data), fill='black', font=font)
    draw.text((120, 270), form.make.data, fill='black', font=font)
    draw.text((120, 300), str(form.cylinders.data), fill='black', font=font)
    draw.text((120, 330), str(form.doors.data), fill='black', font=font)
    draw.text((120, 360), str(form.passengers.data), fill='black', font=font)
    draw.text((120, 390), str(form.odometer.data), fill='black', font=font)
    draw.text((120, 420), form.owner_name.data, fill='black', font=font)
    draw.text((120, 450), form.owner_birth.data.strftime('%m/%d/%Y'), fill='black', font=font)
    draw.text((120, 480), form.owner_document.data, fill='black', font=font)
    draw.text((120, 510), form.owner_address.data, fill='black', font=font)
    # Data efetiva do seguro: sempre hoje
    draw.text((120, 540), datetime.now().strftime('%m/%d/%Y'), fill='black', font=font)
    # Garaging address = mailing address
    draw.text((120, 570), form.owner_address.data, fill='black', font=font)

    # Salva em memória
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@rta_bp.route('/rta', methods=['GET', 'POST'])
def rta():
    form = RTAForm()
    if form.validate_on_submit():
        img_io = preencher_rta(form)
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='rta_preenchido.png')
    return render_template('rta.html', form=form)
