import re
import time

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

def get_node(line, nodes_map):
    node_vals = re.findall(r'([A-Z]{3})', line)
    node = Node(node_vals[0], node_vals[1], node_vals[2])
    nodes_map[node_vals[0]] = node

def get_node_steps(nodes_map, instructions):
    steps = 0
    current_node = nodes_map['AAA']
    destination_node = 'ZZZ'

    while current_node.name != destination_node:
        if instructions[steps % len(instructions)] == 'L':
            current_node = nodes_map[current_node.left]
        else:
            current_node = nodes_map[current_node.right]
        steps += 1

    return steps

def main():
    start = time.time()
    with open ('input.txt', 'r') as f:
        lines = f.readlines()
        instructions = lines[0].strip()

        nodes_directions = lines[2:]
        nodes_map = {}
        for node in nodes_directions:
            get_node(node, nodes_map)

    steps = get_node_steps(nodes_map, instructions)

    print(f'Steps to destination: {steps}')
    end = time.time()
    print(f'Time Elapsed: {end-start}')

main()
