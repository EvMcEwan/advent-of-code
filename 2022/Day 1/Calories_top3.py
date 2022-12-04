
with open('input.txt') as input_file:
    lines = input_file.readlines()

    calories = 0
    most_calories_1 = 0
    most_calories_2 = 0
    most_calories_3 = 0

    for line in lines:
        if line != "\n":
            calories += int(line)
        else:
            calories = 0

        # if the number is bigger than most_calories, that is most_calories
        if calories > most_calories_1:
            most_calories_3 = most_calories_2
            most_calories_2 = most_calories_1
            most_calories_1 = calories
        elif calories > most_calories_2:
            most_calories_3 = most_calories_2
            most_calories_2 = calories
        elif calories > most_calories_3:
            most_calories_3 = calories

        total_calories = most_calories_1 + most_calories_2 + most_calories_3

    print("The elf with the most calories is carrying", total_calories, "calories.")