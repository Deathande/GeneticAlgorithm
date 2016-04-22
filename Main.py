import GeneticAlgorithm
from math import floor
from Binary import Binary
from random import random
import matplotlib.pyplot as plt

def generate(size):
	population = list()
	for val in range(size):
		randPaul = floor(random() * 31)
		population.append(Binary(randPaul))
	return population

def h(x):
	return x ** 2

def sort(l):
	for i in range(len(l)):
		for j in range(len(l) - i -1):
			if h(l[j].toInt()) < h(l[j+1].toInt()):
				temp = l[j]
				l[j] = l[j+1]
				l[j+1] = temp
	return l

if __name__ == '__main__':
	population = generate(10)
	tops = list()
	m = population[0]
	for i in range(20):
		population = sort(population)
		print("Iteration " + str(i))
		for item in population:
			print(item)
		print()
		tops.append(population[0].toInt())
		if h(m.toInt()) < h(population[0].toInt()):
			m = population[0]
		population = GeneticAlgorithm.mixMutate(population)
		for i in range(len(population)):
			population[i] = Binary(population[i])
	print(m)
	plt.plot(tops)
	plt.show()
