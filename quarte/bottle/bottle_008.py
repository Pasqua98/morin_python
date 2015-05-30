from bottle import Bottle, template, HTTPError, run
from bottle.ext import sqlite
from bottle import static_file
from bottle import redirect

my_app = Bottle()

@my_app.route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root="img/")
    
@my_app.route('/link')
def link():
    redirect("http://www.google.it")
    
    
run(my_app, host='localhost', port=8080)
