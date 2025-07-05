from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField


class PrecoForm_quitado(FlaskForm):
    nome = StringField('Nome')
    entrada_basico = StringField('Entrada', validators=[DataRequired()])
    mensal_basico = StringField('Mensal', validators=[DataRequired()])
    valor_total_basico = StringField('Valor Total', validators=[DataRequired()])
    entrada_completo = StringField('Entrada Completo', validators=[DataRequired()])
    mensal_completo = StringField('Mensal Completo', validators=[DataRequired()])
    valor_total_completo = StringField('Valor Total Completo', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class PrecoForm_financiado(FlaskForm):
    nome = StringField('Nome')
    entrada_completo = StringField('Entrada Completo', validators=[DataRequired()])
    mensal_completo = StringField('Mensal Completo', validators=[DataRequired()])
    valor_total_completo = StringField('Valor Total Completo', validators=[DataRequired()])
    submit = SubmitField('Enviar')

