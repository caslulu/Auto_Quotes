from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired

class RTAForm(FlaskForm):
    # --- Owner 1 Information ---
    owner_name = StringField(
        "(First Owner's) Name (Last, First, Middle)", validators=[DataRequired()]
    )
    owner_dob = DateField(
        '(Owner 1) Date of Birth', format='%Y-%m-%d', validators=[DataRequired()]
    )
    owner_license = StringField(
        '(Owner 1) License Number/ID/SSN', validators=[DataRequired()]
    )
    owner_residential_address = StringField(
        '(Owner 1) Residential Address (Rua, Apt, Cidade, Estado, CEP)', validators=[DataRequired()]
    )
    owner_license_issued_state = StringField(
        '(Owner 1) State/Country of License/ID'
    )
    owner_same_as_residential = StringField(
        '(Owner 1) Same as residential'
    )


    # --- Sale Info ---
    gross_sale_price = StringField('Gross Sale Price (Proof Required)')
    purchase_date = DateField('Purchase Date', format='%Y-%m-%d')

    # --- Insurance Info ---
    insurance_effective_date = DateField('Effective Date of Insurance', format='%Y-%m-%d')
    insurance_policy_change_date = DateField('Policy Change Date', format='%Y-%m-%d')

    # --- Seller Info ---
    seller_name = StringField('Seller Name (Please print)')
    seller_address = StringField('Seller Address (Rua, Cidade, Estado, CEP)')

    # --- Veículo ---
    vin = StringField('VIN', validators=[DataRequired()])
    body_style = StringField('Body Style', validators=[DataRequired()])
    color = SelectField(
        'Cor',
        choices=[
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
        ],
        validators=[DataRequired()]
    )
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
