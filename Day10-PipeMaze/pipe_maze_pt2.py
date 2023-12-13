
class Direction:
    def __init__(self):
        self.NORTH = "NORTH"
        self.SOUTH = "SOUTH"
        self.EAST = "EAST"
        self.WEST = "WEST"

class Coordinate:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

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
                start_coordinate = Coordinate(x=j, y=i, direction = Direction().SOUTH)
                break

    # find the first two coordinates to the path:
    current_coordinate = find_traversible_neighbors(map, start_coordinate)[0]
    previous_coordinate = start_coordinate
    loop_coordinates = {start_coordinate.y: {start_coordinate.x: start_coordinate.direction}}
    while not current_coordinate == start_coordinate:
        add_coordinate(current_coordinate, loop_coordinates)
        char = current_coordinate.coordinate_char(map)
        temp_coordinate = current_coordinate
        current_coordinate = get_next_coordinate(map, char, current_coordinate, previous_coordinate)
        previous_coordinate = temp_coordinate
    
    # print the loop coordinates
    # find the min and max x and y values
    min_x = min(loop_coordinates[0].keys())
    max_x = max(loop_coordinates[0].keys())
    min_y = min(loop_coordinates.keys())
    max_y = max(loop_coordinates.keys())
    for i in range(min_y, max_y + 1):
        line = ""
        for j in range(min_x, max_x + 1):
            if i in loop_coordinates and j in loop_coordinates[i]:
                line += " " + loop_coordinates[i][j][0] + " "
            else:
                line += " . "
        print(line.strip())

    inside_coordinates = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if i in loop_coordinates and j in loop_coordinates[i]:
                continue
            else:
                for k in range(j, len(map[i])):
                    if i in loop_coordinates and k in loop_coordinates[i]:
                        if loop_coordinates[i][k] == Direction().NORTH:
                            inside_coordinates.append(Coordinate(k, i, None))
                        break
    
    print(f'Count of inside coordinates: {len(inside_coordinates)}')
                    
    

def find_traversible_neighbors(map, coordinate):
    neighbors = []
    if coordinate.y >= 1:
        char = map[coordinate.y - 1][coordinate.x]
        if char in ["|", "7", "F"]:
            direction = Direction().NORTH if char == "|" else Direction().WEST if char == "7" else Direction().EAST
            neighbors.append(Coordinate(coordinate.x, coordinate.y - 1, direction))
    if coordinate.y < len(map) - 2:
        char = map[coordinate.y + 1][coordinate.x]
        if char in ["|", "J", "L"]:
            direction = Direction().SOUTH if char == "|" else Direction().WEST if char == "J" else Direction().EAST
            neighbors.append(Coordinate(coordinate.x, coordinate.y + 1, direction))
    if coordinate.x >= 1:
        char = map[coordinate.y][coordinate.x - 1]
        if char in ["-", "F", "L"]:
            direction = Direction().WEST if char == "-" else Direction().SOUTH if char == "F" else Direction().NORTH
            neighbors.append(Coordinate(coordinate.x - 1, coordinate.y, direction))
    if coordinate.x < len(map[coordinate.y]) - 2:
        char = map[coordinate.y][coordinate.x + 1]
        if char in ["-", "7", "J"]:
            direction = Direction().EAST if char == "-" else Direction().SOUTH if char == "7" else Direction().NORTH
            neighbors.append(Coordinate(coordinate.x + 1, coordinate.y, direction))

    return neighbors

def add_coordinate(coordinate, loop_coordinates):
    if coordinate.y not in loop_coordinates:
        loop_coordinates[coordinate.y] = {}
    loop_coordinates[coordinate.y][coordinate.x] = coordinate.direction

