# The idea is essentially the same as solution-1. Split the list into two lists: low
# and high. The separating point is TARGET / 2. This means the possible combinations
# to reach target are (3L) or (2L, 1H). The case 3L can also be split into two lists:
# low and high and summed in the same way (2L, 1H). This means the comparison
# function is actually the same for both cases.

import sys

TARGET = 2020


def check(low_list, high_list):
    for i in low_list:
        for j in low_list:
            if i == j:
                # Skip the same value (assume no duplicates)
                continue

            for k in high_list:
                my_sum = i + j + k

                if my_sum > TARGET:
                    # Summing more values in the high list are guaranteed to be > TARGET
                    break
                elif my_sum == TARGET:
                    print(f"Three values are {i} * {j} * {k} = {i * j * k}")
                    sys.exit(0)


def split_data(data_list, split_point):
    low_list = []
    high_list = []
    for d in data_list:
        if d < split_point:
            low_list.append(d)
        else:
            high_list.append(d)

    return low_list, high_list


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
