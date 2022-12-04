import string

# open file
with open('input.txt') as input_file:
    lines = input_file.readlines()

    # set empty dictionary and create string of lowercase and uppercase alphabet
    dct = {}
    alphabet = string.ascii_lowercase + string.ascii_uppercase

    # make dictionary with priorities (scores) for all items (letters in alphabet)
    counter = 1
    for letter in alphabet:
        dct[letter] = counter
        counter += 1

    sum_priorities = 0
    double_items = []

    # go over all lines
    for line in lines:
        # split first and second compartment
        half = int(len(line)/2)                  # Possible bug here if it chooses the wrong side of the half
        first_compartment = line[0:half]
        second_compartment = line[half:]

        # loop over compartments to see if any item is present in both
        doubles_in_line = []
        for i in first_compartment:
            for item in second_compartment:
                # if in both -> add to list
                if i == item and i not in doubles_in_line:
                    doubles_in_line += [i]
        double_items += doubles_in_line
        doubles_in_line = []


    # loop over double_items and check their priority score in the dict
    for item in double_items:
        # add priority score to sum_priorities
        sum_priorities += dct[item]
        print(item, dct[item])

    print("The sum of the priorities of the items that appear in both compartments is", sum_priorities)