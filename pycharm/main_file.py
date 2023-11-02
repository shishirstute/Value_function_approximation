# importing modules
import numpy as np
import matplotlib.pyplot as plt
import copy
from projection_module import projection
from function_modules import demand_sample_plotter
from function_modules import value_calc_using_slope
from function_modules import *
# for reproducibility
np.random.seed(1)
# Parameters initialization
# number of iterations
num_iterations = 10000;
B = 10000 # some big number for extreme slope
# for demand
demand_size = 1000
mean_value = 7
sigma = 2

q = 2 # selling price 6 2 100
c = 1 # cost price   4 1 75

# Generate  Demand Samples
#normal
#demand_sample = np.random.normal(mean_value,sigma,demand_size) # normal distribution
#demand_sample = np.round(demand_sample).astype(int)
# poisson
demand_sample = np.random.poisson(mean_value,demand_size)  # poisson distribution

# probable decision space 0 to 20
M = np.max(demand_sample) # decision limit
decision_space = list(range(0,M+1))


# Plotting demand samples
demand_sample_plotter(demand_sample, demand_size, mean_value)
######################################################################
# Learning starts
######################################################################
# initializing slope vector V
# Size of V will be equal to probable decision space size
# assigning 0 value initially
V = {}
for x in decision_space:
    V[x]=0

# initializing B and -B as slope for left extreme and right extreme end
V[-1] = B
V[M+1] = -B
Z = copy.copy(V)
# iterations starts for learning

for k in range(num_iterations):
    s = np.random.choice(decision_space)
    d = np.random.choice(demand_sample)
    # calculate slope as
    if s <= d:
        eta = q-c
    else:
        eta = -c
    alpha = 20/(40+k) # from powell's paper
    # update Z vector
    for x in decision_space:
        # update slope at sample decision point only
        if x == s:
            Z[x] = (1-alpha)*V[x] + alpha*eta
        else:
            Z[x] = V[x]
    V = projection(Z,V,s,M,B)
# calculating approximated value
f_approx = value_calc_using_slope(V, decision_space)
# calculating exact expected value
f_exact = expected_value_calc_exact(decision_space, demand_sample, q, c)
# plotting approximated value
#approximated_function_plotter(f_approx)
# plotting exact functional value
#exact_function_plotter(f_exact)
# plotting both exact and approximated function
both_functional_plotter(f_approx, f_exact)
plt.show()

