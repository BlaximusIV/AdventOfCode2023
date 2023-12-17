# heavily inspired by https://github.com/hyper-neutrino

import time

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"

def get_viable_combination_count(springs_record, damaged_springs, combination_cache):
    if springs_record == "":
        return 1 if damaged_springs == () else 0
    
    if damaged_springs == ():
        return 0 if DAMAGED in springs_record else 1
    
    cache_key = (springs_record, damaged_springs)
    if cache_key in combination_cache:
        return combination_cache[cache_key]
    
    viable_combination_count = 0

    if springs_record[0] in [OPERATIONAL, UNKNOWN]:
        viable_combination_count += get_viable_combination_count(springs_record[1:], damaged_springs, combination_cache)

    if springs_record[0] in [DAMAGED, UNKNOWN]:
        # the length of the next contiguous damaged springs
        springs_length = damaged_springs[0]
        if springs_length <= len(springs_record) and OPERATIONAL not in springs_record[:springs_length] and (springs_length == len(springs_record) or springs_record[springs_length] != DAMAGED):
            viable_combination_count += get_viable_combination_count(springs_record[springs_length + 1:], damaged_springs[1:], combination_cache)

    combination_cache[cache_key] = viable_combination_count
    return viable_combination_count


def main():
    start = time.time()
    viable_combination_counts = []
    combination_cache = {}
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            record, damaged_springs = line.split()

            # we're unfolding the record 5 times now
            record = "?".join([record] * 5)
            damaged_springs = tuple(map(int, damaged_springs.split(",")))
            damaged_springs *= 5

            viable_combination_counts.append(get_viable_combination_count(record, damaged_springs, combination_cache))

    print(f"Viable combination sum: {sum(viable_combination_counts)}")
    end = time.time()
    print(f"Time taken: {end - start}")

main()
