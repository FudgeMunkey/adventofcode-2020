
def check_password(policy):
    # Split policy/password
    initial_split = policy.split(':')
    policy_split = initial_split[0].split(' ')

    min_num = int(policy_split[0].split('-')[0])
    max_num = int(policy_split[0].split('-')[1])
    pass_char = policy_split[1]
    password = initial_split[1].strip()

    char_count = password.count(pass_char)

    if min_num <= char_count <= max_num:
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