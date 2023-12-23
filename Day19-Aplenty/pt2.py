class Process_Node:
    def __init__(this, rules, fallback):
        this.rules = rules
        this.fallback = fallback

def main():
    nodes = {}
    with open("input.txt", "r") as f:
        blob = f.read()
        node_txt, _ = blob.split('\n\n')
        for line in node_txt.splitlines():
            name, node = parse_node(line)
            nodes[name] = node

    ranges = { "x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}

    combination_count = count_combinations(nodes, ranges, "in")
    print(combination_count)


def parse_node(node_ln):
    name = node_ln[:node_ln.index("{")]
    rules = node_ln[len(name) + 1:-1].split(",")
    fallback = rules[-1]
    rules = rules[:-1]
    return name, Process_Node(rules, fallback)
                
def count_combinations(nodes, ranges, name):
    if name == "R":
        return 0
    elif name == "A":
        product = 1
        for start, end in ranges.values():
            product *= end - start + 1
        return product
    
    node = nodes[name]

    total = 0

    for rule in node.rules:
        compare, destination = rule.split(":")
        key, comparer, val = compare[0], compare[1], int(compare[2:])
        lo, hi = ranges[key]
        # Find ranges for each
        if comparer == "<":
            T = (lo, min(val - 1, hi))
            F = (max(val, lo), hi)
        else:
            T = (max(val + 1, lo), hi)
            F = (lo, min(val, hi))

        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count_combinations(nodes, copy, destination)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count_combinations(nodes, ranges, node.fallback)

    return total

main()

# Basically we're still traversing the list, but summing the products of each viable range when we reach an 'A' 'node'