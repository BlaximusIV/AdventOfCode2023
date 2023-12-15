
def main():
    strings = []
    with open("input.txt") as f:
        strings = f.read().strip("\n").split(",")

    hash_values = []
    for string in strings:
        hash_values.append(get_string_hash(string))

    print(sum(hash_values))


def get_string_hash(string):
    hash = 0
    for i in range(len(string)):
        hash += ord(string[i])
        hash *= 17
        hash = hash % 256
    return hash

main()