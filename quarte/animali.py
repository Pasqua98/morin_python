class volante(object):
    def __init__(self):
        print "crea un animale volante"
    def vola(self):
        print "vola"

class strisciante(object):
    def __init__(self):
        print "crea un animale strisciante"
    def striscia(self):
        print "striscia"
        
class serpente_volante(volante,strisciante):
    pass

        
