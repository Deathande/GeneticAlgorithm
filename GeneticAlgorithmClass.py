import abc
import matplotlib.pyplot as plt
from random import random
from math import floor
from BubbleSort import sort

"""
My goal is to make the genetic algorithm as general
as possible. This way problems that can be solved
with a genetic algorithm can come to this class and
have a basis already developed. Any new problem to be
solved will have to have it's own fitness function
overridden as well as it's own crossing function.
"""

class GeneticAlgorithm(object):
	def __init__(self, population, iterations=10):
		self.population = population
		self.iterations = iterations
	
	def f(x):
		return x.toInt() ** 2

	def applyFitness(self):
		self.population = sort(self.population, f)

	def mix(self):
		newlist = list()
		olength = len(self.population)
		for i in range(floor(len(l) / 2)):
			index = floor(random() * olength)
			l1 = self.population.pop(index)
			index = floor(random() * olength)
			l2 = self.population.pop(index)
			newlist.extend(self.cross(l1, l2))

	def run(self):
		for i in range(self.iterations):
			self.applyFitness()

if __name__ == '__main__':
	pass
