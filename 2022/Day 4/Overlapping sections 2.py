# open input file
with open('input.txt') as input_file:
    lines = input_file.readlines()

    counter = 0

    # loop over assignments pairs
    for line in lines:
        # split the two assignments pairs
        first, second = line.split(',')

        first_1, first_2 = first.split('-')
        second_1, second_2 = second.split('-')

        # if the first number is bigger than the other first number and the second number is smaller than the
        # other second number then one pair contains the other -> add one to counter

        first_1 = int(first_1)
        first_2 = int(first_2)
        second_1 = int(second_1)
        second_2 = int(second_2)

        if first_2 >= second_1 >= first_1:
            print(line)
            counter += 1
        elif second_2 >= first_1 >= second_1:
            print(line)
            counter += 1


    print(counter)

