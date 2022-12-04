input_file = open("input.txt", "r")
directions = input_file.read()
print(directions)

floor = 0

for i in range(len(directions)):
    if floor == -1:
        print("The first time it goes to the basement is at position " + str(i))
    if directions[i] == "(":
        floor += 1
    if directions[i] == ")":
        floor -= 1

print("The correct floor is " + str(floor))

input_file.close()