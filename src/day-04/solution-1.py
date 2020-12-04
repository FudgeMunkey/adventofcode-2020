def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.readlines()

    return raw_data


def check_valid(my_passport):
    check_dict = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
    }

    for field in my_passport:
        field_name = field.split(':')[0]

        if field_name in check_dict:
            check_dict[field_name] = True

    return all(check_dict.values())


if __name__ == "__main__":
    # Read Input
    data = read_input()

    # Extract passports
    passports = []
    passport = []
    for line in data:
        # Passport done
        if line == '\n':
            passports.append(passport)
            passport = []
            continue

        s = line.split(' ')
        passport.extend(s)

    passports.append(passport)

    # Check if passports are valid
    total_valid = 0
    for p in passports:
        if check_valid(p):
            total_valid += 1

    print(f"There are {total_valid} valid passports.")
