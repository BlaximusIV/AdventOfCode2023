
class Direction:
    def __init__(self):
        self.UP = "UP"
        self.DOWN = "DOWN"
        self.LEFT = "LEFT"
        self.RIGHT = "RIGHT"



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
    loop_coordinates = {start_coordinate.y: [start_coordinate.x]}
    while not current_coordinate == start_coordinate:
        add_coordinate(current_coordinate, loop_coordinates)
        char = current_coordinate.coordinate_char(map)
        current_coordinate, previous_coordinate, _ = get_next_coordinate(char, current_coordinate, previous_coordinate)

    current_coordinate = find_traversible_neighbors(map, start_coordinate)[0]
    previous_coordinate = start_coordinate
    inside_coordinates = {}
    while not current_coordinate == start_coordinate:
        char = current_coordinate.coordinate_char(map)

        # find the coordinates of the inside of the loop
        # follow the loop, if a character is on the 

    # new_map = []
    # for i in range(len(map)):
    #     chars = []
    #     for j in range(len(line)):
    #         if i in loop_coordinates and j in loop_coordinates[i]:
    #             chars.append("X")
    #         else:
    #             chars.append(".")
    #     new_map.append(chars)

    # for line in new_map:
    #     print("".join(line))

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

def add_coordinate(coordinate, loop_coordinates):
    if coordinate.y in loop_coordinates:
        loop_coordinates[coordinate.y].append(coordinate.x)
    else:
        loop_coordinates[coordinate.y] = [coordinate.x]

def get_next_coordinate(char, coordinate, previous_coordinate, inside):
    if char == "|":
        if previous_coordinate.y < coordinate.y:
            return Coordinate(coordinate.x, coordinate.y + 1), coordinate, inside
        else:
            return Coordinate(coordinate.x, coordinate.y - 1), coordinate, inside
    elif char == "-":
        if previous_coordinate.x < coordinate.x:
            return Coordinate(coordinate.x + 1, coordinate.y), coordinate, inside
        else:
            return Coordinate(coordinate.x - 1, coordinate.y), coordinate, inside
    elif char == "L":
        if previous_coordinate.x > coordinate.x:
            return Coordinate(coordinate.x, coordinate.y -1), coordinate
        else:
            return Coordinate(coordinate.x + 1, coordinate.y), coordinate
    elif char == "J":
        if previous_coordinate.y < coordinate.y:
            return Coordinate(coordinate.x - 1, coordinate.y), coordinate
        else:
            return Coordinate(coordinate.x, coordinate.y - 1), coordinate
    elif char == "7":
        if previous_coordinate.y > coordinate.y:
            return Coordinate(coordinate.x - 1, coordinate.y), coordinate
        else:
            return Coordinate(coordinate.x, coordinate.y + 1), coordinate
    elif char == "F":
        if previous_coordinate.x > coordinate.x:
            return Coordinate(coordinate.x, coordinate.y + 1), coordinate
        else:
            return Coordinate(coordinate.x + 1, coordinate.y), coordinate

main()