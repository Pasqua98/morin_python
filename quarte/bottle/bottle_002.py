from bottle import Bottle, run

my_app = Bottle()

# in tal modo uso la sintassi per riferirsi al namespace di un modulo

@my_app.route('/hello')
def hello():
    return "Hello World!"

run(my_app, host='localhost', port=8080)
