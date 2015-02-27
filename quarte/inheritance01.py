class A(object):
    a = 11
    def __init__(self):
        print "crea A"
    def mtd(self):
        print "mtd A"
    def sss(self):
        print "mtd A"
    def get_a(self):
        return self.__class__.a

class B(A):
    a = 12
    def __init__(self):
        A.__init__(self)
        print "crea B"
    def mtd(self):
        print "mtd B"
    def get_a(self):
        return self.__class__.a
