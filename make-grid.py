# dobble generator:
# num of cards: 57
# num of symbols: 57
num_of_symbols = 57
sequenced_list = [0, 1, 3, 13, 32, 36, 43, 52]
# generates dobble game by sequens of 0,1,3,13,32,36,43,52 rotated num_of_symbols times

# input: list of which indices (cards) to put the next symbol on
# increase the value of each index by 1, when past the max value (56), it make it zero
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
    cards = [[]] * num_of_symbols
    for symbol in symbols_list:
        for i in sequenced_list:
            cards[sequenced_list].append(symbol)
        rotate_right(sequenced_list)

def main():
    global num_of_symbols
    numbers_list = [x for x in range(num_of_symbols)] 
    cards = makeGrid(numbers_list)
    print(cards)


if __name__ == "__main__":
    main()