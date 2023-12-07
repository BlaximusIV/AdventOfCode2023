import time

class hand:
    def __init__(self, cards_string_array, cards, bid):
        self.cards_string_array = cards_string_array
        self.cards = cards
        self.bid = bid

CHAR_VALUES = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
def get_hand(line):
    card_string, bid = line.split()
    cards = []
    for card in card_string:
        if card in CHAR_VALUES:
            cards.append(CHAR_VALUES[card])
        else:
            cards.append(int(card))

    cards_string_array = list(card_string)
    current_hand =  hand(cards_string_array, cards, int(bid))
    # change the J's in the cards string array to whatever would make the hand get into the most valuable group
    if 'J' in current_hand.cards_string_array:
        # find the character that has the most occurances in the hand
        joker_val = find_joker_value(current_hand)
        # replace all the J's with that character
        current_hand.cards_string_array = [joker_val if char == 'J' else char for char in current_hand.cards_string_array]

    return current_hand

def find_joker_value(hand):
    # Get character counts
    char_counts = {}
    # check if every character in the hand is a J. If so, return the first character in the hand
    if all(char == 'J' for char in hand.cards_string_array):
        return hand.cards_string_array[0]

    for char in hand.cards_string_array:
        if char != 'J':
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    # sort the characters by their count, then by their value
    sorted_char_counts = sorted(char_counts.items(), key=lambda x: (x[1], CHAR_VALUES[x[0]]), reverse=True)
    return sorted_char_counts[0][0]
    

def group_hands(hands):
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for hand in hands:
        if is_five_of_a_kind(hand):
            five_of_a_kind.append(hand)
        elif is_four_of_a_kind(hand):
            four_of_a_kind.append(hand)
        elif is_full_house(hand):
            full_house.append(hand)
        elif is_three_of_a_kind(hand):
            three_of_a_kind.append(hand)
        elif is_two_pair(hand):
            two_pair.append(hand)
        elif is_one_pair(hand):
            one_pair.append(hand)
        else:
            high_card.append(hand)

    return [high_card, one_pair, two_pair, three_of_a_kind, full_house, four_of_a_kind, five_of_a_kind]

def is_five_of_a_kind(hand):
    return len(set(hand.cards_string_array)) == 1

def is_four_of_a_kind(hand):
    return any(hand.cards_string_array.count(card) == 4 for card in set(hand.cards_string_array))

def is_full_house(hand):
    return any(hand.cards_string_array.count(card) == 3 for card in set(hand.cards_string_array)) and any(hand.cards_string_array.count(card) == 2 for card in set(hand.cards_string_array))

def is_three_of_a_kind(hand):
    return any(hand.cards_string_array.count(card) == 3 for card in set(hand.cards_string_array))

def is_two_pair(hand):
    return sum(hand.cards_string_array.count(card) == 2 for card in set(hand.cards_string_array)) == 2

def is_one_pair(hand):
    return any(hand.cards_string_array.count(card) == 2 for card in set(hand.cards_string_array))


def main():
    start = time.time()

    # Get the input
    with open("input.txt", "r") as file:
        input = file.readlines()

    # Create a list of lists, where each list is a hand
    hands = []
    for line in input:
        hands.append(get_hand(line.strip('\n')))

    # get groups
    groups  = group_hands(hands)

    # sort each group's hands with the highest valued hands at the end of the list. Value is determined left to right, like multi digit numbers.
    for group in groups:
        group.sort(key=lambda x: x.cards, reverse=False)

    # combine the sorted groups into a single list, least valuable to most valueable. High card -> one pair -> two pair -> three of a kind -> full house -> four of a kind -> five of a kind
    sorted_hands = []
    for group in groups:
        sorted_hands.extend(group)

    # Determine each hand's value. Value is the hand's rank multiplied by its bid. Sum the values of each hand to get the total value.
    total_value = 0
    for i in range(len(sorted_hands)):
        total_value += (i + 1) * sorted_hands[i].bid

    print(f'Total value: {total_value}')
    end = time.time()
    print(f'Time: {end - start}')


main()