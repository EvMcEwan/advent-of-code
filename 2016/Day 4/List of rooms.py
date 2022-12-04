from collections import Counter

# open file and read lines
with open("test_input.txt") as input_file:
    lines = input_file.readlines()

    for line in lines:
        # separate encrypted name, sector ID, and checksum
        name = line[0:len(line)-11]
        sectorID = line[len(line)-11:len(line)-8]
        checksum = line[len(line)-7:len(line)-2]

        # find number of occurrences for all letters in the encrypted name
        letters = []
        all_letters = []
        for i in name:
            all_letters.append(i)
            if i not in letters and i != "-":
                letters.append(i)

        print(letters)
        letters_sorted = []
        for i in letters:
            print(i, name.count(i))

        letters_sorted = [item for items, c in Counter(all_letters).most_common() for item in [items] * c]

        print(letters_sorted)


        # put letters in order of occurrence and compare with checksum

        # if the room is real add sector ID to total sector ID