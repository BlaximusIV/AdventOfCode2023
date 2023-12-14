import time

ROUND_ROCK = "O"

def main():
    start = time.time()
    map = []
    with open("test_input.txt") as f:
        input = f.readlines()
        for line in input:
            parts = []
            for char in line.strip("\n"):
                parts.append(char)
            map.append(parts)

    cycle_count = 3
    for i in range(cycle_count):
        move_rocks_north(map)
        move_rocks_west(map)
        move_rocks_south(map)
        move_rocks_east(map)
        # print_map(map)

    # now figure out how much they weigh on the north beam
    total_weight = find_north_beam_weight(map)
    print(f'Total weight: {total_weight}')
    print(f'Time: {time.time() - start}')

def move_rocks_north(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ROUND_ROCK:
                move_north(map, i, j)

def move_north(map, i, j):
    temp_i = i
    while temp_i > 0 and map[temp_i-1][j] == ".":
        temp_i -= 1
    
    map[i][j] = "."
    map[temp_i][j] = ROUND_ROCK

def move_rocks_south(map):
    for i in range(len(map) - 1, -1, -1):
        for j in range(len(map[i])):
            if map[i][j] == ROUND_ROCK:
                move_south(map, i, j)

def move_south(map, i, j):
    temp_i = i
    while temp_i < len(map) - 1 and map[temp_i+1][j] == ".":
        temp_i += 1
    
    map[i][j] = "."
    map[temp_i][j] = ROUND_ROCK

def move_rocks_east(map):
    for i in range(len(map)):
        for j in range(len(map[i]) - 1, -1, -1):
            if map[i][j] == ROUND_ROCK:
                move_east(map, i, j)

def move_east(map, i, j):
    temp_j = j
    while temp_j < len(map[i]) - 1 and map[i][temp_j+1] == ".":
        temp_j += 1
    
    map[i][j] = "."
    map[i][temp_j] = ROUND_ROCK

def move_rocks_west(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ROUND_ROCK:
                move_west(map, i, j)

def move_west(map, i, j):
    temp_j = j
    while temp_j > 0 and map[i][temp_j-1] == ".":
        temp_j -= 1
    
    map[i][j] = "."
    map[i][temp_j] = ROUND_ROCK

def find_north_beam_weight(map):
    total_weight = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ROUND_ROCK:
                weight = len(map) - i
                total_weight += weight
    
    return total_weight

def print_map(map):
    for i in range(len(map)):
        line = ""
        for j in range(len(map[i])):
            line += map[i][j]
        print(line)
    print()

main()