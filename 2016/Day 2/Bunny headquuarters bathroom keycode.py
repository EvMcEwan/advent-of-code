# open file and read lines
with open("input.txt") as input_file:
    lines = input_file.readlines()

    # create keypad
    key_pad = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    row = 1
    column = 1
    number = key_pad[row][column]
    code = []

    # TODO: loop over instructions to find the final number, ignoring impossible moves
    for i in range(len(lines)):
        for letter in lines[i]:
            if letter == "U":
                row -= 1
                if row < 0:
                    row = 0
            if letter == "D":
                row += 1
                if row > 2:
                    row = 2
            if letter == "R":
                column += 1
                if column > 2:
                    column = 2
            if letter == "L":
                column -= 1
                if column < 0:
                    column = 0
        code.append(key_pad[row][column])
        print(code)
        print("-----------------------------")

