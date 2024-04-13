from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email #, NumberRange
from app2 import NumberLength

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired('Поле не должно быть пустым'), Email()])
    #phone = IntegerField(validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)])
    phone = IntegerField(validators=[InputRequired('вы не ввели номер телефона'), NumberLength(min=1000000000, max=9999999999, message=None)])
    name = StringField(validators=[InputRequired('Поле не должно быть пустым')])
    address = StringField(validators=[InputRequired('Поле не должно быть пустым')])
    index = IntegerField(validators=[InputRequired('Поле не должно быть пустым')])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        phone = form.phone.data
        name = form.name.data

        return f"Успешная регистрация пользователя: {name}, email: {email} с телефоном +7{phone} "

    return f"Неверный ввод, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)