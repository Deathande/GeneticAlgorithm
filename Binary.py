from math import floor
import sys

class Binary:
	def __init__(self, number, l=4):
		if isinstance(number, list):
			self.bs = number
			self.isBinary(self.bs)
		elif isinstance(number, int):
			self.bs = list()
			while number > 0:
				self.bs.append(number % 2)
				number = floor(number / 2)
			for i in range(l - len(self.bs)+ 1):
				self.bs.append(0)
			self.bs.reverse()
		else:
			raise Exception ("Bad Type")
	
	def __str__(self):
		s = ""
		for val in self.bs:
			s += str(val) + " "
		return s
	
	def __len__(self):
		return len(self.bs)

	def toInt(self):
		s = len(self.bs)
		val = 0
		for i in self.bs:
			s -= 1
			val += i * 2 ** s
		return val

	def isBinary(self, val):
		for i in val:
			if i != 0 and i != 1:
				print("bad value")
				exit(1)
	
	def out(self):
		for val in self.bs:
			sys.stdout.write(str(val) + " ")
		sys.stdout.write('\n')
	

if __name__ == '__main__':
	b = Binary(16)
	print(b.out())
