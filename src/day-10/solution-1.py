def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')[:-1]
    clean_data = []

    # Clean Data
    clean_data = [int(rd) for rd in raw_data]

    return clean_data


if __name__ == "__main__":
    data = read_input()
    data.sort()

    # Solve problem
    differences = [0] * 4
    last = 0
    for i in range(len(data)):
        d = data[i]

        diff = d - last
        differences[diff] += 1

        last = d

    differences[3] += 1

    print(f"Result is {differences[1] * differences[3]}")
