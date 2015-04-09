n = int(raw_input("Inserisci un numero intero positivo: "))
fattori = []
if n > 2:
    for i in range(2,n/2):
        r = n%i
        while(r==0):
            fattori.append(i)
            n = n/i
            r = n%i
# nelk caso in cui sia irriducibile o unita' (primo)
if len(fattori) == 0: 
    fattori.append(n)
print fattori

