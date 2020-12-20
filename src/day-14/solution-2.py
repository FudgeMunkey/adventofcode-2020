from itertools import product


def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')[:-1]
    clean_data = []

    # Clean Data
    clean_data = raw_data

    return clean_data


def apply_mask(value, mask):
    # Apply the masks, carry over the Xs
    first_pass = ''.join(
        [value[i] if mask[i] == '0' else mask[i] for i in range(len(value))]
    )

    # Substitute the X values in the masks
    num = mask.count('X')
    subs = product([0, 1], repeat=num)
    binary_values = []

    # Substitute the Xs for all combinations of 1s and 0s
    for s in subs:
        temp_mask = first_pass
        for i in range(len(s)):
            temp_mask = temp_mask.replace('X', str(s[i]), 1)
        binary_values.append(temp_mask)

    return binary_values


if __name__ == "__main__":
    data = read_input()

    # Solve problem
    current_mask = ""
    memory = {}
    for index in range(len(data)):
        d = data[index]
        if "mask" in d:
            # Extract mask
            current_mask = data[index].split(' = ')[1]
        else:
            # Put value in memory
            binary_location = format(int(d[d.index('[') + 1: d.index(']')]), "b").zfill(36)
            write_value = int(d.split(' = ')[1])

            locations = apply_mask(binary_location, current_mask)
            for bin_loc in locations:
                loc = int(bin_loc, 2)
                memory[loc] = write_value

    total_sum = 0
    for k, v in memory.items():
        total_sum += v

    print(f"Total sum is {total_sum}")
