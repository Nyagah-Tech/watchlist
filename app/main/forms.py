from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title = StringField('Reveiw title' ,validators = [Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')