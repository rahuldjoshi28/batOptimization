import random
from bat import BatAlgorithm
import math

class benchmarkfunction:
	def Funone(D, sol):
		val = 0.0
		for i in range(D):
			val = val + (sol[i] * sol[i])
		return val
		
		
	def Funthree(D, sol):
		valj=0.0
		vali=0.0
		for i in range(D):
			for j in range(i):
				valj = valj + (sol[i] * sol[i])
			vali=vali+valj
		return vali
		
	def FunFive(D, sol):
		val=0.0
		for i in range((D-1)):
			val=val+(((100*((sol[i+1]-sol[i])*(sol[i+1]-sol[i])))+((sol[i]-1)*(sol[i]-1))))
		return val
		
		
	def Funsix(D, sol):
		val=0.0
		r = random.uniform(0, 1)
		for i in range(D):
			val=val+(i*(sol[i]*sol[i]*sol[i]*sol[i])+r)
		return val
		
		
	def Funseven(D, sol):
		val=0.0
		for i in range(D):
			val= val+(((sol[i]*sol[i])-10*math.cos(2*3.14*sol[i])+10))
		return val
def constraints(D, sol):
	pass

Algorithm = BatAlgorithm(2, 500, 300, 0.5, 0.5, 0.0, 2.0, -5.12, 5.12, benchmarkfunction.Funone, constraints)
Algorithm.move_bats()