msg = ""
n = int(raw_input("inserisci un numero "))
if n%2 == 0:
    msg = "il numero e' pari"
else:
    msg = "il numero dispari"
if n%3 == 0:
    msg = msg + ", e' divisibile per 3"
if n%7 == 0:
    msg = msg + ", e' divisibile per 7"
print msg
     
