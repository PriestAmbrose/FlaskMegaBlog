from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Priest Ambrose'}
    return '''
<html>
    <head>
        <title> Home Page - Flask Mega Blog </title>
    </head>
    <body>
        <h1> Hello, ''' + user['username'] + '''!<h1>
    </body>
</html>'''
