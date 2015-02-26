n = int(raw_input("inserisci un numero "))
if n%2 == 0:
    if n%4 == 0:
        print "e' divisibile per 2 e per 4"
    else:
        print "e' divisibile per 2"
else:
    print "il numero e' dispari"
