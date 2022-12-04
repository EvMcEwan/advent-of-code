input_file = open("input.txt", "r")
line = None

total_ribbon = 0

while line != "":
    line = input_file.readline()
    # print(line)
    if line != "":
        length_this_present = 0

        lst = []
        lst = line.split("x")
        lst[2], rest = lst[2].split("\n")

        lst.sort(key = int)

        a, b, c = lst

        length_this_present += 2*int(a)+2*int(b) + int(a)*int(b)*int(c)

        total_ribbon += length_this_present

print(total_ribbon)

input_file.close
