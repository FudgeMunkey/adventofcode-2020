# NOT DONE
# This works for smaller puzzle input files but never finishes on the big one..

counter = 0

def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')[:-1]
    clean_data = []

    # Clean Data
    clean_data = [int(rd) for rd in raw_data]

    return clean_data


def check(data_list, index):
    if len(data_list) - 1 == index:
        return data_list[index] - data_list[0] <= 3
    else:
        return False


def tarverse_tree(data_list):
    if len(data_list) == 1:
        global counter
        counter += 1
        return
    else:
        for i in range(1, 4):
            if check(data_list[:i + 1], i):
                tarverse_tree(data_list[i:])

if __name__ == "__main__":
    data = read_input()
    data.sort()

    # Solve problem
    target = data[-1] + 3
    data.insert(0, 0)

    tarverse_tree(data)
    print(f"Number of valid adapter combinations is {counter}")

