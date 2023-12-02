import re

CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

POSSIBLE_GAMES = []
# Check if any of the drawings are possible. If none of the drawn results are impossible, return the game id. It is not possible to draw more cubes of a color than what is stipulated in the cubes dict.
def process_line(line):
    drawing_possible = True
    game_id = re.search(r'Game (\d+)', line).group(1)
    line = re.sub(r'Game \d+: ', '', line)
    drawings = line.split(';')
    for drawing in drawings:
        cubes = drawing.split(', ')
        if not drawing_possible:
            break
        for cube in cubes:
            cube_count, cube_color = cube.strip().split(' ')
            if int(cube_count) > CUBES[cube_color]:
                drawing_possible = False
                break

    if drawing_possible:
        return int(game_id)
    else:
        return 0

with open("input.txt") as input:
    for line in input:
        POSSIBLE_GAMES.append(process_line(line.rstrip('\n')))

print(f"Sum of possible game ids: {sum(POSSIBLE_GAMES)}")