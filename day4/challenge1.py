import sys
import numpy as np

def check_if_won(bingo_card):
    for x in range(5):
        if np.sum(bingo_card[x,:]) == -5:
            return True
    
    for y in range(5):
        if np.sum(bingo_card[:,y]) == -5:
            return True
    
    return False



def fill_bingo_cards(bingo_cards, bingo_input):
    for i in range(len(bingo_input)):

        the_num = bingo_input[i]
        for j in range(len(bingo_cards)):
            card_flatten = bingo_cards[j].flatten(order='C')
            indexes = np.where(card_flatten == the_num)
            card_flatten[indexes] = -1
            bingo_cards[j] = card_flatten.reshape(5,5)

        if i >=5:
            for j in range(len(bingo_cards)):
                result = check_if_won(bingo_cards[j])
                if result:
                    return (bingo_cards[j], the_num)

def solution(bingo_cards, bingo_input):
    winning_bingo_card, final_num = fill_bingo_cards(bingo_cards, bingo_input)
    flat_winner = winning_bingo_card.flatten(order='C')
    remaining_sum = np.sum(flat_winner[np.where(flat_winner != -1)])
    return remaining_sum * final_num

    



if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        file_input = f.readlines()
        bingo_input = file_input[0].split(",")
        bingo_input = [int(num) for num in bingo_input]
        i = 2
        bingo_cards = []
        while i < len(file_input):
            bingo_card = file_input[i:i+5]
            for j in range(len(bingo_card)):
                line = bingo_card[j].strip()
                line = line.split(" ")
                bingo_card[j] = [int(num) for num in line if num] 
            bingo_cards.append(np.array(bingo_card))
            i += 6
        the_solution = solution(bingo_cards, bingo_input)
        print(f"The solution is {the_solution}")