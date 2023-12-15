import time

class ReflectionType:
    VERTICAL = 0
    HORIZONTAL = 1

def main():
    start = time.time()
    reflections = []
    with open("input.txt") as f:
        input = f.read().split("\n\n")
        for block in input:
            reflections.append(block.split("\n"))

    reflection_values = []
    for reflection in reflections:
        reflection_values.append(find_reflection_line_value(reflection))

    print(f'Reflection sum: {sum(reflection_values)}')

    print(f'Time taken: {time.time() - start}')
    
def find_reflection_line_value(reflection):
    horizontal_reflection_line = find_horizontal_reflection_line(reflection)
    if horizontal_reflection_line > 0:
        return  100 * horizontal_reflection_line
    
    vertical_reflection_line = find_vertical_reflection_line(reflection)
    return vertical_reflection_line


def find_horizontal_reflection_line(reflection):
    reflection_line = -1
    for i in range(1, len(reflection)):
        found = are_all_rows_equal(reflection, i - 1, i)
        if found:
            reflection_line = i
            break

    return reflection_line

def are_all_rows_equal(reflection, y1, y2):
    are_equal = True
    correction_total = 0
    while y1 >= 0 and y2 < len(reflection) and are_equal:
        are_equal, correction_count = are_rows_equal(reflection, y1, y2)
        correction_total += correction_count
        if correction_total > 1:
            are_equal = False
            break

        y1 -= 1
        y2 += 1
    
    return are_equal and correction_total == 1

def are_rows_equal(reflection, y1, y2):
    difference_count = 0
    are_equal = True
    if y1 < 0 or y2 >= len(reflection):
        return are_equal, difference_count
    
    for i in range(len(reflection[y1])):
        if reflection[y1][i] != reflection[y2][i]:
            difference_count += 1
            if difference_count > 1:
                are_equal = False
                break

    return are_equal, difference_count

def find_vertical_reflection_line(reflection):
    reflection_line = -1
    for i in range(1, len(reflection[0])):
        found = are_all_columns_equal(reflection, i - 1, i)
        if found:
            reflection_line = i
            break

    return reflection_line

def are_all_columns_equal(reflection, x1, x2):
    are_equal = True
    correction_total = 0
    while x1 >= 0 and x2 < len(reflection[0]) and are_equal:
        are_equal, correction_count = are_columns_equal(reflection, x1, x2)
        correction_total += correction_count
        if correction_count > 1:
            are_equal = False
            break

        x1 -= 1
        x2 += 1

    return are_equal and correction_total == 1

def are_columns_equal(reflection, x1, x2):
    difference_count = 0
    are_equal = True
    if x1 < 0 or x2 >= len(reflection[0]):
        return are_equal, difference_count
    
    for i in range(len(reflection)):
        if reflection[i][x1] != reflection[i][x2]:
            difference_count += 1
            if difference_count > 1:
                are_equal = False
                break

    return are_equal, difference_count

main()