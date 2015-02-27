n = int(raw_input("inserisci un numero "))
for i in range(1, n+1):
    print i
    s = raw_input("vuoi continuare? (batti invio per continuare oppure digota \"no\")\n")
    if s == "No" or s == "no":
        break
    
