from flask_wtf import FlaskForm
from wtforms import TextAreaField, FileField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import InputRequired

class UploadForm (FlaskForm):
    description = TextAreaField("Enter Description Here",validators=[InputRequired()])
    photo = FileField("Upload Image Here", validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'],'Images Only!')
    ])