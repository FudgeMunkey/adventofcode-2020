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
    target = 1639024365
    max_index = data.index(target)

    for i in range(max_index):
        check_list = data[i:max_index]

        running_sum = 0
        running_list = []
        for n in check_list:
            running_sum += n
            running_list.append(n)

            if running_sum == target:
                print(f"Encryption weakness is {min(running_list) + max(running_list)}")
            elif running_sum > target:
                break
