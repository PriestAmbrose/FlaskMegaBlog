from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Priest Ambrose'}
    posts = [
        {
            'author':{'username':'John'},
            'body':'Beautiful day in Jordanville'
        },
        {
            'author':{'username':'Susan'},
            'body':'The prayers were so good at the monastery!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
