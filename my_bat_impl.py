import random
from bat import BatAlgorithm
import math

def sphere(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val

#ackeleys
#range -40 to 40
#expected output 0
def ackeleys(D, sol):
	a1 = 0
	a2 = 0
	for i in range(D):
		a1 += sol[i]*sol[i]
		a2 += math.cos(sol[i] * math.pi * 2)
	z = -20 * math.exp(-0.2 * math.sqrt(0.5 * a1)) - math.exp(0.5 * a2) + math.e + 20
	return z

def gear_train(D, sol):
	return math.pow((1/6.931 - (sol[0] * sol[1]) / (sol[2] * sol[3])), 2)
# For reproducive results

def three_bar_truss(D, sol):
	ans =  (2 * math.sqrt(2 * sol[0]) + sol[1]) * 100 # l = 100
	#print(ans)
	return ans

def constraints(D, sol):
	return True
	#return g1(D, sol) and g2(D, sol) and g3(D, sol)

def g1(D, sol):
	return 2 * (math.sqrt(2) * sol[0] + sol[1])/(math.sqrt(2) * sol[0] * sol[0] + 2 * sol[0] * sol[1]) - 2 <= 0

def g2(D, sol):
	return 2 * (sol[1])/(math.sqrt(2) * sol[0] * sol[0] + 2 * sol[0] * sol[1]) - 2 <= 0

def g3(D, sol):
	return 2/(math.sqrt(2) * sol[1] + sol[0] ) - 2 <= 0

#eggholder function
# range -512 to 512
#expected output -959.64
def eggholder(D, sol):
	x = sol[0]
	y = sol[1]
	a = -(y + 47) * math.sin(math.sqrt(abs(x/2 + y+47))) - x * math.sin(math.sqrt(abs(x - (y + 47))))
	return a

#grienwank
#range -50 to 50
#expected output 0
def grienwank(D, sol):
	a1 = 0
	a2 = 1
	for i in range(1, D+1):
		a1 += sol[i - 1] * sol[i - 1]
		a2 *= math.cos(1.0 * sol[i - 1] / math.sqrt(i))
	return a1/4000 - a2 + 1


#holder table function
# -10 to  10
#expected output = -19.20
def holder_table_function(D, sol):
	x = sol[0]
	y = sol[1]
	return - abs( math.sin(x) * math.cos(y) *math.exp( abs(1 - (math.sqrt( x*x + y*y ) / math.pi)) ) )

#schaffer function
# range -100 100
#expected output 0 
def schaffer(D, sol):
	x = sol[0]
	y = sol[1]
	return 0.5 + (math.pow(math.cos(math.sin(abs(x*x - y*y))), 2) - 0.5)/math.pow((1 + 0.001 * (x*x + y*y)), 2)
import numpy as np
X = np.arange(1, 1000, 2)
Y = X*2
X2 = np.square(X)
X3 = np.multiply(X, X2)
def cost_function(D, sol):
	err = 0.0
	m1 = sol[0]
	m2 = sol[1]
	m3 = sol[2]
	b = sol[3]
	for i in range(len(X)):
		err += (m1*X[i] + m2*X2[i] + m3*X3[i] + b - Y[i])**2
	return err

print("Menu\n1. Sphere Function\n2. grienwank\n3. holder_table_function\n4. schaffer\n5. Ackeleys\n6. Exit\nOpt... ")
opt = int(input())
if opt == 7:
	exit(0)
if opt == 1:
	print("Enter dimentions (Graph available for 2D): ")
	dim = int(input())
	#if dim == 2:
	#	plot.myPlot("sphere")
	print("Actual minimum value = 0")
	Algorithm = BatAlgorithm(D = dim, NP = 50, N_gen = 50*dim, A_min = 0.5,A_max = 0.5,F_min = 0.0,F_max = 2.0,X_min = -5.12, X_max = 5.12, fitness_fun = sphere, constrains = constraints)
	Algorithm.move_bats()	
elif opt == 2:
	print("Actual minimum value = 0")
	#plot.myPlot("grienwank")
	Algorithm = BatAlgorithm(2, 10, 500, 0.5, 0.5, 0.0, 2.0, -50, 50, grienwank, constraints)
	Algorithm.move_bats()
elif opt == 3:
	print("Actual minimum value = -19.20")
	#plot.myPlot("holder_table_function")
	Algorithm = BatAlgorithm(2, 20, 600, 0.5, 0.5, 0.0, 2.0, -10, 10, holder_table_function, constraints)
	Algorithm.move_bats()
elif opt == 4:
	print("Actual minimum value = 0")
	#plot.myPlot("schaffer")
	Algorithm = BatAlgorithm(2, 500, 20, 0.5, 0.5, 0.0, 2.0, -100, 100, schaffer, constraints)
	Algorithm.move_bats()
elif opt == 5:
	Algorithm = BatAlgorithm(2, 5, 20, 0.5, 0.5, 0.0, 2.0, -40, 40, ackeleys, constraints)
	Algorithm.move_bats()
elif opt == 6:
	print("Actual minimum value = 0")
	#plot.myPlot("ackeleys")
	Algorithm = BatAlgorithm(4, 500, 200, 0.5, 0.5, 0.0, 2.0, -5, 5, cost_function, constraints)
	Algorithm.move_bats()
