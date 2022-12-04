with open("input.txt") as input_file:
    characters_in_string = 0
    characters_in_memory = 0

    lines = [x.strip() for x in input_file.readlines()]

    # print(lines)

    for strings in lines:
        test_in_string = 0
        test_in_memory = 0
        for i in strings:
            characters_in_string += 1
            test_in_string += 1
        print(test_in_string)
        length_str = len(strings)
        i = 1
        while i < length_str - 1:
            test = strings[i]
            if strings[i] == "\\" and strings[i + 1] == "x":
                characters_in_memory += 1
                test_in_memory += 1
                i += 4
            elif strings[i] == "\\" and strings[i + 1] == "\"":
                characters_in_memory += 1
                test_in_memory += 1
                i += 2
            elif strings[i] == "\\" and strings[i + 1] == "\\":
                characters_in_memory += 1
                test_in_memory += 1
                i += 2
            elif strings[i] != "\\":
                characters_in_memory += 1
                test_in_memory += 1
                i += 1
            else:
                print(strings, i)
                break
        print(test_in_memory)
    result = characters_in_string - characters_in_memory

    for testing in range(2):
        t = 2

    print("The answer is", result)

