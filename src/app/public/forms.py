from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, Length


class LocationForm(FlaskForm):
    street = StringField('Ulica', validators=[DataRequired(), Length(max=80)])
    house_number = StringField('Numer domu', validators=[DataRequired(), Length(max=10)])
    zip_code = StringField('Kod pocztowy', validators=[DataRequired(), Length(min=5, max=5)])
    phone_number = StringField('Numer telefonu', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Potwierdźr')


class ConfigurationForm(FlaskForm):
    name = StringField('Imię')
    email = StringField('E-mail', validators=[Email()])
    password = PasswordField('hasło')
    submit = SubmitField('Potwierdź')