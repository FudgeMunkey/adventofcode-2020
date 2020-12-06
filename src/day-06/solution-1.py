def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.readlines()
    clean_data = []

    # Clean Data
    for rd in raw_data:
        clean_data.append(rd.strip())

    return clean_data


if __name__ == "__main__":
    data = read_input()

    question_sum = 0
    alphabet = [0] * 26
    for d in data:
        if d == '':
            question_sum += sum(alphabet)
            alphabet = [0] * 26

        for c in d:
            alphabet_index = ord(c) - 97

            if alphabet[alphabet_index] == 0:
                alphabet[alphabet_index] += 1

    question_sum += sum(alphabet)

    print(question_sum)
