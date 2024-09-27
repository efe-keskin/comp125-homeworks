# 0083781 Muhammed Efe Keskin Comp125-03
# This program takes a positive integer from the user and displays it in the expanded form.

# First I want an integer input
user_input = int(input("Enter a positive integer: "))
# I store that input as three different variables : 1 for the continuity of while loop, 1 for digit tracking
# and 1 for our main purpose which is to store the input as it is.
user_input_in_calc = user_input
digit_tracker = user_input
digits = 0
# I created a blank string variable to add further strings onto
text = ""
# The program quits if the input is not a positive integer
if user_input > 0:
    # This part keeps track of existing digits with while loop.
    while digit_tracker >= 1 and user_input > 0:
        digit_tracker = digit_tracker / 10
        digits += 1
    # For loop is used to create expanded form of each digit separately
    for digit in range(digits - 1, -1, -1):
        numbers = int(user_input_in_calc / 10 ** digit)
        user_input_in_calc -= numbers * 10 ** digit
        a = f"({numbers}*{10 ** digit})"
        text += a
        # When the last digit is done we stop adding "+" signs
        if digit > 0:
            text += " + "
    # We print the text as a whole
    print(f"{user_input} = {text}")
else: print("That is not a positive integer")
