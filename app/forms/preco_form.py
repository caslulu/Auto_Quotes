from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, RadioField


class PrecoForm_quitado(FlaskForm):
    seguradora = RadioField('Seguradora', choices=[('Progressive', 'Progressive'), ('Geico', 'Geico'), ('Allstate', 'Allstate')])
    nome = StringField('Nome')
    entrada_basico = StringField('Entrada')
    mensal_basico = StringField('Mensal')
    valor_total_basico = StringField('Valor Total')

    entrada_completo = StringField('Entrada Completo')
    mensal_completo = StringField('Mensal Completo')
    valor_total_completo = StringField('Valor Total Completo')

    submit = SubmitField('Enviar')

class PrecoForm_financiado(FlaskForm):
    seguradora = RadioField('Seguradora', choices=[('Progressive', 'Progressive'), ('Geico', 'Geico'), ('Allstate', 'Allstate')])
    nome = StringField('Nome')

    entrada_completo = StringField('Entrada Completo')
    mensal_completo = StringField('Mensal Completo')
    valor_total_completo = StringField('Valor Total Completo')

    submit = SubmitField('Enviar')

