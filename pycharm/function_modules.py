import numpy as np
import matplotlib.pyplot as plt



# function calculating exact expected value
def expected_value_calc_exact(decision_space, demand_sample, q, c):
    f_exact = {}
    for decision in decision_space:
        f_exact[decision]=0 # assigning 0 value initially

    for decision in decision_space:
        for demand in demand_sample:
            value = q*np.min([decision,demand]) - c*decision
            f_exact[decision] = np.mean([f_exact[decision],value])

    return f_exact

# function calculating approximated value using slope information
def value_calc_using_slope(V,decision_space):
    # f is approximated value calculated using slopes
    f_approx = {}
    for x in decision_space:
        if x == 0:
            f_approx[x] = 0
        else:
            f_approx[x] = sum(value for key, value in V.items() if 0 <= key < x)
    return f_approx

# Plotting demand samples functions
def demand_sample_plotter(demand_sample, demand_size, mean_value):
    # counts elements from 0 to maximum present in sample
    element_counts = np.bincount(demand_sample)
    # calculating probability
    probabilities = element_counts / demand_size;
    min_element = np.min(demand_sample)
    max_element = np.max(demand_sample)
    # since index starts from 0
    plt.figure(1)
    plt.plot(range(len(probabilities)), probabilities, marker='o', linestyle='-')
    plt.xlim(min_element - 1, max_element + 1)
    plt.xlabel('element')
    plt.ylabel('probability')
    plt.title(f"Poisson Demand Sample Space (mean={mean_value}, demand_sample size={demand_size})")
    #plt.show()
    return None

# plotting approximated function
def approximated_function_plotter(f_approx):
    plt.figure(2)
    plt.plot(f_approx.keys(),f_approx.values())
    plt.xlabel('decision space')
    plt.ylabel('approximated_expected_value')
    plt.title(f'plot of approximated expected function using slope')
    #plt.show()
    return None
# plotting exat function
def exact_function_plotter(f_exact):
    plt.figure(3)
    plt.plot(f_exact.keys(),f_exact.values())
    plt.xlabel('decision space')
    plt.ylabel('true_expected_value')
    plt.title(f'true expected function plot')
    #plt.show()

# Plotting expected value of exact and approximated functions
def both_functional_plotter(f_approx, f_exact):
    plt.figure(4)
    plt.plot(f_approx.keys(), f_approx.values(), label = 'Approximated expected value using slope')
    plt.plot(f_exact.keys(), f_exact.values(), label = 'Exact expected function value')
    plt.legend()
    plt.xlabel('decision space')
    plt.ylabel('expected_value')
    plt.title(f' Exact and approximated expected function plot')
    #plt.show()