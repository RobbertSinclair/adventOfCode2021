import sys
import numpy as np

def calculate_fueling(fuelings):
    the_fueling = 0
    for fuel in fuelings:
        the_fueling += int(1/2 * fuel * (fuel + 1))
    return the_fueling

def solution(positions):
    min_value = None
    min_position = 0
    num_of_positions = np.max(positions)
    for i in range(num_of_positions):
        fuelings = np.abs(positions - i)
        fuel_requirements = calculate_fueling(fuelings)
        if min_value is None or min_value > fuel_requirements:
            min_position = i
            min_value = fuel_requirements
    return (min_position, min_value)

if __name__ == '__main__':
    positions = []
    with open(sys.argv[1], "r") as f:
        line = f.read()
        line = line.strip()
        line = line.split(",")
        positions = np.array([int(num) for num in line])
    the_solution = solution(positions)
    print(f"Min Position is {the_solution[0]}\nMin Value: {the_solution[1]}")