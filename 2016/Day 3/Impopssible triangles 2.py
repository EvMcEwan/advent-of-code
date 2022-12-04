with open('input.txt') as input_file:
    lines = input_file.readlines()

    possible_triangles = 0
    triangles = []
    counter = 0

    for sides in lines:
        triangle1, triangle2, triangle3 = sides.split()

        triangles.append([triangle1, triangle2, triangle3])

        counter += 1

        if counter == 3:
            for column in range(3):
                side1 = int(triangles[0][column])
                side2 = int(triangles[1][column])
                side3 = int(triangles[2][column])
                test1 = side1 + side2 > side3
                test2 = side1 + side3 > side2
                test3 = side2 + side3 > side1
                if test1 and test2 and test3:
                    possible_triangles += 1

                    print(triangles, "is a possible triangle")
                    print(possible_triangles)

            triangles = []
            counter = 0




