from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Priest Ambrose'}
    return render_template('index.html', title='Home', user=user)
