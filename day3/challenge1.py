import sys
import numpy as np

def solution(the_input):
    #Due to the fact that we are dealing with binary
    gamma = "0b"
    epsilon = "0b"
    the_shape = np.shape(the_input)
    num_of_columns = the_shape[1]
    for i in range(num_of_columns):
        the_column = the_input[:,i]
        counts = ((the_column == 0).sum(), (the_column == 1).sum())
        max_value = counts.index(max(counts))
        if max_value == 0:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    gamma_int = int(gamma, base=2)
    epsilon_int = int(epsilon, base=2)
    power_consumption = gamma_int * epsilon_int
    return power_consumption



if __name__ == "__main__":
    the_input = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            line = [int(i) for i in line]
            the_input.append(line)
    the_input = np.array(the_input)
    the_solution = solution(the_input)
    print(f"Power Consumption is {the_solution}")