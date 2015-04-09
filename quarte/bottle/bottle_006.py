from bottle import Bottle, run
from bottle.ext import sqlite

my_app = Bottle()
plugin = sqlite.Plugin(dbfile='test.sqlite')
my_app.install(plugin)

@my_app.route('/show/<name>')
def show(name, db):
    row = db.execute('SELECT * FROM tab01 WHERE name=?', (name,)).fetchone()
    if row:
        print row
        return tostr(row)
    else:
        return "non trovato"
    
@my_app.route('/showall')
def showall(db):
    rows = db.execute('SELECT * FROM tab01').fetchall()
    s = ''
    if rows:
        print rows
        for row in rows:
            s += tostr(row) + '<br />'
        return s
    else:
        return "non trovato"

def tostr(t):
    s = ""
    for e in t:
        s += str(e) + " "
    return s
    
run(my_app, host='localhost', port=8080)
