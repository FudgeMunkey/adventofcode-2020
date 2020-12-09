from itertools import combinations


def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')
    clean_data = []

    # Clean Data
    clean_data = [int(rd) for rd in raw_data[:-1]]

    return clean_data


if __name__ == "__main__":
    data = read_input()

    # Solve problem
    preamble = 25

    for i in range(preamble, len(data)):
        target = data[i]

        comb = combinations(data[i - preamble:i], 2)

        valid = False
        for c in comb:
            if c[0] + c[1] == target:
                valid = True
                break

        if not valid:
            print(f"Bad number is {target}")
            break
