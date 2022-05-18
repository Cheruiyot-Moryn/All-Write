from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,SubmitField)
from wtforms.validators import InputRequired

class BlogForm(FlaskForm):
    title = StringField("Blog title:", validators=[InputRequired()])
    blog = TextAreaField("Type:", validators=[InputRequired()])
    submit = SubmitField("Post")

class UpdateBlogForm(FlaskForm):
    title = StringField("Blog title", validators=[InputRequired()])
    blog = TextAreaField("Type", validators=[InputRequired()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[InputRequired()])
    nicname= StringField("Comment Alias")
    submit = SubmitField("Comment")

class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Biography")
    email = StringField("Email")    
    submit = SubmitField("Update")