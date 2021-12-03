import sys
import numpy as np

def solution(the_input):
    return oxygen_generator_rating(the_input) * co2_generator_rating(the_input)

def oxygen_generator_rating(the_input):
    new_array = np.copy(the_input)
    num_of_rows, num_of_columns = np.shape(new_array)
    i = 0
    while i < num_of_columns and num_of_rows > 1:
        the_column = new_array[:,i]
        counts = ((the_column == 0).sum(), (the_column == 1).sum())
        if counts[0] == counts[1]:
            max_value = 1
        else:
            max_value = counts.index(max(counts))
        new_array_indexes = (the_column == max_value)
        new_array = new_array[new_array_indexes,:]
        num_of_rows, num_of_columns = np.shape(new_array)
        i += 1
    
    binary_string = "".join([str(i) for i in new_array[0,:]])
    return int(binary_string, base=2)

def co2_generator_rating(the_input):
    new_array = np.copy(the_input)
    num_of_rows, num_of_columns = np.shape(new_array)
    i = 0
    while i < num_of_columns and num_of_rows > 1:
        the_column = new_array[:,i]
        counts = ((the_column == 0).sum(), (the_column == 1).sum())
        if counts[0] == counts[1]:
            max_value = 0
        else:
            max_value = counts.index(min(counts))
        new_array_indexes = (the_column == max_value)
        new_array = new_array[new_array_indexes,:]
        num_of_rows, num_of_columns = np.shape(new_array)
        i += 1
    
    binary_string = "".join([str(i) for i in new_array[0,:]])
    return int(binary_string, base=2)


if __name__ == "__main__":
    the_input = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            line = [int(i) for i in line]
            the_input.append(line)
    the_input = np.array(the_input)
    the_solution = solution(the_input)
    print(f"Solution {the_solution}")