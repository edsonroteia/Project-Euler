import numpy as np
import math
from multiprocessing import Pool
import sys

def getDivisors(n):
	domain = []
	for i in xrange(1, int(math.sqrt(n))):
		if n % i == 0:
			domain.append((i, n/i));
	return domain;

def isPerfectSquare(n):
	sr = math.sqrt(n)
	if (sr - int(sr)):
		return False
	else:
		return True

''' in development
def P(f, r):
	if f == r == 1:
		return 1;
	for floor in xrange(1,f):
		if floor
			
	return n
'''

if __name__ == "__main__":
	domain = getDivisors(71328803586048)
	floors = [(1,1)]
	person = 2;
	sum = 0;
	concluded = 0;
	while 1:
		for idx in xrange(0,len(floors)):
			if isPerfectSquare(person + floors[idx][1]):
				tempRoom = (floors[idx][0] + 1, person)
				floors[idx] = tempRoom
				for test in domain:
					if test[0]-1 == idx and test[1] == floors[idx][0]:
						sum += person % 100000000;
						concluded += 1;
						print concluded;
				break
		else:
			floors.append((1, person))
		person += 1;
		if concluded == 183:
			break


