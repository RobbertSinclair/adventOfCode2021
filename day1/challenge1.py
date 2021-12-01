import sys

def solution(the_list):
    count = 0
    prev = the_list[0]
    for i in range(1, len(the_list)):
        current = the_list[i]
        difference = prev - current
        if difference < 0:
            count += 1
        prev = current
    return count

if __name__ == '__main__':
    depths = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            line = int(line)
            depths.append(line)
    count = solution(depths)
    print(f"The result is {count}")
