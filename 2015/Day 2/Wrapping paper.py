input_file = open("input.txt", "r")
line = None

total_paper = 0


while line != "":
    line = input_file.readline()
    # print(line)
    if line != "":
        surface_this_present = 0

        l, w, h = line.split("x")
        h, rest = h.split("\n")

        a = int(l)*int(w)
        b = int(w)*int(h)
        c = int(h)*int(l)
        d = 0

        if a <= b and a <= c:
            d = a
        elif b <= a and b <= c:
            d = b
        else:
            d = c

        surface_this_present += 2*a + 2*b + 2*c + d

        total_paper += surface_this_present

print(total_paper)


input_file.close
