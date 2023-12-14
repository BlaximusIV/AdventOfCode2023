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

    # roll the rocks (O) north. They stop when they encounter the top, another rock, or a square rock (#)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ROUND_ROCK:
                move_north(map, i, j)

    # now figure out how much they weigh on the north beam
    total_weight = find_north_beam_weight(map)
    print(f'Total weight: {total_weight}')
    print(f'Time: {time.time() - start}')

def move_north(map, i, j):
    temp_i = i
    while temp_i > 0 and map[temp_i-1][j] == ".":
        temp_i -= 1
    
    map[i][j] = "."
    map[temp_i][j] = ROUND_ROCK

def find_north_beam_weight(map):
    total_weight = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == ROUND_ROCK:
                weight = len(map) - i
                total_weight += weight
    
    return total_weight

main()