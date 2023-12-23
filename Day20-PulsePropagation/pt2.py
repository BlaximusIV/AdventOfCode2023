from collections import namedtuple
from queue import Queue
import math

BROADCASTER = "broadcaster"
OUTPUT = "output"

Pulse = namedtuple('Pulse', ['source', 'frequency', 'destination'])

class Node:
    def __init__(self, name, type, state, destinations):
        self.name = name
        self.type = type
        self.state = state
        self.destinations = destinations

def main():
    nodes = {}
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            node_name, node = parse_node(line)
            nodes[node_name] = node
    
    populate_conjunction_states(nodes)

    (final_feed,) = [name for name, node in nodes.items() if "rx" in node.destinations]
    count = find_btn_count(nodes, final_feed)
    print(f'Lowest button count to low rx: {count}')

def parse_node(line):
    node, destinations = line.split(" -> ")
    destinations = destinations.strip("\n")

    node_type = BROADCASTER if node == BROADCASTER else node[0]
    node_name = BROADCASTER if node_type == BROADCASTER else node[1:]

    destinations = destinations.split(", ")

    state = False if node_type == "%" else {} if node_type == "&" else None

    return node_name, Node(node_name, node_type, state, destinations)

def populate_conjunction_states(nodes):
    for i in nodes.values():
        if i.type == "&":
            for j in nodes.values():
                if j.name == i.name:
                    continue
                if i.name in j.destinations:
                    i.state[j.name] = 0 


# TODO: Try seeing how often the nodes leading to rx have the necessary input
def find_btn_count(nodes, target_name):
    seen_counts = { name: 0 for name, node in nodes.items() if target_name in node.destinations}
    cycles = {}
    q = Queue()
    button_count = 0
    while True:
        button_count += 1
        q.put(Pulse("btn", 0, BROADCASTER))
        while not q.empty():
            pulse = q.get()
            
            if not pulse.destination in nodes:
                continue

            node = nodes[pulse.destination]

            if node.name == target_name and pulse.frequency == 1:
                seen_counts[pulse.source] += 1

                if pulse.source not in cycles:
                    cycles[pulse.source] = button_count
                
                if all(seen_counts.values()):
                    x = 1
                    for cycle in cycles.values():
                        x = x * cycle // math.gcd(x, cycle)
                    return x

            # if node is broadcaster
            if node.type == BROADCASTER:
                for dest in node.destinations:
                    q.put(Pulse(BROADCASTER, 0, dest))
            elif node.type == "%":
                if pulse.frequency == 0:
                    node.state = not node.state
                    for d in node.destinations:
                        frequency = 1 if node.state else 0
                        q.put(Pulse(node.name, frequency, d))            
            else: # is & type
                node.state[pulse.source] = pulse.frequency
                all_high = all(x == 1 for x in node.state.values())
                for d in node.destinations:
                    frequency = 0 if all_high else 1
                    q.put(Pulse(node.name, frequency, d))
            

main()
