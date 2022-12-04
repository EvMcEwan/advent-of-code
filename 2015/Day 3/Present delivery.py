# make list of list with all visited coordinates
input_file = open("input.txt", "r")
line = input_file.read()

visited_locations = []
x = 0
y = 0

for i in range(len(line)):
    if line[i] == "^":
        y += 1
    if line[i] == "v":
        y -= 1
    if line[i] == ">":
        x += 1
    if line[i] == "<":
        x -= 1
    visited_locations.append([x, y])

# check how many unique coordinates are in the list of list
counter = 1
seen = []
for i in visited_locations:
    if i not in seen:
        seen.append(i)
        counter += 1

print(counter)


input_file.close()
