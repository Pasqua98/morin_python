import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# funzioni di aiuto per le liste

def max(l):
    m = l[0]
    for i in range(1,len(l)):
        if l[i] > m:
            m = l[i]
    return m

def swap(l, i, j):
	l[i], l[j] = l[j], l[i]
    
# colora la coppia il cui primo elemento si trova in posizione i 
	
def print_color(l, i, color):
	# colora gli elementi al posto i e i + 1
	if color == "y": # yellow
		bc = "\033[0;33m"
		ec = "\033[0m"
	elif color == "g": # green
		bc = "\033[0;32m"
		ec = "\033[0m"
	elif color == "r": # red
		bc = "\033[0;31m"
		ec = "\033[0m"
	elif color == "b": # blue
		bc = "\033[0;34m"
		ec = "\033[0m"
	elif color == "g": # cyan
		bc = "\033[0;36m"
		ec = "\033[0m"
	else:
		bc = ""
		ec = ""
	s = "["
	for j in range(0, i):
		s += str(l[j]) + ", "
	s += bc + str(l[i]) + ec + ", " + bc + str(l[i+1]) + ec
	if i+1 < len(l)-1:
		for j in range(i + 2, len(l)):
			s += ", " + str(l[j])  
	s += "]"
	print s
	
def bubblesort(l):
	# ciclo esterno: esegue il ciclo interno per len(l) - 1 volte, i: ultimo elemento
	for i in range(len(l), 1, -1):
		#ciclo interno: porta il max alla fine
		for j in range(1, i):
			if(l[j-1] > l[j]):
				swap(l, j-1, j)
				print "scambio: " + str(l)
			else:
				print "non scambio: " + str(l)
		print "posizionato il massimo: " + str(l) 
				 
def bubblesort_color(l):
	# ciclo esterno: esegue il ciclo interno per len(l) - 1 volte, i: ultimo elemento
	for i in range(len(l), 1, -1):
		#ciclo interno: porta il max alla fine
		for j in range(1, i):
			if(l[j-1] > l[j]):
				swap(l, j-1, j)
				print_color(l, j-1, "y")
			else:
				print_color(l, j-1, "g")
				
# mergesort viene  proposto nella versione riscorsiva

def mergesort(l):
    if len(l) < 2:
        logger.info("\tnon fondo nulla " )
        return l
    result = []
    mid = len(l)/2
    h1 = mergesort(l[:mid])
    h2 = mergesort(l[mid:])
    logger.info("\t" + str(h1) + " *** " + str(h2))
    i = 0
    j = 0
    logger.info("\tfusione")
    while i < len(h1) and j < len(h2):
            if h1[i] > h2[j]:
                result.append(h2[j])
                j += 1
            else:
                result.append(h1[i])
                i += 1
    # terminata una delle due liste ...
    result += h1[i:]
    result += h2[j:]
    return result
