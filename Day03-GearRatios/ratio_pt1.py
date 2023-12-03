import re

class Part_Number_Schematic:
    def __init__(self, number, y, x):
        self.number = number
        self.y = y
        self.x = x
        self.length = len(number)

# part number has number of part, along with y value and x range
PART_NUMBERS = []
# Symbols is a dict of symbols with the key being the y value and the value being a list of x values
SYMBOLS = { }

Y = 0
# Parse the line and add the part number and symbols to the respective lists
def process_line(line):
    global Y
    global PART_NUMBERS

    # Use regex to get part numbers from the line
    for part_number in re.finditer(r'(\d+)', line):
        # add the part number to the list of part numbers
        PART_NUMBERS.append(Part_Number_Schematic(part_number.group(0), Y, part_number.start()))

    # find indexes of symbols that are not numbers and not '.'
    for symbol in re.finditer(r'[^0-9.]', line):
        process_symbol(symbol.group(0), Y, symbol.start())

    Y += 1

def process_symbol(symbol, y, x):
    global SYMBOLS
    if y not in SYMBOLS:
        SYMBOLS[y] = []
    SYMBOLS[y].append(x)

def get_part_sum():
    global SYMBOLS
    global PART_NUMBERS
    sum = 0
    # if there are any symbols adjacent to any of the part number, we know they're a part we need, add the part number to the sum
    for part in PART_NUMBERS:
        is_part = False
        y = part.y
        # check left and right
        if y in SYMBOLS:
            x = part.x
            if x - 1 in SYMBOLS[y] or x + part.length in SYMBOLS[y]:
                is_part = True
        # check above
        if y - 1 in SYMBOLS and not is_part:
            x = part.x
            for i in range(x -1, x + part.length + 1):
                if i in SYMBOLS[y - 1]:
                    is_part = True
                    break
        # check below
        if y + 1 in SYMBOLS and not is_part:
            x = part.x
            for i in range(x -1, x + part.length + 1):
                if i in SYMBOLS[y + 1]:
                    is_part = True
                    break
        
        if is_part:
            sum += int(part.number)

    return sum

with open("input.txt") as input:
    for line in input:
        process_line(line.rstrip('\n'))

print(f'Sum of actual part numbers: {get_part_sum()}')
