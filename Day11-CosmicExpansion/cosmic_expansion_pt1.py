

def main():
    galaxy_map = []
    galaxies = {}
    galaxies_x = {}
    with open("test_input.txt") as f:
        input = f.readlines()
        for i in range(len(input)):
            line = input[i].strip("\n")
            galaxy_map.append(line)
            for j in range(len(line)):
                if line[j] == "#":
                    if i not in galaxies:
                        galaxies[i] = []
                    galaxies[i].append(j)
                    galaxies_x[j] = 1
    
    # find the rows that have no galaxies, and insert another row of '.'s
    for i in range(len(galaxy_map)):
        if i not in galaxies:
            galaxy_map.insert(i, "." * len(galaxy_map[0]))

    # find the columns that have no galaxies, and insert another column of '.'s
    for i in range(len(galaxy_map[0])):
        if i not in galaxies_x:
            for j in range(len(galaxy_map)):
                galaxy_map[j] = galaxy_map[j][:i] + "." + galaxy_map[j][i:]

    #adjust the galaxies dictionary to account for the new rows and columns
    galaxies = {}
    for i in range(len(galaxy_map)):
        for j in range(len(galaxy_map[i])):
            if galaxy_map[i][j] == "#":
                if i not in galaxies:
                    galaxies[i] = []
                galaxies[i].append(j)

    # Print the new galaxy map
    for line in galaxy_map:
        print(line)


main()