import re

class Part:
    def __init__(this, x, m, a, s, status):
        this.x = x
        this.m = m
        this.a = a
        this.s = s
        this.status = status

class Process_Node:
    def __init__(this, name, rules):
        this.name = name
        this.rules = rules

PROCESSING = "P"
ACCEPTED = "A"
REJECTED = "R"

def main():
    nodes = {}
    parts = []
    with open("input.txt", "r") as f:
        blob = f.read()
        node_txt, part_txt = blob.split('\n\n')
        for line in node_txt.splitlines():
            node = parse_node(line)
            nodes[node.name] = node

        for line in part_txt.splitlines():
            parts.append(parse_part(line))

    accepted = []
    for part in parts:
        process_part(nodes, part, accepted)

    total = sum(part.x + part.m + part.a + part.s for part in accepted)
    print(f'Total parts ratings: {total}')

def parse_node(node_ln):
    name = node_ln[:node_ln.index("{")]
    rules = node_ln[len(name) + 1:-1].split(",")
    return Process_Node(name, rules)

def parse_part(part_ln):
    vals = part_ln[1:-1].split(",")
    x,m,a,s = int(vals[0][2:]), int(vals[1][2:]), int(vals[2][2:]), int(vals[3][2:])
    return Part(x,m,a,s, PROCESSING)

def process_part(nodes, part, accepted):
    # Current node
    c = nodes["in"]
    while part.status == PROCESSING:
        for rule in c.rules:
            matches = False
            if ":" in rule:
                criteria, new_node = rule.split(":")
                is_less = "<" in rule
                rating, val = re.split(r'[<>]', criteria)
                val = int(val)
                if is_less:
                    matches = part.x < val if rating == "x" else part.m < val if rating == "m" else part.a < val if rating == "a" else part.s < val
                else:
                    matches = part.x > val if rating == "x" else part.m > val if rating == "m" else part.a > val if rating == "a" else part.s > val
            else:
                if rule == ACCEPTED:
                    part.status = ACCEPTED
                    accepted.append(part)
                elif rule == REJECTED:
                    part.status = REJECTED
                else:
                    c = nodes[rule]
                    
                break

            if matches:
                if new_node == ACCEPTED:
                    part.status = ACCEPTED
                    accepted.append(part)
                elif new_node == REJECTED:
                    part.status = REJECTED
                else:
                    c = nodes[new_node]
                break

                


main()
