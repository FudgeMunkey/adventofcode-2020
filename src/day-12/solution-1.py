def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')[:-1]
    clean_data = []

    # Clean Data
    clean_data = raw_data

    return clean_data


if __name__ == "__main__":
    data = read_input()

    # Solve problem
    coords = [0, 0]
    direction = 90

    # Go through each instruction
    for row in data:
        instruction = row[0]
        value = int(row[1:])

        if instruction == 'N':
            coords[1] += value
        elif instruction == 'S':
            coords[1] -= value
        elif instruction == 'E':
            coords[0] += value
        elif instruction == 'W':
            coords[0] -= value
        elif instruction == 'L':
            direction -= value
            direction %= 360
        elif instruction == 'R':
            direction += value
            direction %= 360
        elif instruction == 'F':
            if direction == 0:
                coords[1] += value
            elif direction == 180:
                coords[1] -= value
            elif direction == 90:
                coords[0] += value
            elif direction == 270:
                coords[0] -= value

    print(f"Manhattan distance is {sum([abs(c) for c in coords])}")











