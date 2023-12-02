import re

GAME_POWERS = []
def process_line(line):
    needed_cubes = {"red": 1, "green": 1, "blue": 1}
    cube_drawings = re.findall(r'\d+ \w+', line)
    for drawing in cube_drawings:
        cube_count, cube_color = drawing.split(' ')
        if int(cube_count) > needed_cubes[cube_color]:
            needed_cubes[cube_color] = int(cube_count)
    
    return needed_cubes["red"] * needed_cubes["green"] * needed_cubes["blue"]

with open("input.txt") as input:
    for line in input:
        GAME_POWERS.append(process_line(line.rstrip('\n')))

print(f"Sum of game powers: {sum(GAME_POWERS)}")