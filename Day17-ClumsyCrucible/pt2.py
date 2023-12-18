from heapq import heappush, heappop
from collections import namedtuple

Pos = namedtuple("Pos", ["y", "x", "dir", "ct"])

NORTH = "^"
SOUTH = "v"
EAST = ">"
WEST = "<"

def main():
    map = []
    with open("input.txt", "r") as input:
        for line in input:
            losses = []
            for char in line.strip("\n"):
                losses.append(int(char))
            map.append(losses)

    path = find_shortest_path(map)
    print(f"Least heat loss: {path}")


def find_shortest_path(map):
    came_from = set()
    q = [(0, Pos(0, 0, None, 0))]

    while q:
        cost, pos = heappop(q)
        if pos.y == len(map) - 1 and pos.x == len(map[0]) - 1:
            return cost
        
        if pos in came_from:
            continue

        came_from.add(pos)

        if pos.ct < 10 and pos.dir:
            new_y = pos.y + 1 if pos.dir == SOUTH else pos.y - 1 if pos.dir == NORTH else pos.y
            new_x = pos.x + 1 if pos.dir == EAST else pos.x - 1 if pos.dir == WEST else pos.x
            new_pos = Pos(new_y, new_x, pos.dir, pos.ct + 1)
            if new_pos.y >= 0 and new_pos.y < len(map) and new_pos.x >= 0 and new_pos.x < len(map[0]):
                heappush(q, (cost + map[new_pos.y][new_pos.x], new_pos))
        
        if pos.ct >= 4 or pos.ct == 0:
            for new_direction in [NORTH, SOUTH, EAST, WEST]:
                if new_direction != pos.dir and new_direction != opposite_direction(pos.dir):
                    new_y = pos.y + 1 if new_direction == SOUTH else pos.y - 1 if new_direction == NORTH else pos.y
                    new_x = pos.x + 1 if new_direction == EAST else pos.x - 1 if new_direction == WEST else pos.x
                    new_pos = Pos(new_y, new_x, new_direction, 1)
                    if new_pos.y >= 0 and new_pos.y < len(map) and new_pos.x >= 0 and new_pos.x < len(map[0]):
                        heappush(q, (cost + map[new_pos.y][new_pos.x], new_pos))


def opposite_direction(direction):
    if direction == NORTH:
        return SOUTH
    elif direction == SOUTH:
        return NORTH
    elif direction == EAST:
        return WEST
    elif direction == WEST:
        return EAST
    
main()