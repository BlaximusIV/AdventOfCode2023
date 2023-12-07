import time

class hand:
    def __init__(self, cards_string, cards, bid):
        self.cards_string = cards_string
        self.cards = cards
        self.bid = bid

CHAR_VALUES = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
def get_hand(line):
    card_string, bid = line.split()
    cards = []
    for card in card_string:
        if card in CHAR_VALUES:
            cards.append(CHAR_VALUES[card])
        else:
            cards.append(int(card))
    return hand(card_string, cards, int(bid))

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
    return len(set(hand.cards)) == 1

def is_four_of_a_kind(hand):
    return any(hand.cards.count(card) == 4 for card in set(hand.cards))

def is_full_house(hand):
    return any(hand.cards.count(card) == 3 for card in set(hand.cards)) and any(hand.cards.count(card) == 2 for card in set(hand.cards))

def is_three_of_a_kind(hand):
    return any(hand.cards.count(card) == 3 for card in set(hand.cards))

def is_two_pair(hand):
    return sum(hand.cards.count(card) == 2 for card in set(hand.cards)) == 2

def is_one_pair(hand):
    return any(hand.cards.count(card) == 2 for card in set(hand.cards))


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