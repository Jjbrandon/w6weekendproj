from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

### IMPORT FORMS HERE ONCE WE HAVE THEM

from app.models import Post

# create instance of blueprint
post = Blueprint('post', __name__, template_folder='post_templates')

from app.models import db

@post.route('/feed')
def feedHome():
    posts = Post.query.all()
    return render_template('feed.html', posts = posts)