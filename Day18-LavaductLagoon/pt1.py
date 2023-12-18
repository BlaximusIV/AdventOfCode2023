from collections import namedtuple
from queue import Queue

Coord = namedtuple("Coord", ["y", "x"])

def main():
    data = None
    with open('test_input.txt', 'r') as f:
        data = f.read().splitlines()

    hole_coords, min_y = draw_map(data)
    edge_count = get_edge_count(hole_coords)
    inside_count = find_inside_count(hole_coords, min_y)

    print(f"Total hole size: {edge_count + inside_count}")

def draw_map(data):
    hole_coords = {0: [0]}
    current = Coord(0, 0)
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for instruction in data:
        direction, distance, _ = instruction.split(" ")
        for _ in range(int(distance)):
            next = (Coord(current.y, current.x + 1) if direction == "R" 
                    else Coord(current.y, current.x - 1) if direction == "L" 
                    else Coord(current.y + 1, current.x) if direction == "D" 
                    else Coord(current.y - 1, current.x))
            
            if next.x < min_x:
                min_x = next.x
            if next.x > max_x:
                max_x = next.x
            if next.y < min_y:
                min_y = next.y
            if next.y > max_y:
                max_y = next.y
 
            if next.y not in hole_coords:
                hole_coords[next.y] = []
            hole_coords[next.y].append(next.x)
            current = next
    
    # print_map(hole_coords, min_x, max_x, min_y, max_y)
    return hole_coords, min_y

def print_map(hole_coords, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if y in hole_coords and x in hole_coords[y]:
                print("X", end="")
            else:
                print(".", end="")
        print("")

def get_edge_count(hole_coords):
    edge_count = 0
    for y in hole_coords:
        edge_count += len(hole_coords[y])

    return edge_count

def find_inside_count(hole_coords, min_y):
    visited = set()
    current = Coord(min_y + 1, hole_coords[min_y][0] + 1)
    q = Queue()
    q.put(current)
    while not q.empty():
        position = q.get()
        if position in visited:
            continue
        visited.add(position)

        neighbors = get_neighbors(hole_coords, position, visited)
        for neighbor in neighbors:
            q.put(neighbor)

    return len(visited)

def get_neighbors(hole_coords, current, visited):
    neighbors = []
    up = Coord(current.y - 1, current.x)
    down = Coord(current.y + 1, current.x)
    left = Coord(current.y, current.x - 1)
    right = Coord(current.y, current.x + 1)
    if up not in visited and up.x not in hole_coords[up.y]:
        neighbors.append(up)
    if down not in visited and down.x not in hole_coords[down.y]:
        neighbors.append(down)
    if left not in visited and left.x not in hole_coords[left.y]:
        neighbors.append(left)
    if right not in visited and right.x not in hole_coords[right.y]:
        neighbors.append(right)

    return neighbors

main()
