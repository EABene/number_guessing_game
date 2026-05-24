import random

def greet():
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have limited chances to guess the correct number.
Please select the difficulty level:
          
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n""")
    

# Random number determination

correct_number = random.randint(1, 100)

# Actual program start

difficulty_level = ""

greet()
difficulty_level = input("Enter your choice: ")

while difficulty_level not in ['1', '2', '3']:
    print("Please select either 1, 2 or 3")
    difficulty_level = input("Enter your choice: ")

difficulties = {
    '1': "Easy",
    '2': "Medium",
    '3': "Hard"
    }

print(f"\nGreat! You have selected the {difficulties[difficulty_level]} difficulty level.\nLet's start the game!\n")

chances = {'1': 10, '2': 5, '3': 3}

# Guessing starts here

attempts = 0
guess = ""

while correct_number != guess:
    attempts += 1
    if attempts > chances[difficulty_level]:
        print(f"You have used up your attempts ({chances[difficulty_level]}).\nCorrect number was: {correct_number}\nBetter luck next time :)")
        break
    try: 
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Guess is not a number.")
        continue

    if not 1 <= guess <= 100:
        print("Guess is not in the given range.")
        continue


    if guess > correct_number:
        print(f"Incorrect! The number is less than {guess}.\n")
    elif guess < correct_number:
        print(f"Incorrect! The number is greater than {guess}.\n")
    else:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
        break







