import sys

def work_out_numbers(the_input, the_output):
    
    string_digit = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 5,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
    }

    letter_mapping = {

    }
    unique = [2, 3, 4, 7]
    unique_len = {
        2: (1, "cf"),
        3: (7, "acf"),
        4: (4, "bcdf"),
        7: (8, "abcdefg")
    }
    total = 0
    the_lengths = [len(string) for string in the_input]
    while len(letter_mapping.keys()) != 7:
        try:
            unique_number = unique.pop(0)
            unique_tuple = unique_len[unique_number]
            code_string = unique_tuple[1]
            the_string = the_input[the_lengths.index(unique_number)]
            for i in range(unique_number):
                letter_mapping[code_string[i]] = the_string[i]
        except ValueError:
            continue

    the_number = ""
    for string in the_output:
        string = list(string)
        for i in range(len(string)):
            string[i] = letter_mapping[string[i]]
        string = "".join(string)
        print(string)
        #the_digit = str(string_digit[string])
        #the_number += the_digit
    
    print(letter_mapping)


    

def calculate_digits(string_map, the_output):
    pass



if __name__ == "__main__":
    the_input = []
    the_solution = 0 
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            line = line.strip()
            the_input, the_output = line.split(" | ")
            the_input = the_input.split(" ") 
            the_output = the_output.split(" ")
            work_out_numbers(the_input, the_output)
    print(f"The solution is {the_solution}")