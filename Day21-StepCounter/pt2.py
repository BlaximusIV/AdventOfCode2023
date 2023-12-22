from collections import namedtuple
from queue import Queue
import time

# point, steps, y, x
P = namedtuple('P', ['s', 'y', 'x'])

def main():
    start = time.time()
    map = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip("\n")
            chars = []
            for char in line:
                chars.append(char)
            map.append(chars)

    i, j = find_s(map)
    target_steps = 200
    count = find_location_count(P(0, i, j), map, target_steps)

    end = time.time()
    print(f'Total possible positions: {count}')
    print(f'Total time: {end - start}s')

def find_s(map):
    for i in range(len(map) - 1):
        for j in range(len(map[0]) - 1):
            if map[i][j] == "S":
                return i, j

def find_location_count(start, map, target_steps):
    steps = []
    seen = set()
    q = Queue()
    seen.add(start)
    q.put(start)
    while not q.empty():
        p = q.get()

        if p.s == target_steps:
            steps.append(p)
            continue

        neighbors = get_neighbors(p.y, p.x, map)
        for neighbor in neighbors:
            point = P(p.s + 1, neighbor[0], neighbor[1])

            if point not in seen:
                seen.add(point)
                q.put(point)
    
    return len(steps)

def get_neighbors(y, x, map):
    neighbors = []
    for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:    
        if map[ny % len(map)][nx % len(map[0])] != "#":
            neighbors.append((ny, nx))

    return neighbors

main()