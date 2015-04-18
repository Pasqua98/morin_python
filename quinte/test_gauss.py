from numpy import *
from gauss import gauss
import sys


n = input("inserire la dimensione della matrice: ")

# A = array([[0.0 for i in range(0,a)] for j in range(0,a)])
A = zeros((n,n))
# b = array([0 for i in range(0,a)])
b = zeros(n)


print("inserire i coefficienti procedendo riga per riga: ")
for i in range(0,n):
    for j in range(0,n):
        a = input("inserire coefficiente in posizione (" + str(i) + "," + str(j) + ") ")
        A[i,j] = a

print("inserire i termini noti: ")
for k in range(0,n):
    b = input("inserire termine in posozione:" + str(k) + " ")
    B[k] = b
    
# test del determinante

if linalg.det(A) == 0:
    print "la matrice ha determinante nullo"
    sys.exit(1)
else:
    x = gauss(A,b)
    print x

        
            
