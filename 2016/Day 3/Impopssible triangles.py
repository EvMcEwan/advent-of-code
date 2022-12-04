with open('input.txt') as input_file:
    lines = input_file.readlines()

    possible_triangles = 0

    for triangles in lines:
        side1, side2, side3 = triangles.split()
        side1 = int(side1)
        side2 = int(side2)
        side3 = int(side3)
        test1 = side1 + side2 > side3
        test2 = side1 + side3 > side2
        test3 = side2 + side3 > side1
        if test1 and test2 and test3:
            possible_triangles += 1

            print(triangles, "is a possible triangle")
            print(possible_triangles)