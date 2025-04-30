from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField

class CotacaoForm(FlaskForm):
    genero = SelectField('Gênero', choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')])
    nome = StringField('Nome Completo')
    documento = StringField('Driver License')
    endereco = StringField('Endereço')
    financiado = SelectField('Financiado', choices=[('Financiado', 'Sim'), ('Quitado', 'Não')])
    tempo_de_seguro = SelectField('Tempo de Seguro', choices=[('nunca_teve', 'Nunca Teve'), ('menos_1_ano', 'Menos de 1 ano'), ('1_3_anos', 'Entre 1 e 3 anos'), ('3+_anos', 'Mais de 3 anos')])
    vin = StringField('VIN')
    data_nascimento = StringField('Data de Nascimento')
    tempo_com_veiculo = SelectField('Tempo com Veículo', choices=[('menos_1_ano', 'Menos de 1 ano'), ('1_3_anos', 'Entre 1 e 3 anos'), ('mais_5_anos', '5 Anos ou mais')])
    tempo_no_endereco = SelectField('Tempo no Endereço', choices=[('menos_1_ano', 'Menos de 1 ano'), ('mais_1_ano', 'Mais de 1 Ano')])
    submit = SubmitField('Enviar')