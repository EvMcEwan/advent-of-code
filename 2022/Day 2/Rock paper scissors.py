with open('input.txt') as input_file:
    lines = input_file.readlines()

    shape_points = 0
    game_points = 0

    # for loop to go over each round
    for line in lines:
        opponent, me = line.split()

        # get points from chosen shape
        if me == "X":    # rock
            shape_points += 1
        elif me == "Y":  # paper
            shape_points += 2
        elif me == "Z":  # scissors
            shape_points += 3

        # get points from game outcome
        if opponent == "A":   # rock
            if me == "X":     # rock
                game_points += 3
            elif me == "Y":   # paper
                game_points += 6
            elif me == "Z":   # scissors
                game_points += 0
        elif opponent == "B":  # paper
            if me == "X":      # rock
                game_points += 0
            elif me == "Y":    # paper
                game_points += 3
            elif me == "Z":    # scissors
                game_points += 6
        elif opponent == "C":  # scissors
            if me == "X":      # rock
                game_points += 6
            elif me == "Y":    # paper
                game_points += 0
            elif me == "Z":    # scissors
                game_points += 3

        print("Round:", line, "\b"
              "Shape points:", shape_points, "\n"
              "Game points:", game_points, "\n")

    total_points = shape_points + game_points

    print("The total score is", total_points, "!")
