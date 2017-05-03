import numpy as np
import math
from multiprocessing import Pool

def teste(maxNo):
	for i in xrange(0, maxNo):
		print "vai quebrar", i

if __name__ == "__main__":
	listN = []
	maxNo = long(math.pow(2,50));
	listN.append(maxNo)
	pool = Pool()
	pool.map(teste, listN)
