
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, coordinate):
        return self.x == coordinate.x and self.y == coordinate.y
    
    def coordinate_char(self, map):
        return map[self.y][self.x]

NORTH = "^"
SOUTH = "v"
EAST = ">"
WEST = "<"

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

    # find the path and direction of the path at each step. 
    loop_path_tiles = {}
    start_direction, current_coordinate, current_direction = find_starting_orientation(start_coordinate, map)
    loop_path_tiles[start_coordinate.y] = { start_coordinate.x: start_direction }
    while current_coordinate != start_coordinate:
        # Add current coordinate to the loop path tiles
        if current_coordinate.y not in loop_path_tiles:
            loop_path_tiles[current_coordinate.y] = {}
        loop_path_tiles[current_coordinate.y][current_coordinate.x] = current_direction

        # find the next coordinate and direction
        current_coordinate, current_direction = find_next_coordinate(current_coordinate, current_direction, map)

    # find the tiles inside the loop. If the tile is inside the loop, the first loop tile it connects with to the east will be facing north
    print_loop(loop_path_tiles, map)

def find_starting_orientation(start_coordinate, map):
    start_direction = None
    current_coordinate = None
    current_direction = None
    north_coordinate = Coordinate(x=start_coordinate.x, y=start_coordinate.y - 1)
    east_coordinate = Coordinate(x=start_coordinate.x + 1, y=start_coordinate.y)
    south_coordinate = Coordinate(x=start_coordinate.x, y=start_coordinate.y + 1)
    west_coordinate = Coordinate(x=start_coordinate.x - 1, y=start_coordinate.y)
    # start coordinate is not on the edge of the map
    if north_coordinate.coordinate_char(map) in ["|", "7", "F"]:
        current_direction = NORTH
        current_coordinate = north_coordinate
    elif east_coordinate.coordinate_char(map) in ["-", "7", "J"]:
        current_coordinate = east_coordinate
        current_char = current_coordinate.coordinate_char(map)
        current_direction = EAST if current_char == "-" else SOUTH if current_char == "7" else NORTH
    elif south_coordinate.coordinate_char(map) in ["|", "L", "J"]:
        current_direction = SOUTH
        current_coordinate = south_coordinate
    else:
        current_coordinate = west_coordinate
        current_char = current_coordinate.coordinate_char(map)
        current_direction = WEST if current_char == "-" else NORTH if current_char == "L" else SOUTH

    if west_coordinate.coordinate_char(map) in ["-", "L", "F"]:
        start_direction = EAST
    elif south_coordinate.coordinate_char(map) in ["|", "L", "J"]:
        start_direction = NORTH
    elif east_coordinate.coordinate_char(map) in ["-", "7", "J"]:
        start_direction = WEST
    else:
        start_direction = SOUTH

    return start_direction, current_coordinate, current_direction

def find_next_coordinate(current_coordinate, current_direction, map):
    current_char = current_coordinate.coordinate_char(map)
    next_coordinate = None
    next_direction = None

    if current_char == "|":
        if current_direction == NORTH:
            next_coordinate = Coordinate(x=current_coordinate.x, y=current_coordinate.y - 1)
            next_direction = NORTH
        else:
            next_coordinate = Coordinate(x=current_coordinate.x, y=current_coordinate.y + 1)
            next_direction = SOUTH
    elif current_char == "-":
        if current_direction == EAST:
            next_coordinate = Coordinate(x=current_coordinate.x + 1, y=current_coordinate.y)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = EAST if next_char == "-" else SOUTH if next_char == "7" else NORTH
        else:
            next_coordinate = Coordinate(x=current_coordinate.x - 1, y=current_coordinate.y)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = WEST if next_char == "-" else NORTH if next_char == "L" else SOUTH
    elif current_char == "7":
        if current_direction == NORTH:
            next_coordinate = Coordinate(x=current_coordinate.x - 1, y=current_coordinate.y)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = WEST if next_char == "-" else SOUTH if next_char == "F" else NORTH
        else:
            next_coordinate = Coordinate(x=current_coordinate.x, y=current_coordinate.y + 1)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = SOUTH
    elif current_char == "L":
        if current_direction == SOUTH:
            next_coordinate = Coordinate(x=current_coordinate.x + 1, y=current_coordinate.y)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = EAST if next_char == "-" else SOUTH if next_char == "7" else NORTH
        else:
            next_coordinate = Coordinate(x=current_coordinate.x, y=current_coordinate.y - 1)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = NORTH
    elif current_char == "F":
        if current_direction == NORTH:
            next_coordinate = Coordinate(x=current_coordinate.x + 1, y=current_coordinate.y)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = EAST if next_char == "-" else NORTH if next_char == "J" else SOUTH
        else:
            next_coordinate = Coordinate(x=current_coordinate.x, y=current_coordinate.y + 1)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = SOUTH
    elif current_char == "J":
        if current_direction == SOUTH:
            next_coordinate = Coordinate(x=current_coordinate.x - 1, y=current_coordinate.y)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = WEST if next_char == "-" else NORTH if next_char == "L" else SOUTH
        else:
            next_coordinate = Coordinate(x=current_coordinate.x, y=current_coordinate.y - 1)
            next_char = next_coordinate.coordinate_char(map)
            next_direction = NORTH
    else:
        print("Error: current char is not a valid pipe character")

    return next_coordinate, next_direction

def print_loop(loop_path_tiles, map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if i in loop_path_tiles and j in loop_path_tiles[i]:
                print(loop_path_tiles[i][j], end="")
            else:
                print(" ", end="")
        print()

main()