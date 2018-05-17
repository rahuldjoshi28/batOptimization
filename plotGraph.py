import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import math

def sphere():
	X = np.arange(-5.12, 5.12, 1)
	Y = np.arange(-5.12, 5.12, 1)
	X, Y = np.meshgrid(X, Y)
	Z = np.add(X**2, Y**2)
	ax.set_zlim(0, 100.01)
	return X, Y, Z

def ackeleys():
	X = np.arange(-40, 40, 0.1)
	Y = np.arange(-40, 40, 0.1)
	X, Y = np.meshgrid(X, Y)
	A = X**2 + Y**2
	B = np.cos(Y * 2*math.pi) + np.cos(X * 2*math.pi)
	ax.set_zlim(0, 25.01)
	return X, Y, -20 * np.exp(-0.2 * np.sqrt(0.5 * A)) - np.exp(0.5 * B) + (math.e + 20)

def eggholder():
	X = np.arange(-512, 512, 2)
	Y = np.arange(-512, 512, 2)
	X, Y = np.meshgrid(X, Y)
	ax.set_zlim(-1000, 1000.01)
	Z = -(Y + 47)*np.sin(np.sqrt(np.fabs(X/2 + (Y + 47)))) - X*np.sin(np.sqrt(np.fabs(X-(Y+47))))
	return X, Y, Z

def holder_table_function():
	X = np.arange(-10, 10, 1)
	Y = np.arange(-10, 10, 1)
	X, Y = np.meshgrid(X, Y)
	ax.set_zlim(-25, 0)
	Z = -np.fabs( np.multiply(np.multiply(np.sin(X) , np.cos(Y)), np.exp( np.fabs(1 - (np.sqrt( X**2 + Y**2 ) / math.pi)) ) ))
	return X, Y, Z

def myPlot(fun_name):
	fig = plt.figure()
	global ax
	ax = fig.gca(projection = '3d')
	if fun_name == "sphere":
		X, Y, Z = sphere()
	elif fun_name == "holder_table_function":
		X, Y, Z = holder_table_function()
	elif fun_name == "eggholder":
		X, Y, Z = eggholder()
	elif fun_name == "ackeleys":
		X, Y, Z = ackeleys()

	surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
	plt.axis('off')
	ax.zaxis.set_major_locator(LinearLocator(5))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

	fig.colorbar(surf, aspect=50)

	plt.show()
while True:
	print("Menu\n1. Sphere Function\n3. holder_table_function\n4. egg holder function\n5. ackeleys\n6. Exit\nOpt... ")
	opt = int(input())
	if opt == 6:
		exit(0)
	if opt == 1:
		#if dim == 2:
		myPlot("sphere")
	elif opt == 2:
		myPlot("grienwank")
	elif opt == 3:
		myPlot("holder_table_function")
	elif opt == 4:
		myPlot("eggholder")
	elif opt == 5:
		myPlot("ackeleys")