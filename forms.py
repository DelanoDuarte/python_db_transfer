from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MigrationForm(FlaskForm):
    # Source Connection
    sourceHost = StringField('sourceHost', validators=[DataRequired()])
    sourcePort = StringField('sourcePort', validators=[DataRequired()])
    sourceUsername = StringField('sourceUsername', validators=[DataRequired()])
    sourcePass = StringField('sourcePass', validators=[DataRequired()])
    sourcedb = StringField('sourcedb', validators=[DataRequired()])
    
    # Target Connection
    targetHost = StringField('targetHost', validators=[DataRequired()])
    targetPort = StringField('targetPort', validators=[DataRequired()])
    targetUsername = StringField('targetUsername', validators=[DataRequired()])
    targetPass = StringField('targetPass', validators=[DataRequired()])
    targetdb = StringField('targetdb', validators=[DataRequired()])