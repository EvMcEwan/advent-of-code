
with open('input.txt') as input_file:
    lines = input_file.readlines()

    calories = 0
    most_calories = 0

    for line in lines:
        if line != "\n":
            calories += int(line)
        else:
            calories = 0

        # if the number is bigger than most_calories, that is most_calories
        if calories > most_calories:
            most_calories = calories

    print("The elf with the most calories is carrying", most_calories, "calories.")