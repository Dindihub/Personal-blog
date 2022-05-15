from flask import render_template,request,redirect,url_for,abort,flash
from . import main
import requests
# from .forms import 
# from ..models import User
# from .. import db,photos

# from flask_login import login_required,current_user

@main.route('/')
def index():
    quotes=requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    get_quotes=quotes.json()

    return render_template('main/index.html',get_quotes=get_quotes)


@main.route('/quotes',methods=['GET','POST'])
def json_url():
    return render_template('main/quotes.html')