def main():
    strings = []
    with open("input.txt") as f:
        strings = f.read().strip("\n").split(",")

    boxes = {}
    for i in range(0, 256):
        boxes[i] = []

    hash_results = []
    for string in strings:
        hash_results.append(get_string_hash(string))
    print(sum(hash_results))

def get_string_hash(string):
    hash = 0
    for i in range(len(string)):
        hash += ord(string[i])
        hash *= 17
        hash = hash % 256
    return hash

main()