
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
    with open("input.txt") as f:
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
    steps = 1
    while not current_coordinates[0] == current_coordinates[1]:
        char_one = current_coordinates[0].coordinate_char(map)
        char_two = current_coordinates[1].coordinate_char(map)
        current_coordinates = get_next_coordinate(char_one, current_coordinates[0], previous_coordinates[0])
        current_coordinates[1], previous_coordinates[1] = get_next_coordinate(char_two, current_coordinates[1], previous_coordinates[1])

        steps += 1

    print(f'Farthest point is {steps} steps away')


def find_traversible_neighbors(map, coordinate):
    neighbors = []
    if coordinate.y >= 1:
        if map[coordinate.y - 1][coordinate.x] in ["|", "7", "F"]:
            neighbors.append(Coordinate(coordinate.x, coordinate.y - 1))
    if coordinate.y < len(map) - 1:
        if map[coordinate.y + 1][coordinate.x] in ["|", "J", "L"]:
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