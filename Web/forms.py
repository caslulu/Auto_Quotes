from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField

class CotacaoForm(FlaskForm):
    genero = SelectField('Gênero', choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')])
    nome = StringField('Nome Completo')
    documento = StringField('Driver License')
    endereco = StringField('Endereço')
    financiado = SelectField('Financiado', choices=[('Financiado', 'Sim'), ('Quitado', 'Não')])
    tempo_de_seguro = SelectField('Tempo de Seguro', choices=[('Nunca Teve', 'Nunca Teve'), ('Menos de 1 ano', 'Menos de 1 ano'), ('1-3 Anos', 'Entre 1 e 3 anos'), ('3+ anos', 'Mais de 3 anos')])
    vin = StringField('VIN')
    data_nascimento = StringField('Data de Nascimento')
    tempo_com_veiculo = SelectField('Tempo com Veículo', choices=[('Menos de 1 ano', 'Menos de 1 ano'), ('1-3 Anos', 'Entre 1 e 3 anos'), ('Mais de 5 Anos', '5 Anos ou mais')])
    tempo_no_endereco = SelectField('Tempo no Endereço', choices=[('Menos de 1 Ano', 'Menos de 1 ano'), ('Mais de 1 Ano', 'Mais de 1 Ano')])
    colocar_trello = BooleanField('Colocar Trello')
    submit = SubmitField('Enviar')