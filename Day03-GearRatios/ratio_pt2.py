import re

class Part_Number_Schematic:
    def __init__(self, number, x):
        self.number = number
        self.x_range = range(x, x + len(number))

def process_line(line, part_numbers, symbols, y):
    for part_number in re.finditer(r'(\d+)', line):
        part = Part_Number_Schematic(part_number.group(0), part_number.start())
        add_part_number(part_numbers, part, y)

    for symbol in re.finditer(r'[\*]', line):
        add_symbol(symbols, y, symbol.start())

def add_part_number(part_numbers, part_number, y):
    if y not in part_numbers:
        part_numbers[y] = []
    part_numbers[y].append(part_number)

def add_symbol(symbols, y, x):
    if y not in symbols:
        symbols[y] = []
    symbols[y].append(x)

def find_ratio_sums(part_numbers, symbols):
    sum = 0
    for y in symbols:
        for x in symbols[y]:
            adjacent_parts = []
            # check left and right
            if y in part_numbers:
                for part in part_numbers[y]:
                    if x - 1 in part.x_range or x + 1 in part.x_range:
                        adjacent_parts.append(part.number)
            # check above
            if y - 1 in part_numbers:
                for part in part_numbers[y - 1]:
                    if x in part.x_range or x + 1 in part.x_range or x - 1 in part.x_range:
                        adjacent_parts.append(part.number)
            # check below
            if y + 1 in part_numbers:
                for part in part_numbers[y + 1]:
                    if x in part.x_range or x + 1 in part.x_range or x - 1 in part.x_range:
                        adjacent_parts.append(part.number)

            if len(adjacent_parts) == 2:
                sum += int(adjacent_parts[0]) * int(adjacent_parts[1])

    return sum

def get_ratio_sums():
    part_numbers = {}
    symbols = {}

    with open("input.txt") as input:
        y = 0
        for line in input:
            process_line(line.rstrip('\n'), part_numbers, symbols, y)
            y += 1

    return find_ratio_sums(part_numbers, symbols)

print(f'Sum of actual part numbers: {get_ratio_sums()}')
