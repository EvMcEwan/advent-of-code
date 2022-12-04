# open file and read lines
with open("input.txt") as input_file:
    lines = input_file.readlines()

    # create keypad
    # key_pad = [[1],
    #         [2, 3, 4],
    #      [5, 6, 7, 8, 9],
    #      ['A', 'B', 'C'],
    #           ['D']]

    key_pad = [["v", "v", "v", "v", "v", "v", "v"],
               ["v", "v", "v",  1,  "v", "v", "v"],
               ["v", "v",  2,   3,   4,  "v", "v"],
               ["v",  5,   6,   7,   8,   9,  "v"],
               ["v", "v", 'A', 'B', 'C', "v", "v"],
               ["v", "v", "v", 'D', "v", "v", "v"],
               ["v", "v", "v", "v", "v", "v", "v"]]

    row = 3
    column = 1
    number = key_pad[row][column]
    code = []

    # TODO: loop over instructions to find the final number, ignoring impossible moves
    for i in range(len(lines)):
        for letter in lines[i]:
            if letter == "U":
                if key_pad[row - 1][column] != "v":
                    row -= 1
            elif letter == "D":
                if key_pad[row + 1][column] != "v":
                    row += 1
            elif letter == "R":
                if key_pad[row][column + 1] != "v":
                    column += 1
            elif letter == "L":
                if key_pad[row][column - 1] != "v":
                    column -= 1
        code.append(key_pad[row][column])
        print(code)
        print("-----------------------------")
