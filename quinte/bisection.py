## module bisection
""" root = bisection(f,x1,x2,switch=0,tol=1.0e-9).
Finds a root of f(x) = 0 by bisection.
The root must be bracketed in (x1,x2).
Setting switch = 1 returns root = None if
f(x) increases upon bisection.
"""

from math import log,ceil

def bisection(f,x1,x2,switch=1,tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0: 
        return x1
    f2 = f(x2)
    if f2 == 0.0: 
        return x2
    if f1*f2 > 0.0: 
        raise Exception('bad braketed')
    n = int(ceil(log(abs(x2 - x1)/tol)/log(2.0)))
    # print "in " + str(n) + " steps"
    # rint "[-1]:x1=" +str(x1)
    # print "[-1]:x1=" +str(x2)
    for i in range(n):
        x3 = 0.5*(x1 + x2)
        f3 = f(x3)
        if (switch == 1) and (abs(f3) > abs(f1)) and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0:
            return x3
        if f2*f3 < 0.0:
            x1, f1 = x3, f3
        else:
            x2, f2 = x3, f3
        # print "[" + str(i) + "]:x1=" + str(x1)
        # print "[" + str(i) + "]:x2=" + str(x2)
    return (x1 + x2)/2.0
