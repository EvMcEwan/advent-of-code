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
    triple_items = []

    bag_1 = []
    bag_2 = []
    bag_3 = []

    # go over all lines
    counter = 1
    for line in lines:
        if counter == 1:
            bag_1 = line
        if counter == 2:
            bag_2 = line
        if counter == 3:
            bag_3 = line

        if counter == 3:
            # loop over rucksacks to see if any item is present in all three
            triple_in_group = []
            for a in bag_1:
                for b in bag_2:
                    for c in bag_3:
                        # if in both -> add to list
                        if a == b and a == c and a not in triple_in_group and a != "\n":
                            triple_in_group += [a]


            triple_items += triple_in_group
            triple_in_group = []

            counter = 0

        counter += 1


    # loop over double_items and check their priority score in the dict
    for item in triple_items:
        # add priority score to sum_priorities
        sum_priorities += dct[item]
        print(item, dct[item])

    print("The sum of the priorities of the items that appear in both compartments is", sum_priorities)