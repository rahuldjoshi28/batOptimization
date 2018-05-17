import random
import sys
import math, copy
import csv
import numpy as np

import matplotlib.pyplot as plt

class Bat:
	def __init__(self, D, A, r, F_min, F_max, X_min, X_max, fun, constrains):
		self.D = D	# Dimensions
		self.N_gen = 1 # Generation number
		self.X_min = X_min
		self.X_max = X_max
		self.X = []
		for i in range(self.D):
			rnd = random.random()
			self.X += [self.X_min + (self.X_max - self.X_min) * rnd]
		self.X = np.array(self.X)
		#[X_min + (X_max - X_min)*random.random() for i in range(D) ] #X velocity
		self.A = A
		self.r = r	#something
		self.F_min = F_min
		self.F_max = F_max
		self.F = self.F_min + (self.F_max - self.F_min) * random.uniform(0, 1)		#Frequency
		#self.sol = sys.maxsize	#maximum size of int
		self.V = [0]*D	#Velocity
		self.V = np.array(self.V)
		self.fun = fun
		self.constrains = constrains
		self.sol = self.fun(self.D, self.X)
	def getArray(self):
		li = [a for a in self.X]
		li += [self.sol]
		return li
	
	def __str__(self):
		s = ""
		for k in self.X:
			s += " "+str(k)
		s += "  ans = "+str(self.sol)		
		return s
	
	def updateFrequency(self, rand_num):
		self.F = self.F_min + rand_num * (self.F_max - self.F_min)	# Beta should be random vector from uniform distribution
	
	def adjust_range(self):
		#while self.constrains(self.D , self.X) == False:
		# 	 self.randomize_position()
		while True:
			for i in range(self.D):
				if self.X[i] > self.X_max:
					self.X[i] = self.X_max
				if self.X[i] < self.X_min:
					self.X[i] = self.X_min
			if not self.constrains(self.D, self.X):
				self.randomize_position()
			else:
				break
		self.sol = self.fun(self.D, self.X)
			#self.randomize_position()
	def randomize_position(self):
		for i in range(0, self.D):
			self.X[i] = self.X_min + (self.X_max - self.X_min)*random.random()

	def updateVelocity(self, b):
		self.V = np.add(self.V, np.subtract(b.X, self.X) * self.F)
		"""
		for i in range(self.D):
			self.V[i] = self.V[i] + (b.X[i] - self.X[i])*self.F
		"""

	def move(self):
		self.X = np.add(self.X, self.V)
		"""
		for i in range(self.D):
			#self.V[i] = self.V[i] + (b.X[i] - self.X[i])*self.F
			print(self.X[i], " + ", self.V[i], end=" ")
			self.X[i] = self.X[i] + self.V[i]
			print(" = ", self.X[i])
		"""
		self.adjust_range()
		
	def jump(self, b):	# I guess lavy flight
		for i in range(self.D):
			self.X[i] = b.X[i] + 0.3 * random.gauss(0, 1)
		self.adjust_range()
		
	def next_generation(self):
		self.N_gen += 1
	
	def changeA(self, a):
		self.A = self.A * a
	
	def changeR(self, g):
		self.r = self.r * (1 - math.exp(-g))
	
	def getCopy(self):
		return copy.deepcopy(self)


class BatAlgorithm:
	def __init__(self, D, NP, N_gen, A_min, A_max, F_min, F_max, X_min, X_max, fitness_fun, constrains):
		self.D = D	#Dimention
		self.NP = NP	#Population
		self.N_gen = N_gen	# Number of generations
		self.A_min = A_min	#min loudness
		self.A_max = A_max	#max Loudness
		
		self.F_min = F_min	#min frequency
		self.F_max = F_max	#max frequency
		self.fitness_fun = fitness_fun	#fitness function

		self.X_min = X_min	#min X
		self.X_max = X_max	#max X
		
		self.alpha = 0.95
		self.gamma = 0.05
		
		self.constrains = constrains

		#self.Fitness = [0.0]*NP
		self.bats = []
		
		for i in range(NP):
			b = Bat(D, A_min + (A_max - A_min)*random.random(), random.random(), F_min, F_max, X_min, X_max, fitness_fun, constrains)
			b.sol = self.fitness_fun(self.D, b.X)
			self.bats += [b]

		self.best_bat = self.get_best_bat()

	def get_best_bat(self):
		i = 0
		for j in range(0, self.NP):
			if(self.bats[i].sol > self.bats[j].sol):
				i = j
		return self.bats[i]

	def move_bats(self):
		const_sol = self.best_bat.sol
		counter = 0
		with open("batalgo.csv","w") as batfile:
			for b in  self.bats:
				b.sol = b.fun(b.D, b.X)

			"""
			plt.axis([self.X_min , self.X_max, 0, 26])
			x = np.arange(self.X_min, self.X_max, 0.1)
			y = x**2
			"""
			writer=csv.writer(batfile)
			#for t in range(1, self.N_gen + 1):
			t = 0
			while True:
				t += 1
				cnt = 1
				x_graph, y_graph = [], []
				
				for index, bat in enumerate(self.bats):
						rnd_num = random.uniform(0, 1)	# Returns number in [0.0, 1.0)
						self.bats[index].updateFrequency(rnd_num)
						self.bats[index].updateVelocity(self.best_bat)
						tmp_bat = self.bats[index].getCopy()

						tmp_bat.move()

						tmp_bat.sol = self.fitness_fun(tmp_bat.D, tmp_bat.X)

						rnd_num = random.random()	# Returns number in [0.0, 1.0]

						if rnd_num > self.bats[index].r:
							tmp_best_bat = self.get_best_bat()
							tmp_bat.jump(tmp_best_bat)
							#break
						
						tmp_bat.sol = self.fitness_fun(self.D, tmp_bat.X)
						
						rnd_num = random.random()
						print(self.bats[index].X, self.bats[index].sol)
						if rnd_num < tmp_bat.A and tmp_bat.sol < self.bats[index].sol:	#my change
							#print("prev = ", bat.X, end = " ")
							self.bats[index] = tmp_bat.getCopy()	#Accept bat
							self.bats[index].changeA(self.alpha)
							self.bats[index].changeR(self.gamma*t)
							#flag = 1
						if self.bats[index].sol < self.best_bat.sol:
							#print("Bat sol = ", bat.sol)
							self.best_bat = bat.getCopy()
							#flag = 1
						# if flag:
						# 	break
						
						cnt += 1
					
						y_graph += [self.bats[index].sol]
						x_graph += [self.bats[index].X[0]]
				if const_sol == self.best_bat.sol:
					counter += 1
				else:
					const_sol= self.best_bat.sol
					counter = 0
				if counter > 500	:
					print("Breaked")
					break
				"""
				plt.clf()
				plt.scatter(np.array(x_graph), np.array(y_graph))
				plt.plot(x, y, 'C1')
				
				plt.pause(0.5)
				"""
				#plt.show()
				writer.writerow(self.best_bat.getArray())
				#print("Yoo ", self.best_bat)
		print("\n\nGenerations: ", self.N_gen)
		print("Position: ", self.best_bat.X)
		print("Minimized value = ", self.best_bat.sol)
		return self.best_bat.X