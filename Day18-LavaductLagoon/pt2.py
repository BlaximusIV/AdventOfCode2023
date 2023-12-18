from collections import namedtuple

Coord = namedtuple("Coord", ["y", "x"])

def main():
    data = None
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    vertices = [Coord(0, 0)]
    perimeter_length = 0
    for instruction in data:
        _, _, hex_string = instruction.split(" ")
        hex_string = hex_string[1:-1]
        direction = get_direction(hex_string[-1])
        distance = int(hex_string[1:-1], 16)
        perimeter_length += distance
        previous_vertex = vertices[-1]

        new_vertex = (Coord(previous_vertex.y, previous_vertex.x + distance) if direction == "R" 
                    else Coord(previous_vertex.y, previous_vertex.x - distance) if direction == "L" 
                    else Coord(previous_vertex.y + distance, previous_vertex.x) if direction == "D" 
                    else Coord(previous_vertex.y - distance, previous_vertex.x))
        
        vertices.append(new_vertex)
    
    
    # Shoelace formula
    sum = 0
    for i in range(len(vertices) - 1):
        next_y = vertices[i + 1].y if i + 1 < len(vertices) else vertices[-1].y
        last_y = vertices[i - 1].y if i - 1 >= 0 else vertices[-1].y
        sum += vertices[i].x * (next_y - last_y)

    sum = abs(sum // 2) 
    print(f"Total area: {sum + perimeter_length // 2 + 1}")

def get_direction(char):
    return ("R" if char == "0" else "D" if char == "1" else "L" if char == "2" else "U")

main()