def get_next_coordinate(map, char, coordinate, previous_coordinate):
    if char == "|":
        if previous_coordinate.y < coordinate.y:
            # current heading south, augmented by next char
            next_char = map[coordinate.y + 1][coordinate.x]
            next_direction = get_next_direction(Direction().SOUTH, next_char)
            return Coordinate(coordinate.x, coordinate.y + 1, next_direction) 
        else:
            # current heading north, augmented by next char
            next_char = map[coordinate.y - 1][coordinate.x]
            next_direction = get_next_direction(Direction().NORTH, next_char)
            return Coordinate(coordinate.x, coordinate.y - 1, next_direction) 
    elif char == "-":
        if previous_coordinate.x < coordinate.x:
            # current heading east, augmented by next char
            next_char = map[coordinate.y][coordinate.x + 1]
            next_direction = get_next_direction(Direction().EAST, next_char)
            return Coordinate(coordinate.x + 1, coordinate.y, next_direction)
        else:
            # current heading west, augmented by next char
            next_char = map[coordinate.y][coordinate.x - 1]
            next_direction = get_next_direction(Direction().WEST, next_char)
            return Coordinate(coordinate.x - 1, coordinate.y, next_direction) 
    elif char == "L":
        if previous_coordinate.x > coordinate.x:
            # current heading north, augmented by next char
            next_char = map[coordinate.y - 1][coordinate.x]
            next_direction = get_next_direction(Direction().NORTH, next_char)
            return Coordinate(coordinate.x, coordinate.y -1, next_direction) 
        else:
            # current heading east, augmented by next char
            next_char = map[coordinate.y][coordinate.x + 1]
            next_direction = get_next_direction(Direction().EAST, next_char)
            return Coordinate(coordinate.x + 1, coordinate.y, next_direction) 
    elif char == "J":
        if previous_coordinate.y < coordinate.y:
            # current heading west, augmented by next char
            next_char = map[coordinate.y][coordinate.x - 1]
            next_direction = get_next_direction(Direction().WEST, next_char)
            return Coordinate(coordinate.x - 1, coordinate.y, next_direction) 
        else:
            # current heading north, augmented by next char
            next_char = map[coordinate.y - 1][coordinate.x]
            next_direction = get_next_direction(Direction().NORTH, next_char)
            return Coordinate(coordinate.x, coordinate.y - 1, next_direction) 
    elif char == "7":
        if previous_coordinate.y > coordinate.y:
            # current heading west, augmented by next char
            next_char = map[coordinate.y][coordinate.x - 1]
            next_direction = get_next_direction(Direction().WEST, next_char)
            return Coordinate(coordinate.x - 1, coordinate.y, next_direction) 
        else:
            # current heading south, augmented by next char
            next_char = map[coordinate.y + 1][coordinate.x]
            next_direction = get_next_direction(Direction().SOUTH, next_char)
            return Coordinate(coordinate.x, coordinate.y + 1, next_direction) 
    elif char == "F":
        if previous_coordinate.x > coordinate.x:
            # current heading south, augmented by next char
            next_char = map[coordinate.y + 1][coordinate.x]
            next_direction = get_next_direction(Direction().SOUTH, next_char)
            return Coordinate(coordinate.x, coordinate.y + 1, next_direction) 
        else:
            # current heading east, augmented by next char
            next_char = map[coordinate.y][coordinate.x + 1]
            next_direction = get_next_direction(Direction().EAST, next_char)
            return Coordinate(coordinate.x + 1, coordinate.y, next_direction)
        

def get_next_direction(current_direction, next_char):
    if current_direction == Direction().NORTH:
        if next_char == "|":
            return Direction().NORTH
        elif next_char == "7":
            return Direction().WEST
        elif next_char == "F":
            return Direction().EAST
    elif current_direction == Direction().SOUTH:
        if next_char == "|":
            return Direction().SOUTH
        elif next_char == "J":
            return Direction().WEST
        elif next_char == "L":
            return Direction().EAST
    elif current_direction == Direction().EAST:
        if next_char == "-":
            return Direction().EAST
        elif next_char == "7":
            return Direction().SOUTH
        elif next_char == "J":
            return Direction().NORTH
    elif current_direction == Direction().WEST:
        if next_char == "-":
            return Direction().WEST
        elif next_char == "F":
            return Direction().SOUTH
        elif next_char == "L":
            return Direction().NORTH
        

    

main()