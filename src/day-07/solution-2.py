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
            stored_bag_num = int(raw_bag.split(' ')[0])
            stored_bag_name = raw_bag.split(' ')[1] + ' ' + raw_bag.split(' ')[2]
            stored_bags.append((stored_bag_name, stored_bag_num))

        ret_rules[root_bag] = stored_bags

    return ret_rules


def count_bags(rules, bag):
    if not rules[bag]:
        return 0
    else:
        stored_num = [num for (name, num) in rules[bag]]

        return sum(stored_num[i] + stored_num[i] * count_bags(rules, rules[bag][i][0]) for i in range(len(stored_num)))


if __name__ == "__main__":
    data = read_input()

    # Process rules
    bag_rules = process_rules(data)

    # Solve
    number_of_bags = count_bags(bag_rules, "shiny gold")
    print(f"The total number of bags is {number_of_bags}")
