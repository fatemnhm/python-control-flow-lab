# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()



# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
  
    letter = input("Please enter a letter: ")
    if letter.isalpha() and len(letter) == 1:
        if letter.lower() in 'aeiou':
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single letter.")

# Call the function
check_letter()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = input("Input a dog's age: ")
    if dog_age.isdigit():
        dog_age = int(dog_age)
        if dog_age == 1:
            dog_years = 10
        elif dog_age == 2:
            dog_years = 20
        else:
            dog_years = 20 + (dog_age - 2) * 7
        print(f"The dog's age in dog years is {dog_years}.")
    else:
        print("Invalid input. Please enter a valid number.")

# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    cold = input("Is it cold? (yes/no) ")
    raining = input("Is it raining? (yes/no) ")
    if cold.lower() == 'yes' and raining.lower() == 'yes':
        print("Wear a waterproof coat.")
    elif cold.lower() == 'yes' and raining.lower() == 'no':
        print("Wear a warm coat.")
    elif cold.lower() == 'no' and raining.lower() == 'yes':
        print("Carry an umbrella.")
    elif cold.lower() == 'no' and raining.lower() == 'no':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ")
    day = input("Enter the day of the month: ")
    if month.capitalize() in ('Jan', 'Feb', 'Mar'):
        season = 'Winter'
    elif month.capitalize() in ('Apr', 'May', 'Jun'):
        season = 'Spring'
    elif month.capitalize() in ('Jul', 'Aug', 'Sep'):
        season = 'Summer'
    elif month.capitalize() in ('Oct', 'Nov', 'Dec'):
        season = 'Fall'
    else:
        print("Invalid month. Please enter a valid month.")
        return
    if month.capitalize() == 'Dec' and int(day) >= 21:
        season = 'Winter'
    elif month.capitalize() == 'Mar' and int(day) >= 20:
        season = 'Spring'
    elif month.capitalize() == 'Jun' and int(day) >= 21:
        season = 'Summer'
    elif month.capitalize() == 'Sep' and int(day) >= 22:
        season = 'Fall'
    print(f"{month.capitalize()} {day} is in {season}.")

# Call the function
determine_season()