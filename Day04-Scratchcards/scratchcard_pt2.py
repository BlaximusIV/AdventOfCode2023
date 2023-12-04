class Scratchcard:
    def __init__(self, card_number, winning_draws_count):
        self.card_number = card_number
        self.winning_draws_count = winning_draws_count

def get_winning_draws_count(winning_numbers, drawn_numbers):
    winning_draws_count = 0
    for drawn_number in drawn_numbers:
        if drawn_number in winning_numbers:
            winning_draws_count += 1
    return winning_draws_count

def process_line(line):
    card_number = int(line.split(':')[0].split()[1])
    parts = [part.strip() for part in line.split(':')[1].split('|')]
    winning_numbers = [int(num) for num in parts[0].split()]
    drawn_numbers = [int(num) for num in parts[1].split()]
    winning_draws_count = get_winning_draws_count(winning_numbers, drawn_numbers)
    return Scratchcard(card_number, winning_draws_count)

def win_cards(card_win_counts, card_totals):
    for card in card_win_counts:
        for i in range(card + 1, card + card_win_counts[card] + 1):
            if i in card_totals:
                card_totals[i] += card_totals[card]

def find_scratchcard_values():
    with open('input.txt') as input:
        card_totals = {}
        card_win_counts = {}
        for line in input:
            card = process_line(line.rstrip('\n'))
            card_win_counts[card.card_number] = card.winning_draws_count
            card_totals[card.card_number] = 1

        win_cards(card_win_counts, card_totals)

    return sum(card_totals.values())

print(f'Sum of scratch card values: {find_scratchcard_values()}')
