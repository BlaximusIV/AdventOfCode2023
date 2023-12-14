
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, coordinate):
        return self.x == coordinate.x and self.y == coordinate.y
    
    def coordinate_char(self, map):
        return map[self.y][self.x]


def main():
    map = []
    with open("test_input.txt") as f:
        input = f.readlines()
        for line in input:
            map.append(line.strip("\n"))

    # find the S coordinate
    start_coordinate = None
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                start_coordinate = Coordinate(x=j, y=i)
                break

    # find the first two coordinates to the path:
    current_coordinate = find_traversible_neighbors(map, start_coordinate)[0]
    previous_coordinate = start_coordinate
    loop_coordinates = { start_coordinate.y: [start_coordinate.x] }
    while not current_coordinate == start_coordinate:
        if current_coordinate.y not in loop_coordinates:
            loop_coordinates[current_coordinate.y] = [current_coordinate.x]
        else:
            loop_coordinates[current_coordinate.y].append(current_coordinate.x)

        char_one = current_coordinate.coordinate_char(map)
        temp_coordinate = current_coordinate
        current_coordinate = get_next_coordinate(char_one, current_coordinate, previous_coordinate)
        previous_coordinate = temp_coordinate

    # print the loop coordinates
    # find the min and max x and y values
    min_x = 0
    max_x = len(map[0])
    min_y = 0
    max_y = len(map)
    for i in range(min_y, max_y):
        line = ""
        for j in range(min_x, max_x):
            if i in loop_coordinates and j in loop_coordinates[i]:
                line += " X "
            else:
                line += " . "
        print(line.strip())
        print()


def find_traversible_neighbors(map, coordinate):
    neighbors = []
    if coordinate.y >= 1:
        if map[coordinate.y - 1][coordinate.x] in ["|", "7", "F", "S"]:
            neighbors.append(Coordinate(coordinate.x, coordinate.y - 1))
    if coordinate.y < len(map) - 1:
        if map[coordinate.y + 1][coordinate.x] in ["|", "J", "L", "S"]:
            neighbors.append(Coordinate(coordinate.x, coordinate.y + 1))
    if coordinate.x >= 1:
        if map[coordinate.y][coordinate.x - 1] in ["-", "F", "L"]:
            neighbors.append(Coordinate(coordinate.x - 1, coordinate.y))
    if coordinate.x < len(map[coordinate.y]) - 2:
        if map[coordinate.y][coordinate.x + 1] in ["-", "7", "J"]:
            neighbors.append(Coordinate(coordinate.x + 1, coordinate.y))

    return neighbors

def get_next_coordinate(char, coordinate, previous_coordinate):
    if char == "|":
        if previous_coordinate.y < coordinate.y:
            return Coordinate(coordinate.x, coordinate.y + 1)
        else:
            return Coordinate(coordinate.x, coordinate.y - 1)
    elif char == "-":
        if previous_coordinate.x < coordinate.x:
            return Coordinate(coordinate.x + 1, coordinate.y)
        else:
            return Coordinate(coordinate.x - 1, coordinate.y)
    elif char == "L":
        if previous_coordinate.x > coordinate.x:
            return Coordinate(coordinate.x, coordinate.y -1)
        else:
            return Coordinate(coordinate.x + 1, coordinate.y)
    elif char == "J":
        if previous_coordinate.y < coordinate.y:
            return Coordinate(coordinate.x - 1, coordinate.y)
        else:
            return Coordinate(coordinate.x, coordinate.y - 1)
    elif char == "7":
        if previous_coordinate.y > coordinate.y:
            return Coordinate(coordinate.x - 1, coordinate.y)
        else:
            return Coordinate(coordinate.x, coordinate.y + 1)
    elif char == "F":
        if previous_coordinate.x > coordinate.x:
            return Coordinate(coordinate.x, coordinate.y + 1)
        else:
            return Coordinate(coordinate.x + 1, coordinate.y)

main()