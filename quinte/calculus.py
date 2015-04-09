# importiamo il modulo delle frazioini

from fractions import Fraction
fr = Fraction

# prodotto scalare
def dot(u,v):
    d = 0
    for i in range(0, len(u)):
        d += u[i]*v[i]
    return d

# stampa di matrici (allineata)
def printm(A):
    m = len(A)
    n = len(A[0])
    for i in range(0, m):
        s = ""
        for j in range(0, n-1):
            s += str(A[i][j]) + "\t"
        s += str(A[i][n-1])
        print s
