import re

NUMBER_DICT = { "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }

def process_line(line):
    number_indices = [(i, char) for i, char in enumerate(line) if char.isdigit()]
    word_indices = []
    for word, number in NUMBER_DICT.items():
        for match in re.finditer(word, line):
            word_indices.append((match.start(), str(number)))
    combined_indices = sorted(number_indices + word_indices)
    # Return a two-item array of the first and last item's number, rather than index
    return [combined_indices[0][1], combined_indices[-1][1]]

calibration_lines = []
with open("input.txt") as input:
    for line in input:
        line = line.rstrip('\n')
        calibration_lines.append(process_line(line))

calibration_sum = sum(int(str(line[0]) + str(line[1])) for line in calibration_lines)

print(f"Calibration number sum: {calibration_sum}")