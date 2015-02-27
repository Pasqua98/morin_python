n = int(raw_input("inserisci un numero "))
if n <= 0:
    exit
for i in range(1, n+1):
    print (n-i)*" " + (2*i-1)*"*"
