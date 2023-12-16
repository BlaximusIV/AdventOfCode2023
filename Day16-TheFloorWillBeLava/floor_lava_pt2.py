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


    energized_tile_counts = []
    light_beams = get_start_beams(tiles)
    for light_beam in light_beams:
        energized_tile_counts.append(get_energized_tile_count(light_beam, tiles))
        
    print(f"Greatest number of energized tiles: {max(energized_tile_counts)}")
    end = time.time()
    print(f"Time elapsed: {end-start}")

def get_start_beams(tiles):
    start_beams = []
    for x in range(len(tiles[0])):
        start_beams.append(LightBeam(0, x, SOUTH))
        start_beams.append(LightBeam(len(tiles)-1, x, NORTH))

    for y in range(len(tiles)):
        start_beams.append(LightBeam(y, 0, EAST))
        start_beams.append(LightBeam(y, len(tiles[0])-1, WEST))

    return start_beams

def get_energized_tile_count(start_beam, tiles):
    energized_tiles = {start_beam.y:[start_beam.x]}
    paths = {}
    light_beams = queue.Queue()
    light_beams.put(start_beam)
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

    total_energized_tiles = 0
    for y in energized_tiles:
        total_energized_tiles += len(energized_tiles[y])

    return total_energized_tiles

main()