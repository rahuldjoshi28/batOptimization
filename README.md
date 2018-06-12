# Bat Optimization algorithm in python:
Object oriented python implementation of bat algorithm.

Following are the parameters we need to give to pass to the function.
## Parameters:
- D : dimention of the optimization problem.
- NP: Number of population.
- N_gen: Number of generation i.e. number of iterations.
- A_min: Minimum loudness.
- A_max: Maximum loudness.
- F_min: Minimum frequency.
- F_max: Maximum frequency.
- X_min: Lower bound.
- X_max: Upper bound.
- fitness_fun: Objective function which we have to minimize.
- constrains: Constrains over variables.

## Examples:
```
def sphere_function(D, sol):
    ans = 0.0
    for index in range(D):
        ans += sol[index] * sol[index]
    return ans

def constrins(D, sol):
    #Check constrins
    if (constrins is true):
      return True
    else:
      return False

object = BatAlgorithm(D = dim, NP = 50, N_gen = 50*dim, A_min = 0.5,A_max = 0.5,F_min = 0.0,F_max = 2.0,X_min = -5.12, X_max = 5.12, fitness_fun = sphere_function, constrains = constraints)
print( object.move_bats() )
```
