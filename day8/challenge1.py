import sys

def calculate_total(the_output):
    unique_lengths = [2,3,4,7]
    total = 0
    for string in the_output:
        if len(string) in unique_lengths:
            total += 1
    return total



if __name__ == "__main__":
    the_input = []
    the_solution = 0 
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            line = line.strip()
            the_input, the_output = line.split(" | ")
            the_input = the_input.split(" ") 
            the_output = the_output.split(" ")
            the_total = calculate_total(the_output)
            the_solution += the_total
    print(f"The solution is {the_solution}")
            