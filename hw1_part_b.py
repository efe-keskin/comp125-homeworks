# 0083781 Muhammed Efe Keskin Comp125-03
# This program is a simple number guessing game for two people.

secret_number = int(input("Enter a 3 digits positive integer for your opponent to guess: "))

# First the program checks if the input is acceptable or not
# If it is not it wants another input
while secret_number < 100:
    secret_number = int(input("Invalid number, enter a three-digit positive number: "))
# The program splits the input to its digits
secret_number_first = int(secret_number / 100)
secret_number_second = int((secret_number - (secret_number_first * 100)) / 10)
secret_number_third = int(secret_number - (secret_number_second * 10) - (secret_number_first * 100))
# The program takes a guess input and checks its validity
guess = int(input("Guess the 3 digits positive integer: "))
while guess < 100:
    guess = int(input("Invalid number, enter a three-digit positive number: "))
# If the guess is suitable it continues on and splits the number to its digits
while guess >= 100 and guess != secret_number:
    guess_first = int(guess / 100)
    guess_second = int((guess - (guess_first * 100)) / 10)
    guess_third = int(guess - (guess_second * 10) - (guess_first * 100))
# If the guess is not correct it checks the digits
    if guess != secret_number:
        correct_place = 0
        incorrect_place = 0
# This variables are introduced to keep track of the existence of guessed digits in secret number.
        first_exist = False
        first_is_right = False
        second_exist = False
        second_is_right = False
        third_exist = False
        third_is_right = False

        if guess_first == secret_number_first:
            correct_place += 1
            first_exist = True
            first_is_right = True

        if guess_second == secret_number_second:
            correct_place += 1
            second_exist = True
            second_is_right = True

        if guess_third == secret_number_third:
            correct_place += 1
            third_exist = True
            third_is_right = True

        if guess_first == secret_number_second:
            if not first_exist and not second_is_right:
                incorrect_place += 1
                first_exist = True

        if guess_first == secret_number_third:
            if not first_exist and not third_is_right:
                incorrect_place += 1
                first_exist = True

        if guess_second == secret_number_first:
            if not second_exist and not first_is_right:
                incorrect_place += 1
                second_exist = True


        if guess_second == secret_number_third:
            if not second_exist and not third_is_right:
                incorrect_place += 1
                second_exist = True

        if guess_third == secret_number_first:
            if not third_exist and not first_is_right:
                incorrect_place += 1
                third_exist = True

        if guess_third == secret_number_second:
            if not third_exist and not second_is_right:
                incorrect_place += 1
                third_exist = True

# After all that tracking it calculated the number of correct and incorrect places and it will print that
        print(f"{correct_place} correct places, {incorrect_place} incorrect places")
        guess = int(input("Guess the 3 digits positive integer: "))
        while guess < 100:
            guess = int(input("Invalid number, enter a three-digit positive number: "))
print(f"Yes the number was {guess}")
