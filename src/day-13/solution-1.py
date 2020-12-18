def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')[:-1]

    departure_time = int(raw_data[0])
    ids = [int(d) for d in raw_data[1].split(',') if d != 'x']

    return departure_time, ids


if __name__ == "__main__":
    ideal_departure, bus_ids = read_input()

    current_time = ideal_departure
    found = False
    bus_time = 0
    bus_id = 0
    while not found:
        for bid in bus_ids:
            if current_time % bid == 0:
                bus_time = current_time
                bus_id = bid
                found = True

        current_time += 1

    print(f"Result is {bus_id * (bus_time - ideal_departure)}")
