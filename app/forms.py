from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class UploadForm (FlaskForm):
    description = TextAreaField("Enter Description Here",validators=[DataRequired()])
    photo = FileField("Upload Image Here", validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'],'Images Only!')
    ])