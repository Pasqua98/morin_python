from bottle import Bottle, template, HTTPError, run
from bottle.ext import sqlite

my_app = Bottle()
plugin = sqlite.Plugin(dbfile='test.sqlite')
my_app.install(plugin)

@my_app.route('/show/<nome>')
def show(nome, db):
    row = db.execute('SELECT * FROM tab01 WHERE name=?', (nome,)).fetchone()
    if row:
        print row
        return template('fetchone', row=row)
    return HTTPError(404, "Page not found")
    
@my_app.route('/showall')
def showall(db):
    rows = db.execute('SELECT * FROM tab01').fetchall()
    if rows:
        print rows
        return template('fetchall', rows=rows)
    return HTTPError(404, "Page not found")

def tostr(t):
    s = ""
    for e in t:
        s += str(e) + " "
    return s
    

    
run(my_app, host='localhost', port=8080)
