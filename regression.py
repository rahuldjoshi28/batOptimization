from bat import BatAlgorithm

def cost_function(parameters, sol):
	

def regression(parameters, cost_function, X_min = -10, X_max = 10):
	Algorithm = BatAlgorithm(parameters, 500, 20, 0.5, 0.5, 0.0, 2.0, X_min, X_max, cost_function, lambda: True)
	return Algorithm.move_bats()