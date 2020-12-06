import math

def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.readlines()

    # Clean Data
    pass

    return raw_data


if __name__ == "__main__":
    # Read Input
    data = read_input()
    seat_ids = []

    # Do stuff
    for d in data:
        row_min = 0
        row_max = 128

        # Get Row
        for i in range(7):
            row_range = row_max - row_min

            if d[i] == 'F':
                row_max -= row_range / 2
            else:
                row_min += row_range / 2

        # Get column
        col_min = 0
        col_max = 8
        for i in range(7, len(d)):
            col_range = col_max - col_min

            if d[i] == 'L':
                col_max -= col_range / 2
            else:
                col_min += col_range / 2

        row = row_min
        col = math.floor(col_min)

        seat_ids.append(row * 8 + col)

    # Generate all IDs
    all_ids = []
    for row_id in range(16, 112):
        for col_id in range(8):
            all_ids.append(row_id * 8 + col_id)

    missing_id = []
    for s in all_ids:

        if s in seat_ids:
            continue
        else:
            missing_id.append(s)

    for mid in missing_id:
        if mid + 1 in seat_ids and mid - 1 in seat_ids:
            print(mid)
