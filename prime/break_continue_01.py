# break_continue_01.py

# il programma da' 5 tentativi per disegnare la piramide
# di altezza non negativa

for i in range(5):
	n = int(raw_input("inserisci un intero non negativo: "))
	if n <= 0:
		print "riprova"
		if i == 4:
			print "non hai piu' tentativi"
		else:
			print "hai " + str(4-i) + " tentativi"
		# procedo coi tentativi nel caso ve ne siano
		continue
	else:
		for j in range(1,n+1):
			print (n-j)*" " + (2*j-1)*"*"
		# non devo procedere coi tentativi: ho disegnato la piramide
		break
