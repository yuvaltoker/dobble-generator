import json

# dobble generator:
# case 1- 
# num of cards: 31
# num of symbols: 31
# num of symbols in card: 6
# generates dobble game by sequens of 0,1,3,10,14,26 rotated num_of_symbols times

# case 2- 
# num of cards: 57
# num of symbols: 57
# num of symbols in card: 8
# generates dobble game by sequens of 0,1,3,13,32,36,43,52 rotated num_of_symbols times

num_of_symbols = 57
num_of_symbols_in_card = 8
sequenced_list = [0,1,3,13,32,36,43,52]


def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0, size):
        list_of_objects.append(list()) #different object reference each time
    return list_of_objects

# input: list of which indices (cards) to put the next symbol on
# increase the value of each index by 1, when past the max value (56), it make it zero
# as if they were indexes on a circle of 57 nodes
def rotate_right(sequence_list):
    global num_of_symbols
    for i in range(len(sequence_list)):
        new_value = sequence_list[i] + 1
        # if the new value reached to the end (num_of_symbols) it'll get back to zero
        if new_value >= num_of_symbols: # the last index is num_of_symbols - 1
            new_value = 0
        sequence_list[i] = new_value
    
    
def makeGrid(symbols_list):
    global num_of_symbols
    global sequenced_list
    cards = init_list_of_objects(num_of_symbols)
    for symbol in symbols_list:
        for i in sequenced_list:
            cards[i].append(symbol)
        rotate_right(sequenced_list)
    return cards

# input: a card as list of symbols
# do: checks how many symbols this card has
# returns tuple num_of_symbols in card & (True if the num of symbols is as the rules say, otherwise False) 
def is_num_of_symbols_okay(card, num_of_symbol_must_have):
    card_len = len(card)
    if len(card) != num_of_symbol_must_have:
        return card_len, False
    return card_len, True

# input: 2 cards as 2 lists of symbols
# do: count how many matching symbols these 2 cards have
# returns True if they have only 1 matching symbol, otherwise False
def is_num_of_matches_okay(card1, card2):
    counter = 0
    for card1_index in range(len(card1)):
        for card2_index in range(len(card2)):
            if card1[card1_index] == card2[card2_index]:
                counter = counter + 1
    if counter == 1:
        return True
    return False

# input: game cards as matrix of lists (3d list)
# do: validate if all cards obey the rules (1 same symbol between each pair of cards), and each cards has 8 symbols
# returns True in case of obeying the rules, otherwise False
def validate_game(cards):
    global num_of_symbols_in_card
    for card in cards:
        actual_num_of_symbols, is_rule1_fine = is_num_of_symbols_okay(card, num_of_symbols_in_card)
        if not is_rule1_fine:
            print("card num %d has %d symbols instead of %d" % (cards.index(card), actual_num_of_symbols, num_of_symbols_in_card))
            return False

    for index1 in range(len(cards)):
        for index2 in range(len(cards)):
            if index1 != index2:
                is_rule2_fine = is_num_of_matches_okay(cards[index1], cards[index2])
                if not is_rule2_fine:
                    print("cards No.%d and No.%d don't have only 1 matching symbol" % (index1, index2))
                    return False
            

    return True
   
            

def main():
    global num_of_symbols
    numbers_list = [x for x in range(num_of_symbols)] 
    cards = makeGrid(numbers_list)
    json_cards = json.dumps(cards)
    for sub_list in cards:
        print(sub_list)
    print(len(cards))
    if validate_game(cards):
        print("cards obey the rules :)")


if __name__ == "__main__":
    main()