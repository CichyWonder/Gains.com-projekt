from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class SignUpForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired(), Length(max=64)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired(), Length(min=8)])
    captcha = RecaptchaField()
    submit = SubmitField('Potwierdź')


class LogInForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember = BooleanField('Zapamiętaj')
    submit = SubmitField('Potwierdź')