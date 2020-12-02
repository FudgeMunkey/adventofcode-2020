def check_password(policy):
    # Split policy/password
    initial_split = policy.split(':')
    policy_split = initial_split[0].split(' ')

    first_index = int(policy_split[0].split('-')[0]) - 1
    second_index = int(policy_split[0].split('-')[1]) - 1
    pass_char = policy_split[1]
    password = initial_split[1].strip()

    if (password[first_index] == pass_char and not password[second_index] == pass_char) \
            or (password[second_index] == pass_char and not password[first_index] == pass_char):
        return True
    else:
        return False


if __name__ == "__main__":
    # Read input
    f = open("puzzle_input.txt", "r")
    data = f.readlines()

    valid_passwords = 0

    # Process
    for d in data:
        if check_password(d.strip()):
            valid_passwords += 1

    print(valid_passwords)
