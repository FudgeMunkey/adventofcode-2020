def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')
    clean_data = []

    # Clean Data
    clean_data = raw_data[:-1]

    return clean_data


if __name__ == "__main__":
    data = read_input()

    # Solve problem
    accumulator = 0

    running = True
    instruction_pointer = 0
    run_before = [False] * len(data)
    steps = 0
    while running:
        steps += 1

        if steps > 10000:
            break

        line = data[instruction_pointer]

        instruction = line.split(' ')[0]
        value = int(line.split(' ')[1])

        if run_before[instruction_pointer]:
            break
        else:
            run_before[instruction_pointer] = True

        if instruction == "acc":
            accumulator += value
            instruction_pointer += 1
        elif instruction == "jmp":
            instruction_pointer += value
        elif instruction == "nop":
            instruction_pointer += 1

        if instruction_pointer == len(data):
            break

    print(accumulator)