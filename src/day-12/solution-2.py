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
    ship_coords = [0, 0]
    waypoint_coords = [10, 1]

    # Go through each instruction
    for row in data:
        # Get instruction and value
        instruction = row[0]
        value = int(row[1:])

        # Parse the instruction
        if instruction == 'N':
            waypoint_coords[1] += value
        elif instruction == 'S':
            waypoint_coords[1] -= value
        elif instruction == 'E':
            waypoint_coords[0] += value
        elif instruction == 'W':
            waypoint_coords[0] -= value
        elif instruction == 'L' and value == 90 or instruction == 'R' and value == 270:
            # Rotate waypoint left once or right 3 times
            waypoint_coords = [-waypoint_coords[1], waypoint_coords[0]]
        elif instruction == 'L' and value == 270 or instruction == 'R' and value == 90:
            # Rotate waypoint left 3 times or right once
            waypoint_coords = [waypoint_coords[1], -waypoint_coords[0]]
        elif (instruction == 'L' or instruction == 'R') and value == 180:
            # Rotate twice either direction
            waypoint_coords = [-x for x in waypoint_coords]
        elif instruction == 'F':
            ship_coords = [ship_coords[0] + waypoint_coords[0] * value, ship_coords[1] + waypoint_coords[1] * value]

    print(f"Manhattan distance is {sum([abs(c) for c in ship_coords])}")












