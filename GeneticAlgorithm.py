import BubbleSort # I don't care bout efficiency right now
from Binary import Binary
from random import random
from math import floor

def generate(size):
	population = list()
	for val in range(size):
		randPaul = floor(random() * 31)
		population.append(Binary(randPaul))
	return population
def f(x):
	return x.toInt()**2

def sort(l):
	l = BubbleSort.sort(l, f)
	return l

if __name__ == '__main__':
	pop = generate(5)
	print('Sample:')
	for val in pop:
		print(val.toInt())
		val.out()
	print('--------------------------')
	pop = sort(pop)
	for val in pop:
		val.out()
	

