from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, URL, Optional


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    

class SignInForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class EditForm(FlaskForm):
    """Form for editing a user."""

    image = StringField("Image", validators=[Optional(), URL()])
    bio = TextAreaField("Bio", validators=[Optional(), Length(max=50)])


class DeleteForm(FlaskForm):
    """Delete form -- this form is intentionally blank."""


class SearchForm(FlaskForm):
    """Form for searching songs"""
    lyrics = StringField("lyrics", validators=[InputRequired()], render_kw={'autofocus': True})
    genre = SelectField("genre", choices=[("", "SELECT GENRE"), ("rap", "Rap"), ("pop", "Pop"), ("r-b", "R&B"), ("rock", "Rock"), ("country", "Country"), ("all", "Uncertain")], validators=[InputRequired()])
    year = SelectField("year", choices=[("", "SELECT YEAR RANGE"), ("2010-2024", "2010-present"), ("2000-2009", "00's"), ("1990-1999", "90's"), ("1980-1989", "80's"), ("1970-1979", "70's"), ("1960-1969", "60's"), ("All", "Uncertain")], validators=[InputRequired()])