from bottle import Bottle, run, template

my_app = Bottle()

# in tal modo uso la sintassi per riferirsi al namespace di un modulo

@my_app.route('/hello')
def hello(name='Hello'):
    return template('hello_world', name=name)

run(my_app, host='localhost', port=8080)
