"""
General quick sort algorithm for any
python list

Algorithm:
	1. Pick an element to be the pivot
	2. Reorder so that all values less
	than the pivot come before it.
	3. recursion
"""

# bit of a silly function, but it is
# the default argument for the sort so
# that a custom function can be applied
def __f(x):
	return x

def sort(l, f=__f):
	if len(l) > 1:
		pivot = l.pop()
		wall = 0
		for i in range(len(l)):
			if l[i] > pivot:
				temp = l[wall]
				l[wall] = l[i]
				l[i] = temp
				wall += 1
		l.insert(wall, pivot)
		l1 = l[0:wall]
		l2 = l[wall+1:len(l)]
		l[0:wall] = sort(l1, f)
		l[wall+1:len(l)] = sort(l2, f)
	return l

if __name__ == '__main__':
	from random import random
	from math import floor
	l = list()
	for i in range(1000):
		l.append(floor(random() * 10))
	print(l)
	print(sort(l))
