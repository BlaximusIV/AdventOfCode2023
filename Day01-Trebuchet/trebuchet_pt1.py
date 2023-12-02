import re

def process_line(line):
    numbers = re.findall('\d', line)
    return [numbers[0], numbers[-1]]

calibration_lines = []
with open("input.txt") as input:
    for line in input:
        line = line.rstrip('\n')
        calibration_lines.append(process_line(line))

calibration_sum = sum(int(str(line[0]) + str(line[1])) for line in calibration_lines)

print(f"Calibration number sum: {calibration_sum}")