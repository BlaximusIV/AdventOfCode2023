from heapq import heappush, heappop
from collections import namedtuple

Coord = namedtuple("Coord", ["y", "x"])

NORTH = "^"
SOUTH = "v"
EAST = ">"
WEST = "<"

def main():
    print("Day 17 pt 1.")

    map = []
    with open("test_input.txt", "r") as input:
        for line in input:
            losses = []
            for char in line.strip("\n"):
                losses.append(int(char))
            map.append(losses)

    start = Coord(0, 0)
    end = Coord(len(map) - 1, len(map[0]) - 1)
    path = find_shortest_path(map, start, end)
    print(f"Least heat loss: {path}")

    # for line in map:
    #     print(line)

def find_shortest_path(map, start, end):
    frontier = [(0, start)]
    cost_so_far = {start: 0}
    came_from = {}

    while frontier:
        current = heappop(frontier)[1]
        if current == end:
            break

        previous_directions = get_previous_directions(current, came_from)
        for next in get_neighbors(map, current, previous_directions):
            new_cost = cost_so_far[current] + map[next.y][next.x]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heappush(frontier, (new_cost, next))
                came_from[next] = current

    print_path(map, came_from, start, end)

    return cost_so_far[end]

def get_previous_directions(current, came_from):
    previous_positions = []
    while len(previous_positions) < 3 and came_from.get(current):
        previous_positions.append(came_from[current])
        current = came_from[current]

    temp_current = current
    previous_directions = []
    for direction in previous_positions:
        if direction.y > temp_current.y:
            previous_directions.append(NORTH)
        elif direction.y < temp_current.y:
            previous_directions.append(SOUTH)
        elif direction.x > temp_current.x:
            previous_directions.append(WEST)
        elif direction.x < temp_current.x:
            previous_directions.append(EAST)
        temp_current = direction

    return previous_directions

# will need augmented to disallow going the same direction 3x in a row
def get_neighbors(map, coord, previous_directions):
    all_north = len(previous_directions) > 2 and all(direction == NORTH for direction in previous_directions)
    all_south = len(previous_directions) > 2 and all(direction == SOUTH for direction in previous_directions)
    all_east = len(previous_directions) > 2 and all(direction == EAST for direction in previous_directions)
    all_west = len(previous_directions) > 2 and all(direction == WEST for direction in previous_directions)

    most_recent_direction = previous_directions[-1] if len(previous_directions) > 0 else None
    neighbors = []
    if coord.y > 0 and not all_north and most_recent_direction != SOUTH:
        neighbors.append(Coord(coord.y - 1, coord.x))
    if coord.y < len(map) - 1 and not all_south and most_recent_direction != NORTH:
        neighbors.append(Coord(coord.y + 1, coord.x))
    if coord.x > 0 and not all_west and most_recent_direction != EAST:
        neighbors.append(Coord(coord.y, coord.x - 1))
    if coord.x < len(map[0]) - 1 and not all_east and most_recent_direction != WEST:
        neighbors.append(Coord(coord.y, coord.x + 1))

    return neighbors


def print_path(map, came_from, start, end):
    current = end
    came_from_coords = {}
    while current != start:
        if current.y not in came_from_coords:
            came_from_coords[current.y] = []
        came_from_coords[current.y].append(current.x)
        
        current = came_from[current]
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            if y in came_from_coords and x in came_from_coords[y]:
                print("O", end="")
            else:
                print(".", end="")
        print()
    

main()