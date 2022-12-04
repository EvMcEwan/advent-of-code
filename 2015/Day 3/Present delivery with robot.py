# make list of list with all visited coordinates
input_file = open("input.txt", "r")
line = input_file.read()

visited_locations = [[0, 0]]
x_santa = 0
y_santa = 0
x_robot = 0
y_robot = 0

# Santa instructions
for i in range(0, len(line), 2):
    if line[i] == "^":
        y_santa += 1
    if line[i] == "v":
        y_santa -= 1
    if line[i] == ">":
        x_santa += 1
    if line[i] == "<":
        x_santa -= 1
    visited_locations.append([x_santa, y_santa])

# Robot instructions
for i in range(1, len(line), 2):
    if line[i] == "^":
        y_robot += 1
    if line[i] == "v":
        y_robot -= 1
    if line[i] == ">":
        x_robot += 1
    if line[i] == "<":
        x_robot -= 1
    visited_locations.append([x_robot, y_robot])

# check how many unique coordinates are in the list of list
counter = 0
seen = []
for i in visited_locations:
    if i not in seen:
        seen.append(i)
        counter += 1

print(counter)

input_file.close()
