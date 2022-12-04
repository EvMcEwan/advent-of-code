input_file = open("input.txt", "r")

def string_to_instructions(string):
    if "turn" in string:
        turn, on_off_toggle, number_a, through, number_b = string.split()
    else:
        on_off_toggle, number_a, through, number_b = string.split()

    coordinates_a1, coordinates_a2 = (int(x) for x in number_a.split(","))
    coordinates_b1, coordinates_b2 = (int(x) for x in number_b.split(","))

    return on_off_toggle, coordinates_a1, coordinates_a2, coordinates_b1, coordinates_b2


# Create dictionary with 0-999 grid
# This holds all lights on the grid. key will be the coordinates, values are True or False
light_grid = {}
for row in range(1000):
    for column in range(1000):
        light_grid[row, column] = 0

for line in input_file:
    on_off_toggle, coordinates_a1, coordinates_a2, coordinates_b1, coordinates_b2 = string_to_instructions(line)

    if on_off_toggle == "on":
        for row in range(coordinates_a1, coordinates_b1 + 1):
            for column in range(coordinates_a2, coordinates_b2 + 1):
                light_grid[(row, column)] = light_grid[(row, column)] + 1

    if on_off_toggle == "off":
        for row in range(coordinates_a1, coordinates_b1 + 1):
            for column in range(coordinates_a2, coordinates_b2 + 1):
                light_grid[(row, column)] = light_grid[(row, column)] - 1
                if light_grid[(row, column)] < 0:
                    light_grid[(row, column)] = 0

    if on_off_toggle == "toggle":
        for row in range(coordinates_a1, coordinates_b1 + 1):
            for column in range(coordinates_a2, coordinates_b2 + 1):
                light_grid[(row, column)] = light_grid[(row, column)] + 2

print(light_grid)
print(sum(light_grid.values()))

input_file.close()