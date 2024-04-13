from typing import Optional
from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.minimum = min
        self.maximum = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        data = field.data
        if len(str(data)) > 0 and data is not None and self.minimum <= data <= self.maximum:
            return
        if self.message is not None:
            message = self.message
        else:
            message = field.gettext("Число должно быть между %(minimum)s and %(maximum)s.")
        raise ValidationError(message % dict(min=self.minimum, max=self.maximum))
