import numpy as np
import math
from multiprocessing import Pool

def getDivisors(n):
	domain = []
	for i in xrange(1, int(math.sqrt(n))):
		if n % i == 0:
			domain.append((i, n/i));
	return domain;




if __name__ == "__main__":
	domain = getDivisors(71328803586048)
	print len(domain)
