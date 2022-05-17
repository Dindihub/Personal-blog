from flask import render_template,request,redirect,url_for,abort,flash
from . import main
import requests
from .forms import PostForm
from ..models import User,Post
from .. import db

from flask_login import login_required,current_user

@main.route('/')
def index():
    quotes=requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    get_quotes=quotes.json()

    return render_template('main/index.html',get_quotes=get_quotes)


@main.route('/quotes',methods=['GET','POST'])
def json_url():
    return render_template('main/quotes.html')


@main.route('/posts',methods=['GET','POST'])
@login_required
def posts():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data,
                user_id=current_user.id)

        db.session.add(post)
        db.session.commit()

        flash('Thanks for your post!')
        return redirect(url_for('main.blog'))
    return render_template('main/posts.html',title = 'post',form = form)
    
@main.route('/blog',methods=['GET','POST'])
def blog():
    return render_template('main/blog.html')  