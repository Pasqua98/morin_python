class A(object):
    def __init__(self):
        self.a = 11
        print "crea A"
    def mtd(self):
        print "mtd A"
        

class B(A):
    def __init__(self):
        super(B,self).__init__()
        print "crea B"
    def mtd(self):
        print "mtd B"

class C(A):
    def __init__(self):
        super(C,self).__init__()
        print "crea C"
    def mtd(self):
        print "mtd C"

        
class D(B,C):
    def __init__(self):
        super(D,self).__init__()
        print "crea D"
        


