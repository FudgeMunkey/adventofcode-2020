# The idea is that you split the list into two lists: low and high. The separating
# point is TARGET / 2. This reduces the number of comparisons as two numbers in the
# high list will always be > TARGET, so they never need to be compared. The price of
# comparison is much more expensive that the price of sorting the list.

import sys

TARGET = 2020

if __name__ == "__main__":
    # Read in file and clean data
    f = open("puzzle_input.txt", "r")
    data = f.readlines()
    data = [int(x) for x in data]

    # Sort the list
    data.sort()

    # Split into low and high
    low = []
    high = []
    for d in data:
        if d < TARGET / 2:
            low.append(d)
        else:
            high.append(d)

    # Compare the low list against the high list
    for l in low:
        for h in high:
            my_sum = l + h

            if my_sum > TARGET:
                # Summing more values in the high list are guaranteed to be > TARGET
                break
            elif my_sum == TARGET:
                print(f"Two values are {l} * {h} = {l * h}")
                sys.exit(0)
