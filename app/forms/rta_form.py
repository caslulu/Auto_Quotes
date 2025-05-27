from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired

class RTAForm(FlaskForm):
    vin = StringField('VIN', validators=[DataRequired()])
    color = SelectField('Cor', choices=[
        ('Black', 'Black'),
        ('White', 'White'),
        ('Brown', 'Brown'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
        ('Gray', 'Gray'),
        ('Purple', 'Purple'),
        ('Green', 'Green'),
        ('Orange', 'Orange'),
        ('Red', 'Red'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    ], validators=[DataRequired()])
    miles = IntegerField('Milhas', validators=[DataRequired()])
    purchase_date = DateField('Data de Compra', format='%Y-%m-%d', validators=[DataRequired()])
    model = StringField('Modelo', validators=[DataRequired()])
    year = IntegerField('Ano', validators=[DataRequired()])
    make = StringField('Marca', validators=[DataRequired()])
    cylinders = IntegerField('Cilindros', validators=[DataRequired()])
    doors = IntegerField('Portas', validators=[DataRequired()])
    passengers = IntegerField('Passageiros', validators=[DataRequired()])
    odometer = IntegerField('Odometer', validators=[DataRequired()])
    owner_name = StringField('Nome do Proprietário', validators=[DataRequired()])
    owner_birth = DateField('Data de Nascimento', format='%Y-%m-%d', validators=[DataRequired()])
    owner_document = StringField('Documento do Proprietário', validators=[DataRequired()])
    owner_address = StringField('Endereço do Proprietário', validators=[DataRequired()])
    submit = SubmitField('Gerar RTA')
