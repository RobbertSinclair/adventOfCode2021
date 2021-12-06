import sys
import numpy as np

'''
TERRIBLE SOLUTION
IT'S FINE FOR PART 1 BUT DON'T RUN THIS FOR PART 2
'''


def solution(the_list, days):
    new_fish = np.array([])
    number_of_fish = np.shape(the_list)[0]
    day = 1
    while day < days:
        less_than_seven = np.where(the_list < 7)
        greater_than_seven = np.where(the_list >= 7)
        the_list[less_than_seven] = (the_list[less_than_seven]-1) % 7
        the_list[greater_than_seven] = the_list[greater_than_seven] - 1
        the_list = np.append(the_list, new_fish)
        zero_fish = np.where(the_list == 0)
        new_fish = np.array([8 for i in range(len(zero_fish[0]))])
        number_of_fish += np.shape(new_fish)[0]
        day += 1
        print(f"Day {day}: {number_of_fish} fish")
    return number_of_fish


if __name__ == '__main__':
    the_input = []
    with open(sys.argv[1]) as f:
        line = f.read()
        line = line.strip()
        line = line.split(",")
        the_input = np.array([int(num) for num in line])
    the_solution = solution(the_input, int(sys.argv[2]))
    print(f"The solution is {the_solution}")