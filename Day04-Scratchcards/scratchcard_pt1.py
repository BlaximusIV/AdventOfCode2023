def process_line(line):
    parts = [part.strip() for part in line.split(':')[1].split('|')]
    winning_numbers = [int(num) for num in parts[0].split()]
    drawn_numbers = [int(num) for num in parts[1].split()]
    return [winning_numbers, drawn_numbers]

def increment_card_value(card_value):
    if card_value == 0:
        return 1
    else:
        return card_value * 2

def find_deck_value(card_sets):
    sum = 0
    for card_set in card_sets:
        winning_numbers = card_set[0]
        drawn_numbers = card_set[1]
        card_value = 0
        for drawn_number in drawn_numbers:
            if drawn_number in winning_numbers:
                card_value = increment_card_value(card_value)
        
        sum += card_value

    return sum

def find_scratchcard_values():
    with open('input.txt') as input:
        card_sets = []
        for line in input:
            card_sets.append(process_line(line.rstrip('\n')))

    return find_deck_value(card_sets)

print(f'Sum of scratch card values: {find_scratchcard_values()}')
