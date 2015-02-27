class A(object):
    def __init__(self):
        self.a = 11
        print "crea A"

class B(A):
    def __init__(self):
        super(B,self).__init__()
        self.b = 12
        print "crea B"
        
class C(object):
    def __init__(self):
        self.c = 13
        print "crea C"

class D(C,B):
    def __init__(self):
        super(D, self).__init__()
        super(B, self).__init__()
        self.d = 12
        print "crea D"
        


