# To-do list: adjust code so it can handle double wire input and output

import re
import string

# Create a dictionary with al wires to hold their values
alphabet = string.ascii_lowercase
combined_letters = []

for letter in alphabet:
    combined_letters.append(letter)

for letter_p1 in alphabet:
    for letter_p2 in alphabet:
        double_letters = letter_p1 + letter_p2
        combined_letters.append(double_letters)

wire_set = dict.fromkeys(combined_letters, 0)

print("wire_set:", wire_set)


def assemble_circuit(input_file):
    # Patterns

    # Pattern 1 for format: bn RSHIFT 2 -> bo
    pattern1 = r'(\w+) (\w+) (\w+) -> (\w+)'
    matcher1 = re.compile(pattern1)

    # Pattern 2 for format: NOT y -> i
    pattern2 = r'(NOT) (\w+) -> (\w+)'
    matcher2 = re.compile(pattern2)

    # Pattern 3 for format: 456 -> y
    pattern3 = r'(\d+) -> (\w+)'
    matcher3 = re.compile(pattern3)

    # Pattern 4 for format: lx -> a
    pattern4 = r'(\w+) -> (\w+)'
    matcher4 = re.compile(pattern4)

    while wire_set["a"] == 0:
        with open(input_file) as input:
            for line in input:

                match1 = matcher1.search(line)
                match2 = matcher2.search(line)
                match3 = matcher3.search(line)
                match4 = matcher4.search(line)
                if match1:
                    # y RSHIFT 2 -> g: f += x >> 2
                    source_wire = match1.group(1)
                    operand = match1.group(2)
                    operand_digit = match1.group(3)
                    sink_wire = match1.group(4)

                    if not (sink_wire == 0 or source_wire == 0 or operand_digit == 0 or operand == 0):
                        if operand == "RSHIFT":
                            wire_set[sink_wire] = wire_set[sink_wire] + (wire_set[source_wire] >> int(operand_digit))
                        elif operand == "LSHIFT":
                            wire_set[sink_wire] = wire_set[sink_wire] + (wire_set[source_wire] << int(operand_digit))
                        elif operand == "AND":
                            if source_wire.isdigit():
                                wire_set[sink_wire] = wire_set[sink_wire] + (int(source_wire) & wire_set[operand_digit])
                            else:
                                wire_set[sink_wire] = wire_set[sink_wire] + (
                                            wire_set[source_wire] & wire_set[operand_digit])
                        elif operand == "OR":
                            wire_set[sink_wire] = wire_set[sink_wire] + (
                                        wire_set[source_wire] | wire_set[operand_digit])

                        # print(source_wire + "-" + operand + "-" + operand_digit + "-" + sink_wire)
                        print(sink_wire, wire_set[sink_wire])

                elif match2:
                    # NOT x -> h
                    # h += -x
                    # if h < 0:
                    #     h += 65535
                    operand = match2.group(1)
                    source_wire = match2.group(2)
                    sink_wire = match2.group(3)

                    if not (source_wire == 0 or sink_wire == 0):
                        wire_set[sink_wire] += -wire_set[source_wire]
                        if wire_set[sink_wire] < 0:
                            wire_set[sink_wire] += 65535

                        # print(operand + "-" + source_wire + "-" + sink_wire)
                        print(sink_wire, wire_set[sink_wire])

                elif match3:
                    # 123 -> x
                    # x += 123
                    digit = match3.group(1)
                    sink_wire = match3.group(2)

                    if not (sink_wire == 0 or digit == 0):
                        wire_set[sink_wire] = wire_set[sink_wire] + int(digit)

                        print(sink_wire, wire_set[sink_wire])

                elif match4:
                    # y -> x
                    # x += y
                    source_wire = match4.group(1)
                    sink_wire = match4.group(2)

                    if not (source_wire == 0 or sink_wire == 0):
                        wire_set[sink_wire] += wire_set[source_wire]

                        # print(source_wire + "-" + sink_wire)
                        print(sink_wire, wire_set[sink_wire])

            # print(wire_set)

        print("The signal provided to wire a equals:", wire_set["a"])

        input.close()


assemble_circuit("input.txt")

# if len(source_wire) == 2 and len(sink_wire) == 2:
#     if operand == "RSHIFT":
#         wire_set[sink_wire[0]] = wire_set[sink_wire] + (wire_set[source_wire] >> int(operand_digit))
#
# elif len(source_wire) == 2 and len(sink_wire) == 1:
#     ...
# elif len(source_wire) == 1 and len(sink_wire) == 2:
#     ...
# else:
#     if operand == "RSHIFT":
#         wire_set[sink_wire] = wire_set[sink_wire] + (wire_set[source_wire] >> int(operand_digit))
#     elif operand == "LSHIFT":
#         wire_set[sink_wire] = wire_set[sink_wire] + (wire_set[source_wire] << int(operand_digit))
#     elif operand == "AND":
#         wire_set[sink_wire] = wire_set[sink_wire] + (wire_set[source_wire] & wire_set[operand_digit])
#     elif operand == "OR":
#         wire_set[sink_wire] = wire_set[sink_wire] + (wire_set[source_wire] | wire_set[operand_digit])
#
# # print(source_wire + "-" + operand + "-" + operand_digit + "-" + sink_wire)
# print(sink_wire, wire_set[sink_wire])
