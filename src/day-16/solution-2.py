# It doesn't work, I'm not sure why not..

def read_input():
    # Read input
    f = open("puzzle_input.txt", "r")
    raw_data = f.read().split('\n')[:-1]
    clean_data = []

    # Extract fields
    clean_data = raw_data

    return clean_data


def extract_fields(input_data):
    fields = {}
    for row in input_data:
        if row == '':
            break

        field_name = row.split(':')[0]
        range1 = row.split(':')[1].split(' or ')[0]
        range1 = range(int(range1.split('-')[0]), int(range1.split('-')[1]) + 1)
        range2 = row.split(':')[1].split(' or ')[1]
        range2 = range(int(range2.split('-')[0]), int(range2.split('-')[1]) + 1)

        fields[field_name] = [range1, range2]

    return fields


def extract_my_ticket(input_data):
    ticket = ''

    for i in range(len(input_data)):
        if input_data[i] == 'your ticket:':
            ticket = input_data[i + 1]

    return ticket


def extract_tickets(input_data):
    tickets = []

    for i in range(len(input_data)):
        if input_data[i] == 'nearby tickets:':
            tickets = input_data[i + 1:]

    return tickets


if __name__ == "__main__":
    # Read input data
    data = read_input()

    # Information from the input data
    valid_fields = extract_fields(data)
    my_ticket = extract_my_ticket(data)
    nearby_tickets = extract_tickets(data)

    # Solve problem
    valid_nearby_tickets = []

    # Remove invalid tickets
    for nt in nearby_tickets:
        ticket_values = nt.split(',')
        valid_ticket = True

        for tv in ticket_values:
            valid_value = False

            for field_value_list in valid_fields.values():
                for field_values in field_value_list:
                    if int(tv) in field_values:
                        valid_value = True

            if not valid_value:
                valid_ticket = False
                break

        if valid_ticket:
            valid_nearby_tickets.append(nt)

    # Possible field mappings
    field_mappings = {}

    for k in valid_fields:
        field_mappings[k] = [1] * len(my_ticket.split(','))

    for nt in nearby_tickets:
        ticket_values = nt.split(',')

        for tv_index in range(len(ticket_values)):
            tv_value = int(ticket_values[tv_index])

            for field_name, field_value_list in valid_fields.items():
                valid_value = False

                for field_values in field_value_list:
                    if tv_value in field_values:
                        valid_value = True

                if not valid_value:
                    # Not a valid value for this field
                    field_mappings[field_name][tv_index] = 0

    for k, v in field_mappings.items():
        print(f"{k.ljust(25, ' ')}{v}")













