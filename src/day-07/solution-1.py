def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')
    clean_data = []

    # Clean Data
    clean_data = raw_data[:-1]

    return clean_data


def process_rules(rules):
    ret_rules = {}

    # Process all of the rules
    for i in range(len(rules)):
        rule = rules[i]

        root_bag = rule.split(' contain ')[0][:-5]
        raw_stored_bags = rule.split(' contain ')[1].split(', ')

        # Check for empty bag
        if raw_stored_bags[0] == "no other bags.":
            raw_stored_bags = []

        # Process stored bags
        stored_bags = []
        for raw_bag in raw_stored_bags:
            stored_bags.append(raw_bag.split(' ')[1] + ' ' + raw_bag.split(' ')[2])

        ret_rules[root_bag] = stored_bags

    return ret_rules


if __name__ == "__main__":
    data = read_input()

    # Process rules
    bag_rules = process_rules(data)

    # Solve
    solution_list = [False] * len(bag_rules)
    key_list = list(bag_rules.keys())
    target_index = key_list.index("shiny gold")
    solution_list[target_index] = True

    # Go through bag rules n times
    for count in range(len(bag_rules)):

        # Go through bag rules and check if stored bags contain the shiny gold bag
        for bag in bag_rules:
            stored = bag_rules[bag]

            # Go through each stored bag
            for stored_bag in stored:
                if solution_list[key_list.index(stored_bag)]:
                    solution_list[key_list.index(bag)] = True
                    break

    print(f"The total number of bags that will eventually contain a shiny gold bag is {sum(solution_list) - 1}")
