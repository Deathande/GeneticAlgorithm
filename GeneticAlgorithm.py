import matplotlib.pyplot as plt
import BubbleSort # I don't care bout efficiency right now
from Binary import Binary
from random import random
from random import randint
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
		index = floor(random() * len(l))
		member = l[index]
		index = floor(random() * len(member))
		if member[index] == 1:
			member[index] = 0
		else:
			member[index] = 1
		new.append(member)
	return new

def mixMutate(l, pct=.5):
	index = int(len(l) * pct)
	wl = l[0:index]
	print(len(wl))
	nl = list()
	while len(wl) > 1:
		index = randint(0, len(wl)-1)
		v1 = wl.pop(index)
		index = randint(0, len(wl)-1)
		v2 = wl.pop(index)
		nl.extend(cross(v1.bs, v2.bs))
	if len(wl) == 1:
		index = randint(0, len(nl)-1)
		val = nl[index]
		nl.extend(cross(val, wl[0].bs))
	nl.extend(mutate(nl, len(l) - len(nl)))
	return nl

def cross(l1, l2):
	if len(l1) == len(l2):
		pivot = floor(random() * len(l1))
		ltemp1 = l1[pivot:len(l1)]
		ltemp2 = l2[pivot:len(l2)]
		l1 = l1[0:pivot]
		l2 = l2[0:pivot]
		l1.extend(ltemp2)
		l2.extend(ltemp1)
	return [l1, l2]

def run(times):
	pop = generate(5)
	top = list()
	print("original population")
	out(pop)
	print('----------------')
	for i in range(times):
		pop = sort(pop)
		top.append(pop[0].toInt())
		pop = mixPopulation(pop)
		#out(pop)
		#print()
	plt.plot(top)
	pop = sort(pop)
	top.append(pop[0].toInt())
	pop[0].out()
	plt.show()
