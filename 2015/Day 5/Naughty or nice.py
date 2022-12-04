input_file = open("input.txt", "r")

count_nice = 0

for line in input_file:
    three_vowels = False
    double_letters = False
    substring = False

    count_vowels = 0  # test 1/3 for the presence of at least three vowels
    for i in line:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count_vowels += 1
            if count_vowels == 3:
                three_vowels = True

    test = ""  # test 2/3 for presence of letters that appear twice in a row
    for i in line:
        if test == i:
            double_letters = True
        test = i

    if "ab" not in line and "cd" not in line and "pq" not in line and "xy" not in line:  # test 3/3 for the presence of
        # these specific substrings
        substring = True

    if three_vowels and double_letters and substring:   # if all 3 tests render true, add one to the nice counter
        count_nice += 1
        print("nice")
    else: print("naughty")

print(count_nice)

input_file.close()
