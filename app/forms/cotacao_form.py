from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, RadioField
from wtforms.validators import DataRequired

class CotacaoForm(FlaskForm):
    genero = RadioField('Gênero', choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], validators=[DataRequired()])
    nome = StringField('Nome Completo', validators=[DataRequired()])
    documento = StringField('Driver License', validators=[DataRequired()])
    endereco = StringField('Endereço', validators=[DataRequired()])
    financiado = SelectField('Estado do Veiculo', choices=[('Financiado', 'Financiado'), ('Quitado', 'Quitado')], validators=[DataRequired()])
    tempo_de_seguro = SelectField('Tempo de Seguro', choices=[('Nunca Teve', 'Nunca Teve'), ('Menos de 1 ano', 'Menos de 1 ano'), ('1-3 Anos', 'Entre 1 e 3 anos'), ('3+ anos', 'Mais de 3 anos')], validators=[DataRequired()])
    vin = StringField('VIN', validators=[DataRequired()])
    data_nascimento = StringField('Data de Nascimento', validators=[DataRequired()])
    tempo_com_veiculo = SelectField('Tempo com Veículo', choices=[('Menos de 1 ano', 'Menos de 1 ano'), ('1-3 Anos', 'Entre 1 e 3 anos'), ('Mais de 5 Anos', '5 Anos ou mais')], validators=[DataRequired()])
    tempo_no_endereco = SelectField('Tempo no Endereço', choices=[('Menos de 1 Ano', 'Menos de 1 ano'), ('Mais de 1 Ano', 'Mais de 1 Ano')], validators=[DataRequired()])
    colocar_trello = BooleanField('Colocar Trello')
    submit = SubmitField('Enviar')


class SeguradoraForm(FlaskForm):
    seguradora = RadioField('Seguradora', choices=[('Progressive', 'Progressive'), ('Geico', 'Geico'), ('Allstate', 'Allstate')])