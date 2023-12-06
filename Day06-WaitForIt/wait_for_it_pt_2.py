import time

def calculate_win_path_counts(input):
    time_limit = input[0]
    record = input[1]

    min_time = find_min_winning_time(time_limit, record)
    max_time = find_max_winning_time(time_limit, record)

    return max_time - min_time + 1

def is_win(movement_speed, time_limit, record):
    movement_time = time_limit - movement_speed
    movement_range = movement_speed * movement_time
    return movement_range > record

def find_min_winning_time(time_limit, record):
    min_time = 1
    max_time = time_limit - 1
    while min_time < max_time:
        mid_time = (min_time + max_time) // 2
        if is_win(mid_time, time_limit, record):
            max_time = mid_time
        else:
            min_time = mid_time + 1
    return min_time

def find_max_winning_time(time_limit, record):
    min_time = 1
    max_time = time_limit - 1
    while min_time < max_time:
        mid_time = (min_time + max_time + 1) // 2
        if is_win(mid_time, time_limit, record):
            min_time = mid_time
        else:
            max_time = mid_time - 1
    return min_time

def main():
    start = time.time()
    input = (1, 1)
    
    win_count = calculate_win_path_counts(input)

    print("Winning Paths Count: ", win_count)

    end = time.time()
    print("Time taken: ", end - start)

main()