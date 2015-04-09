from bottle import Bottle, run, template

my_app = Bottle()

# in tal modo uso la sintassi per riferirsi al namespace di un modulo

@my_app.route('/what/<user>/<action>')
def doing(user,action):
    s = "<b> What is {{user}} doing? </b>"
    s += "<br />"
    s += "{{user}} is {{action}}"
    return template(s, user = user, action = action)

run(my_app, host='localhost', port=8080)
