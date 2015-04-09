from bottle import Bottle, get, post, request, run # or route

my_app = Bottle()

@my_app.get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" /> 
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@my_app.post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p style= \"color: #f00\">Login failed.</p>"

def check_login(usr,pwd):
    return usr == "andrea" and pwd == "morettin"
    
run(my_app, host='localhost', port=8080)
