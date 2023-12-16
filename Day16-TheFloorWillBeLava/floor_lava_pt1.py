import queue
import time

NORTH = "^"
SOUTH = "v"
EAST = ">"
WEST = "<"

class LightBeam:
    def __init__(self, y, x, direction):
        self.y = y
        self.x = x
        self.direction = direction

def main():
    start = time.time()
    with open("input.txt") as f:
        lines = f.readlines()

    tiles = []
    for line in lines:
        tile_row = []
        for char in line.strip():
            tile_row.append(char)
        tiles.append(tile_row)

    light_beams = queue.Queue() 
    light_beams.put(LightBeam(0, 0, EAST))
    energized_tiles = {0:[0]}
    paths = {}
    simulate_light(light_beams, tiles, energized_tiles, paths)
    total_energized_tiles = 0
    for y in energized_tiles:
        total_energized_tiles += len(energized_tiles[y])
    
    print(f"Total energized tiles: {total_energized_tiles}")
    end = time.time()
    print(f"Time elapsed: {end-start}")
    

def simulate_light(light_beams, tiles, energized_tiles, paths):
    while not light_beams.empty():
        light_beam = light_beams.get()

        # check if it's already in a path if so, continue. else, add to path
        if light_beam.y in paths and light_beam.x in paths[light_beam.y]:
            if light_beam.direction in paths[light_beam.y][light_beam.x]:
                continue
        else:
            if light_beam.y not in paths:
                paths[light_beam.y] = {}
            if light_beam.x not in paths[light_beam.y]:
                paths[light_beam.y][light_beam.x] = []
            paths[light_beam.y][light_beam.x].append(light_beam.direction)

        # refactor so we check direction first, then move
        if light_beam.y < 0 or light_beam.y >= len(tiles) or light_beam.x < 0 or light_beam.x >= len(tiles[0]):
            continue

        if light_beam.y not in energized_tiles:
            energized_tiles[light_beam.y] = []

        if light_beam.x not in energized_tiles[light_beam.y]:
            energized_tiles[light_beam.y].append(light_beam.x)

        tile_char = tiles[light_beam.y][light_beam.x]
        if tile_char == ".":
            pass
        elif tile_char == "|":
            if light_beam.direction in [NORTH, SOUTH]:
                pass
            else:
                light_beam.direction = NORTH
                light_beams.put(LightBeam(light_beam.y, light_beam.x, SOUTH))
        elif tile_char == "-":
            if light_beam.direction in [EAST, WEST]:
                pass
            else:
                light_beam.direction = EAST
                light_beams.put(LightBeam(light_beam.y, light_beam.x, WEST))
        elif tile_char == "/":
            if light_beam.direction == NORTH:
                light_beam.direction = EAST
            elif light_beam.direction == SOUTH:
                light_beam.direction = WEST
            elif light_beam.direction == EAST:
                light_beam.direction = NORTH
            elif light_beam.direction == WEST:
                light_beam.direction = SOUTH
        elif tile_char == "\\":
            if light_beam.direction == NORTH:
                light_beam.direction = WEST
            elif light_beam.direction == SOUTH:
                light_beam.direction = EAST
            elif light_beam.direction == EAST:
                light_beam.direction = SOUTH
            elif light_beam.direction == WEST:
                light_beam.direction = NORTH

        # move next, augment direction, add to energized_tiles
        if light_beam.direction == NORTH:
            light_beam.y -= 1
        elif light_beam.direction == SOUTH:
            light_beam.y += 1
        elif light_beam.direction == EAST:
            light_beam.x += 1
        elif light_beam.direction == WEST:
            light_beam.x -= 1
        
        light_beams.put(light_beam)

main()