from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired

class RTAForm(FlaskForm):
    vin = StringField('VIN', validators=[DataRequired()])
    body_style = StringField('Body Style', validators=[DataRequired()])
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
    year = IntegerField('Ano', validators=[DataRequired()])
    make = StringField('Marca', validators=[DataRequired()])
    model = StringField('Modelo', validators=[DataRequired()])
    odometer = IntegerField('Odometer', validators=[DataRequired()])
    cylinders = IntegerField('Cylinders', validators=[DataRequired()])
    passengers = IntegerField('Passengers', validators=[DataRequired()])
    doors = IntegerField('Doors', validators=[DataRequired()])
    previous_title_number = StringField('Previous Title Number', validators=[DataRequired()])
    previous_title_state = StringField('Previous Title State', validators=[DataRequired()])
    previous_title_country = StringField('Previous Title Country', validators=[DataRequired()])
    submit = SubmitField('Gerar RTA')
