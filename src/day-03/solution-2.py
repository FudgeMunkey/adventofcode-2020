def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.readlines()
    clean_data = [x[:-1] for x in raw_data]  # Remove \n char

    return clean_data


def check_slope(right, down):
    # Iterate through each row (down)
    # Move the index across RIGHT each time (right)
    trees = 0
    index = 0
    for i in range(down, len(data), down):
        d = data[i]

        index += right
        index = index % len(d)

        if d[index] == "#":
            trees += 1

    return trees


if __name__ == "__main__":
    # Read in data
    data = read_input()

    check_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res = 1

    for check in check_list:
        num_trees = check_slope(check[0], check[1])
        print(f"Number of trees for {check} is {num_trees}")
        res *= num_trees

    print(f"Result {res}")
