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
        for line in reflection:
            print(line)

        reflection_values.append(find_reflection_line_value(reflection))
        print()

    print(f'Reflection sum: {sum(reflection_values)}')

    print(f'Time taken: {time.time() - start}')
    
def find_reflection_line_value(reflection):
    horizontal_reflection_line = find_horizontal_reflection_line(reflection)
    if horizontal_reflection_line > 0:
        return  100 * horizontal_reflection_line 
    
    return find_vertical_reflection_line(reflection)


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
    while y1 >= 0 and y2 < len(reflection) and are_equal:
        are_equal = are_rows_equal(reflection, y1, y2)
        y1 -= 1
        y2 += 1
    
    return are_equal

def are_rows_equal(reflection, y1, y2):
    are_equal = True
    if y1 < 0 or y2 >= len(reflection):
        return are_equal
    
    for i in range(len(reflection[y1])):
        if reflection[y1][i] != reflection[y2][i]:
            are_equal = False
            break

    return are_equal

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
    while x1 >= 0 and x2 < len(reflection[0]) and are_equal:
        are_equal = are_columns_equal(reflection, x1, x2)
        x1 -= 1
        x2 += 1

    return are_equal

def are_columns_equal(reflection, x1, x2):
    are_equal = True
    if x1 < 0 or x2 >= len(reflection[0]):
        return
    
    for i in range(len(reflection)):
        if reflection[i][x1] != reflection[i][x2]:
            are_equal = False
            break

    return are_equal

main()