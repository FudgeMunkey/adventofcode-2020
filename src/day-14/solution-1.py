def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')[:-1]
    clean_data = []

    # Clean Data
    clean_data = raw_data

    return clean_data


def apply_mask(value, mask):
    # Apply mask and convert binary string back to decimal
    ret_value = [value[i] if mask[i] == 'X' else mask[i] for i in range(len(value))]
    ret_value = int(''.join(ret_value), 2)
    return ret_value


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
            location = d[d.index('[') + 1: d.index(']')]
            binary_value = format(int(d.split(' = ')[1]), "b").zfill(36)

            memory[location] = apply_mask(binary_value, current_mask)

    total_sum = 0
    for k, v in memory.items():
        total_sum += v

    print(f"Total sum is {total_sum}")
