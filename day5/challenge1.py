import sys
import numpy as np

def getCoords(diff, start, finish):
    #Get Non zero coordinate
    non_zero = np.where(diff != 0)
    coords = [start]
    if len(non_zero[0] == 1):
        non_zero_value = np.abs(diff[non_zero][0])
        diff = diff / non_zero_value
        diff = diff.astype(np.int32)
        while not np.array_equal(start, finish):
            start = start + diff
            coords.append(start)
    coords = np.array(coords)
    return coords

def solution(board, lines):
    for line in lines:
        start = np.array(line[0])
        end = np.array(line[1])
        diff = end - start
        zeros = np.where(diff == 0)
        if len(zeros[0]) != 0:
            coords = getCoords(diff, start, end)
            for coord in coords:
                x = coord[0]
                y = coord[1]
                board[x,y] += 1
    over_two_indexes = np.where(board >= 2)
    return len(over_two_indexes[0])
        
if __name__ == "__main__":
    board_coords = []
    lines = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            before_after = line.split(" -> ")
            before = [int(num) for num in before_after[0].split(",")]
            after = [int(num) for num in before_after[1].split(",")]
            lines.append([before, after])
            board_coords += before
            board_coords += after
    board_size = max(board_coords)
    board = np.zeros((board_size + 1, board_size + 1))
    the_solution = solution(board, lines)
    print(f"The solution is {the_solution}")