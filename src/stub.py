def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')
    clean_data = []

    # Clean Data
    clean_data = raw_data[:-1]

    return clean_data


if __name__ == "__main__":
    data = read_input()

    # Solve problem
    for i in range(len(data)):
        pass