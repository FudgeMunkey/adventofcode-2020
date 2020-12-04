def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.readlines()

    return raw_data


def check_valid(my_passport):
    # Dictionary of possible valid values for each field
    valid_values = {
        "byr": range(1920, 2003),
        "iyr": range(2010, 2021),
        "eyr": range(2020, 2031),
        "hgt-cm": range(150, 194),
        "hgt-in": range(59, 77),
        "hcl": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],
        "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": [1, 1000000000],
    }

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
        field_value = field.split(':')[1].strip()

        print(f"Pair: {field_name} {field_value}")

        if field_name in ["byr", "iyr", "eyr"]:
            # Convert to int, check if it's in the ranges
            field_value = int(field_value)

            if field_value in valid_values[field_name]:
                check_dict[field_name] = True

        elif field_name == "hgt":
            # Convert to int, check if it's in the cm/in ranges
            if field_value[-2:] not in ["cm", "in"]:
                continue

            check_key = field_name + '-' + field_value[-2:]
            field_value = int(field_value[:-2])

            if field_value in valid_values[check_key]:
                check_dict[field_name] = True

        elif field_name == "hcl":
            # Check if # is at the start, check if each char is valid
            if field_value[0] != '#' or len(field_value) != 7:
                continue

            hcl_valid = True
            for c in field_value[1:]:
                if c not in valid_values[field_name]:
                    hcl_valid = False
                    break

            check_dict[field_name] = hcl_valid

        elif field_name == "ecl":
            # Check eye colour is valid
            if field_value in valid_values[field_name]:
                check_dict[field_name] = True

        elif field_name == "pid":
            # Check if 9 digits and a number
            if len(field_value) != 9:
                continue

            if valid_values[field_name][0] <= int(field_value) <= valid_values[field_name][1]:
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
