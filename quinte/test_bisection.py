import sys
from bisection import bisection

def parab(x):
    return x*x-2
    
# la funzione bisection puo' generare un'eccezione

try:
    print bisection(parab, 0.5, 1.5)
except:
    sys.exit(1)
