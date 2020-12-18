# This currently works for small inputs, not for the puzzle input though..
# Probably needs to be optimised.. Don't want to run it for 3 days..

def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')[:-1]

    departure_time = int(raw_data[0])
    ids = [int(d) if d != 'x' else -1 for d in raw_data[1].split(',')]

    return departure_time, ids


def check_offsets(ids, curr_time):
    correct_time = curr_time

    for i in range(len(ids)):
        if ids[i] == -1:
            continue

        if (curr_time + i) % ids[i] != 0:
            return -1

    return correct_time


if __name__ == "__main__":
    ideal_departure, bus_ids = read_input()

    time_jump = max(bus_ids)
    current_time = time_jump * (100000000000000 // time_jump)
    found_time = -1

    while True:
        start_time = current_time - bus_ids.index(time_jump)
        found_time = check_offsets(bus_ids, start_time)
        if found_time != -1:
            break

        current_time += time_jump

    print(f"Earliest time stamp is {found_time}")
