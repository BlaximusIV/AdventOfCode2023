import time

ROUND_ROCK = "O"

def main():
    start = time.time()
    map = []
    with open("input.txt") as f:
        input = f.readlines()
        for line in input:
            parts = []
            for char in line.strip("\n"):
                parts.append(char)
            map.append(parts)

    cycle_length = find_cycle_length(map)
    remaining_iterations = 1_000_000_000 % cycle_length
    cycle_rocks(map, remaining_iterations + cycle_length)

    total_weight = find_north_beam_weight(map)
    print(f'Total weight: {total_weight}')
    
    print(f'Time: {time.time() - start}')

def cycle_rocks(map, cycle_count):
    for _ in range(cycle_count):
        move_rocks_north(map)
        move_rocks_west(map)
        move_rocks_south(map)
        move_rocks_east(map)

def find_cycle_length(map):
    map_copy = make_map_copy(map)
    map_copy2 = make_map_copy(map)

    iteration_count = 0
    while True:
        cycle_a = 1
        cycle_b = 2

        cycle_rocks(map_copy, cycle_a)
        cycle_rocks(map_copy2, cycle_b)

        iteration_count += 1
        if are_maps_equal(map_copy, map_copy2):
            break

        if iteration_count % 100 == 0:
            print(f'Iteration: {iteration_count}')

    return iteration_count

def make_map_copy(map):
    map_copy = []
    for i in range(len(map)):
        map_copy.append([])
        for j in range(len(map[i])):
            map_copy[i].append(map[i][j])
    
    return map_copy
    

def are_maps_equal(map1, map2):
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] != map2[i][j]:
                return False
    
    return True

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