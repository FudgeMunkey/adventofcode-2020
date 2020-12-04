def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.readlines()
    clean_data = [x[:-1] for x in raw_data]  # Remove \n char

    return clean_data


if __name__ == "__main__":
    # Read in data
    data = read_input()

    # Iterate through each row (down 1)
    # Move the index across 3 each time (right 3)
    trees = 0
    index = 0
    for d in data[1:]:
        index += 3
        index = index % len(d)

        if d[index] == "#":
            trees += 1

    print(f"Number of trees is {trees}")
