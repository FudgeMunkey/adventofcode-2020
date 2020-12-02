# The idea is essentially the same as solution-1. Split the list into two lists: low
# and high. The separating point is TARGET / 2. This means the possible combinations
# to reach target are (3L) or (2L, 1H). The case 3L can also be split into two lists:
# low and high and summed in the same way (2L, 1H). This means the comparison
# function is actually the same for both cases.

import sys

TARGET = 2020


def check(low, high):
    for i in low:
        for j in low:
            if i == j:
                # Skip the same value (assume no duplicates)
                continue

            for k in high:
                my_sum = i + j + k

                if my_sum > TARGET:
                    # Summing more values in the high list are guaranteed to be > TARGET
                    break
                elif my_sum == TARGET:
                    print(f"Three values are {i} * {j} * {k} = {i * j * k}")
                    sys.exit(0)


def split_data(data, split_point):
    low = []
    high = []
    for d in data:
        if d < split_point:
            low.append(d)
        else:
            high.append(d)

    return low, high


if __name__ == "__main__":
    # Read in file and clean data
    f = open("puzzle_input.txt", "r")
    data = f.readlines()
    data = [int(x) for x in data]

    # Sort the list
    data.sort()

    # Split into low and high
    low, high = split_data(data, TARGET / 2)

    # You can either get (3L) or (2L, 1H) to make the target.
    # Check for 3L first
    low_low, low_high = split_data(data, TARGET // 3)
    check(low_low, low_high)

    # Check for 2L, 1H
    check(low, high)
