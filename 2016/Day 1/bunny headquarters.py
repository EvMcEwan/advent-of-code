import matplotlib
import pandas as pd
import random
import sys
import array
import matplotlib.pyplot as plt

with open('input.txt') as input_file:
    line = input_file.readline()
    directions = line.split(", ")

    visited_locations = {"0": [0, 0]}
    dict_counter = 1
    facing_direction = 'N'

    for direction in directions:
        if direction[0] == 'R':
            if facing_direction == 'N':
                facing_direction = 'O'
            elif facing_direction == 'O':
                facing_direction = 'S'
            elif facing_direction == 'S':
                facing_direction = 'W'
            elif facing_direction == 'W':
                facing_direction = 'N'

        elif direction[0] == 'L':
            if facing_direction == 'N':
                facing_direction = 'W'
            elif facing_direction == 'W':
                facing_direction = 'S'
            elif facing_direction == 'S':
                facing_direction = 'O'
            elif facing_direction == 'O':
                facing_direction = 'N'

        blocks = int(direction[1:])
        if facing_direction == 'N':
            for block in range(block):
                new_location = [visited_locations[str(dict_counter - 1)][0],
                                visited_locations[str(dict_counter - 1)][1] + 1]

                dict_values = visited_locations.values()

                if new_location in dict_values:
                    print("For the second time at", new_location)

                visited_locations[str(dict_counter)] = new_location

                print(direction)
                print(visited_locations[str(dict_counter)])

                dict_counter += 1

        elif facing_direction == 'O':
            for block in range(blocks):
                new_location = [visited_locations[str(dict_counter - 1)][0] + 1,
                                visited_locations[str(dict_counter - 1)][1]]

                dict_values = visited_locations.values()

                if new_location in dict_values:
                    print("For the second time at", new_location)

                visited_locations[str(dict_counter)] = new_location

                print(direction)
                print(visited_locations[str(dict_counter)])

                dict_counter += 1

        elif facing_direction == 'S':
            for block in range(blocks):
                new_location = [visited_locations[str(dict_counter - 1)][0],
                                visited_locations[str(dict_counter - 1)][1] - 1]

                dict_values = visited_locations.values()

                if new_location in dict_values:
                    print("For the second time at", new_location)

                visited_locations[str(dict_counter)] = new_location

                print(direction)
                print(visited_locations[str(dict_counter)])

                dict_counter += 1

        elif facing_direction == 'W':
            for block in range(blocks):
                new_location = [visited_locations[str(dict_counter - 1)][0] - 1,
                                visited_locations[str(dict_counter - 1)][1]]

                dict_values = visited_locations.values()

                if new_location in dict_values:
                    print("For the second time at", new_location)

                visited_locations[str(dict_counter)] = new_location

                print(direction)
                print(visited_locations[str(dict_counter)])

                dict_counter += 1

    print(visited_locations)

