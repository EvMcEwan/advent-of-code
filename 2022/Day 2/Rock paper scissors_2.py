with open('input.txt') as input_file:
    lines = input_file.readlines()

    shape_points = 0
    game_points = 0

    # for loop to go over each round
    for line in lines:
        opponent, outcome = line.split()

        # set point value of the different shapes
        rock = 1
        paper = 2
        scissors = 3

        if opponent == "A":   # rock
            if outcome == "X":     # lose
                game_points += 0
                shape_points += scissors
            elif outcome == "Y":   # draw
                game_points += 3
                shape_points += rock
            elif outcome == "Z":   # win
                game_points += 6
                shape_points += paper
        elif opponent == "B":  # paper
            if outcome == "X":  # lose
                game_points += 0
                shape_points += rock
            elif outcome == "Y":  # draw
                game_points += 3
                shape_points += paper
            elif outcome == "Z":  # win
                game_points += 6
                shape_points += scissors
        elif opponent == "C":  # scissors
            if outcome == "X":  # lose
                game_points += 0
                shape_points += paper
            elif outcome == "Y":  # draw
                game_points += 3
                shape_points += scissors
            elif outcome == "Z":  # win
                game_points += 6
                shape_points += rock

        print("Round:", line, "\b"
              "Shape points:", shape_points, "\n"
              "Game points:", game_points, "\n")

    total_points = shape_points + game_points

    print("The total score is", total_points, "!")
