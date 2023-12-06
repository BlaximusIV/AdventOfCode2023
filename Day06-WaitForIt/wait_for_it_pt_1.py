import time

def calculate_win_path_counts(input):
    time_limit = input[0]
    record = input[1]

    winning_paths = []
    # calculate brute force
    for i in range(1, time_limit - 1):
        movement_speed = i
        movement_time = time_limit - i
        movement_range = movement_speed * movement_time
        if movement_range > record:
            winning_paths.append(i)

    return len(winning_paths)

def main():
    start = time.time()
    input = [(1, 1)]
    results = [calculate_win_path_counts(i) for i in input]

    product = 1
    for i in results:
        product *= i

    print("Winning Paths product: ", product)

    end = time.time()
    print("Time taken: ", end - start)

main()