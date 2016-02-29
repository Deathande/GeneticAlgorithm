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

def mutate(l, num):
	new = list()
	for i in range(num):
		print('mutate:')
		index = floor(random() * len(l))
		member = l[index]
		index = floor(random() * len(member))
		print(member)
		if member[index] == 1:
			member[index] = 0
		else:
			member[index] = 1
		print(member)
		new.append(member)
	return new

def mixPopulation(l):
	newlist = list()
	olength = len(l)
	for i in range(floor(len(l) / 2)):
		index = floor(random() * len(l))
		l1 = l.pop(index)
		index = floor(random() * len(l))
		l2 = l.pop(index)
		newlist.extend(cross(l1.bs, l2.bs))
	newlist.extend(mutate(newlist, olength - len(newlist)))	
	for i in range(len(newlist)):
		newlist[i] = Binary(newlist[i])
	return newlist

def cross(l1, l2):
	if len(l1) == len(l2):
		pivot = floor(len(l1) * .40)
		ltemp1 = l1[pivot:len(l1)]
		ltemp2 = l2[pivot:len(l2)]
		l1 = l1[0:pivot]
		l2 = l2[0:pivot]
		l1.extend(ltemp2)
		l2.extend(ltemp1)
	return [l1, l2]

def run(times):
	pop = generate(5)
	print("original population")
	for val in pop:
		sys.stdout.write(str(val.toInt()) + ": k")
		val.out()

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
	pop = mixPopulation(pop)
	for val in pop:
		val.out()
