# gauss.py
""" 
il modulo gauss contiene la funzione gauss: 
restituisce il vettore soluzioni di un sistema lineare 
Ax = b, ove det(A) != 0
"""

def gauss(A,b):
    n = len(b)
    # soluzione tutta a 0
    x = array([0]*n)
    # triangolarizzazione
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k] != 0:
                lam = A[i,k]/A[k,k]
                A[i,k+1:n] = A[i,k+1:n]-lam*A[k,k+1:n]
                b[i] = b[i]-lam*b[k]
    # sostituzione    
    for k in range(n-1,-1,-1):
        x[k]=(b[k]-dot(A[k,k+1:n],b[k+1:n]))/A[k,k]
    return x
