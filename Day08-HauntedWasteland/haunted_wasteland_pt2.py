from math import gcd
import re
import time

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

def parse_line(line, nodes_map, a_nodes):
    node_vals = re.findall(r'([0-9A-Z]{3})', line)
    node = Node(node_vals[0], node_vals[1], node_vals[2])
    nodes_map[node_vals[0]] = node

    if node.name[-1] == 'A':
        a_nodes.append(node)

def get_next_node(nodes_map, current_node, instructions, steps):
    if instructions[steps % len(instructions)] == 'L':
        return nodes_map[current_node.left]
    else:
        return nodes_map[current_node.right]

def get_cycle_length(nodes_map, instructions, a_node):
    steps = 0
    current_node_name = a_node.name
    while not current_node_name[-1] == 'Z':
        current_node_name = get_next_node(nodes_map, nodes_map[current_node_name], instructions, steps).name
        steps += 1

    return steps

def get_least_common_multiple(cycle_lengths):
    lcm = cycle_lengths[0]
    for i in cycle_lengths[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def main():
    start = time.time()
    with open ('input.txt', 'r') as f:
        lines = f.readlines()
        instructions = lines[0].strip()

        nodes_directions = lines[2:]
        nodes_map = {}
        a_nodes = []
        for node in nodes_directions:
            parse_line(node, nodes_map, a_nodes)

    cycle_lengths = []
    for a_node in a_nodes:
        cycle_lengths.append(get_cycle_length(nodes_map, instructions, a_node))
    
    print(f'Cycle Lengths: {cycle_lengths}')

    lcm = get_least_common_multiple(cycle_lengths)
    print(f'Least Common Multiple: {lcm}')

    end = time.time()
    print(f'Time Elapsed: {end-start}')

main()
