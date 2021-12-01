import sys

def solution(the_list):
    prev_sum = 0
    count = 0
    for i in range(0, len(the_list)-3):
        start = i
        end = i + 3
        the_sum = sum(the_list[start:end])
        difference = the_sum - prev_sum
        if difference > 0:
            count += 1
        prev_sum = the_sum
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