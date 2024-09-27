# 0083781 Muhammed Efe Keskin Comp125-03
import random
# This function simulates the rolling of two dice. It should randomly generate
# two numbers in the range of 1 through 6 and return those two numbers to the
# caller. Please check Page 49 of the 6th slide set about this simulation and
# the use of the random module.
def roll_two_dice():
    first_dice = random.randint(1,6)
    sec_dice = random.randint(1,6)
    return first_dice,sec_dice
#  # Write your code here
#  # ...
# # This function gets a lucky number from a player and returns it to the caller.
# # A lucky number should be in between 4 and 12 (inclusive). If the player enters
# # an invalid number, the function should not accept it and ask the player to enter
# # a new one until s/he enters a valid lucky number. You may assume that the input
# # is always an integer.
def get_lucky_number():
    lucky_number = int(input("What is your lucky number between 4 and 12(inclusive) ? "))
    while lucky_number > 13 or lucky_number < 5:
        lucky_number = int(input("This is not a valid lucky number, please enter another one "))
    return lucky_number

#  # Write your code here
#  # ...
# # This function is to implement Rule 4. Remember that when Rule 4 becomes
# # applicable, the program asks the player whether s/he wants to continue or
# # voluntarily stop. This function asks the player to enter her/his choice and
# # returns True if the player wants to continue, otherwise it returns False.
# # The user can have four valid answers: y or Y for yes and n or N for no.
# # If the player enters an invalid answer, the function should not accept it
# # and ask the player to enter a new one until s/he enters a valid answer.
def get_player_answer():
    answer = input("Do you want to continue rolling dices ? y or n ")
    while answer != "y" and answer != "Y" and answer != "n" and answer != "N":
        answer = input("I couldn't understand, Do you want to continue rolling dices ? y or n ")
    return answer
#  # Write your code here
#  # ...
# This function takes two rolls and a lucky number and applies the rules
# one by one. It should return the rule number. You may assume that the parameters
# are always valid. Indeed, you will guarantee the validness of the parameters
# before calling this function (you need to call it in the one_turn function).
#
# Before starting the implementation, do not forget to read the details of
# the rules given in the first page.
def one_roll(die1, die2, lucky_number):
    if die1 == 1 or die2 == 1 and not die1 == die2 == 1:
        rule = 1
    elif die1 == die2 == 1:
        rule = 2
    elif die1 + die2 == lucky_number:
        rule = 3
    else: rule = 4
    return rule

 # Write your code here
 # ...
# This function has two parameters: a lucky number and the current score of the
# player from her/his previous turn. It should simulate one turn as explained
# in the first page and return the new score of the player. That is, it should
# simulate the rolling of two dice, call one_roll function to understand which
# rule is applicable, and take the necessary actions for the applicable rule.
# You may assume that the lucky number is always valid. Indeed, you will guarantee
# the validness of this parameter before calling this function (you need to call
# it in Part C).
#
# Before starting the implementation, do not forget to read the details of
# the rules given in the first page.
#
# Here we strongly recommend you to also call the functions you will implement
# in Part A. This will help you more easily implement this function.
def one_turn(lucky_number, current_score):
    score_in_process = 0
    a, b = roll_two_dice()
    rule_applied = one_roll(a, b, lucky_number)
    print(f"Dice rolled: {a} and {b} ")
    if rule_applied == 1:
        print("Rule 1 applied")
        score_in_process = 0
    if rule_applied == 2:
        print("Rule 2 applied")
        score_in_process = 0
        current_score = score_in_process
    if rule_applied == 3:
        print("Rule 3 applied")
        score_in_process += current_score
    if rule_applied == 4:
        print("Rule 4 applied")
        score_in_process += a + b
    current_score += score_in_process
    if rule_applied == 1 or rule_applied == 2:
        answer = "n"
    elif rule_applied == 3:
        answer = "h"
    else: answer = "y"
    return current_score,answer
 # Write your code here
 # ...
# This function simulates the entire game. Check the example given below for
# the outputs we expect from this function
def play_pig():
    print("Player 1 Turn")
    player_1_current_score = 0
    player_2_current_score = 0
    lucky = get_lucky_number()
    player_1_current_score,answer = one_turn(lucky,player_1_current_score)
    print(f"""--------------------------
    Current scores
    Player 1: {player_1_current_score}
    Player 2: {player_2_current_score}
    --------------------------""")
    first_turn = True
    while player_1_current_score < 100 and player_2_current_score < 100:
        answer = "y"
        if first_turn:
            answer = get_player_answer()
            first_turn = False
        while answer == "Y" or answer == "y" or answer =="h":
            print("Player 1 Turn")
            lucky = get_lucky_number()
            player_1_current_score,answer = one_turn(lucky,player_1_current_score)
            print(f"""--------------------------
            Current scores
            Player 1: {player_1_current_score}
            Player 2: {player_2_current_score}
            --------------------------""")
            if answer == "y":
                answer = get_player_answer()


        print("Player 2 Turn")
        lucky = get_lucky_number()
        player_2_current_score,answer = one_turn(lucky , player_2_current_score)
        print(f"""--------------------------
        Current scores
        Player 1: {player_1_current_score}
        Player 2: {player_2_current_score}
        --------------------------""")
        while answer == "Y" or answer == "y" or answer == "h":
            lucky = get_lucky_number()
            player_2_current_score,answer = one_turn(lucky, player_2_current_score)
            print(f"""--------------------------
            Current scores
            Player 1: {player_1_current_score}
            Player 2: {player_2_current_score}
            --------------------------""")
            if answer == "y":
                answer = get_player_answer()

    if player_1_current_score > player_2_current_score:
        print("Player 1 Wins")
    elif player_1_current_score < player_2_current_score:
        print("Player 2 Wins")
    else: print("It's a Draw")
# Write your code here
# ...
play_pig()
