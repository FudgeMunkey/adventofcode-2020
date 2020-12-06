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
    people = 0
    alphabet = [0] * 26
    for i in range(len(data)):
        d = data[i]

        if d == '' or i == len(data) - 1:
            valid = [1 if x == people else 0 for x in alphabet]
            print(valid)
            print()

            question_sum += sum(valid)
            alphabet = [0] * 26
            people = 0

            continue

        people += 1
        for c in d:
            alphabet_index = ord(c) - 97
            alphabet[alphabet_index] += 1

        print(d)
        print(alphabet)

    question_sum += sum(alphabet)

    print(question_sum)