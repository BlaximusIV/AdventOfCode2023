class Lens:
    def __init__(self, label, length):
        self.label = label
        self.length = length

def main():
    strings = []
    with open("input.txt") as f:
        strings = f.read().strip("\n").split(",")

    boxes = {}
    for i in range(0, 256):
        boxes[i] = []

    for string in strings:
        organize_lens(string, boxes)

    focusing_powers = get_focusing_power(boxes)
    print(sum(focusing_powers))

def organize_lens(string, boxes):
    label = None

    parts = string.split("=")
    if len(parts) == 2:
        label = parts[0]
        length = int(parts[1])
        box_number = get_string_hash(label)
        add_or_replace_lens(boxes, label, box_number, length)

    else:
        label = string.strip("-")
        box_number = get_string_hash(label)
        remove_lens(boxes, label, box_number)

def get_string_hash(string):
    hash = 0
    for i in range(len(string)):
        hash += ord(string[i])
        hash *= 17
        hash = hash % 256
    return hash

def remove_lens(boxes, label, box_number):
    for i in range(len(boxes[box_number])):
        if boxes[box_number][i].label == label:
            boxes[box_number].pop(i)
            return

def add_or_replace_lens(boxes, label, box_number, length):
    for i in range(len(boxes[box_number])):
        if boxes[box_number][i].label == label:
            boxes[box_number][i].length = length
            return
        
    boxes[box_number].append(Lens(label, length))

def get_focusing_power(boxes):
    focusing_powers = []
    for i in range(0, 256):
        for j in range(len(boxes[i])):
            focusing_powers.append((1 + i) * (j + 1) * boxes[i][j].length)

    return focusing_powers

main()