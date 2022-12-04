# New rules for letters to be nice:
# - It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy)
# or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# - It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or
# even aaa.

input_file = open("input.txt", "r")

count_nice = 0

for line in input_file:
    double_letters = False
    sandwich_letters = False

    substring = ""
    for i in range(0, len(line) - 1):   # first test to test if any 2 letter substring is present more than once
        substring = line[i] + line[i+1]

        count_substring = line.count(substring)
        if count_substring == 2:
            double_letters = True

    for i in range(2, len(line)):   # second test to test if any letter repeats with exactly one letter in between
        a = line[i]
        b = line[i-2]
        if line[i] == line[i-2]:
            sandwich_letters = True

    if double_letters and sandwich_letters:   # if all tests render true, add one to the nice counter
        count_nice += 1
        print("nice")
    else: print("naughty")

print(count_nice)

input_file.close()
