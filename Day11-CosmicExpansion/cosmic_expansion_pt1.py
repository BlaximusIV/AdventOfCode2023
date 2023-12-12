import time

class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    start = time.time()

    galaxies_array = []
    galaxies_map = {}
    input_width = 0
    input_height = 0
    with open("input.txt") as f:
        input = f.readlines()
        input_width = len(input[0].strip("\n"))
        input_height = len(input)
        for i in range(len(input)):
            line = input[i].strip("\n")
            for j in range(len(line)):
                if line[j] == "#":
                    if i not in galaxies_map:
                        galaxies_map[i] = [j]
                    else:
                        galaxies_map[i].append(j)

                    galaxies_array.append(Galaxy(j, i))
    
    horizontal_spaces, vertical_spaces = find_spaces(input_width, input_height, galaxies_map)
    expand_spaces(horizontal_spaces, vertical_spaces, galaxies_array)
    manhattan_distances = find_manhattan_distances(galaxies_array)

    print(f'Distance between all galaxies: {sum(manhattan_distances)}')
    end = time.time()
    print(f'Time: {end - start}')

def find_spaces(width, height, map):
    horizontal_spaces = []
    vertical_spaces = []
    for i in range(height):
        if i not in map:
            horizontal_spaces.append(i)

    for i in range(width):
        has_vertical_galaxy = False
        for key in map:
            if i in map[key]:
                has_vertical_galaxy = True
                break

        if not has_vertical_galaxy:
            vertical_spaces.append(i)

    return horizontal_spaces, vertical_spaces

def expand_spaces(horizontal_spaces, vertical_spaces, galaxies_array):
    for galaxy in galaxies_array:
        y_increment = 0
        x_increment = 0
        for i in range(len(horizontal_spaces)):
            if galaxy.y > horizontal_spaces[i]:
                y_increment += 1

        for i in range(len(vertical_spaces)):
            if galaxy.x > vertical_spaces[i]:
                x_increment += 1

        galaxy.y += y_increment
        galaxy.x += x_increment

def find_manhattan_distances(galaxies_array):
    manhattan_distances = []
    for i in range(len(galaxies_array)):
        for j in range(i + 1, len(galaxies_array)):
            manhattan_distances.append(abs(galaxies_array[i].x - galaxies_array[j].x) + abs(galaxies_array[i].y - galaxies_array[j].y))

    return manhattan_distances

def print_galaxies(galaxies_array):
    max_x = 0
    max_y = 0
    for galaxy in galaxies_array:
        if galaxy.x > max_x:
            max_x = galaxy.x
        if galaxy.y > max_y:
            max_y = galaxy.y

    map = []
    for i in range(max_y + 1):
        map.append([])
        for j in range(max_x + 1):
            map[i].append(".")

    for galaxy in galaxies_array:
        map[galaxy.y][galaxy.x] = "#"

    for i in range(len(map)):
        print("".join(map[i]))


main()