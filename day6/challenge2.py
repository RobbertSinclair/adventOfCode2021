import sys
import numpy as np

#Better solution. Much faster


def solution(fish_states, days):
    day = 1
    num_of_fish = sum(fish_states)
    while day <= days:
        fish0 = fish_states.pop(0)
        fish_states[6] += fish0
        fish_states.append(fish0)
        print(f"Day {day}: {fish_states}")
        day += 1
    return sum(fish_states)



if __name__ == '__main__':
    fish_states = [0 for i in range(9)]
    with open(sys.argv[1]) as f:
        line = f.read()
        line = line.strip()
        line = line.split(",")
        for num in line:
            the_num = int(num)
            fish_states[the_num] += 1
    print(fish_states)
    the_solution = solution(fish_states, int(sys.argv[2]))
    print(f"The solution is {the_solution}")