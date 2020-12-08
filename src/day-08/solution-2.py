def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')
    clean_data = []

    # Clean Data
    clean_data = raw_data[:-1]

    return clean_data


def run_program(instructions):
    # Solve problem
    accumulator = 0

    running = True
    instruction_pointer = 0
    run_before = [False] * len(data)
    steps = 0
    while running:
        steps += 1

        if steps > 100000:
            print(steps)
            return False

        line = instructions[instruction_pointer]

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
            print(accumulator)
            return True



if __name__ == "__main__":
    data = read_input()

    for i in range(len(data)):
        new_instructions = data.copy()

        instruction = new_instructions[i].split(' ')[0]
        value = int(new_instructions[i].split(' ')[1])

        new_command = ""

        if instruction == "jmp":
            new_command = f"nop {value}"
        elif instruction == "nop":
            new_command = f"jmp {value}"
        else:
            new_command = f"{instruction} {value}"

        new_instructions[i] = new_command

        run_program(new_instructions)
