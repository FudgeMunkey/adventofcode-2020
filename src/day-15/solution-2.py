def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')[:-1]
    clean_data = []

    # Clean Data
    clean_data = [int(n) for n in raw_data[0].split(',')]

    return clean_data


if __name__ == "__main__":
    data = read_input()

    # Solve problem
    tracker = {}

    # Process the input
    for i in range(len(data[:-1])):
        tracker[data[i]] = i + 1

    counter = len(tracker) + 1
    running = True
    current = data[-1]

    while running:
        if current in tracker:
            difference = counter - tracker[current]
            tracker[current] = counter
            current = difference
        else:
            tracker[current] = counter
            current = 0

        counter += 1

        if counter == 30000000:
            print(current)
            running = False

