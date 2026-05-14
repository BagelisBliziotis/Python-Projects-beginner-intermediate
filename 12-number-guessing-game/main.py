import random
import art

lives = 0
print(art.logo)
print("Welcome to the Number Guessing Game!")
num = random.randint(0,101)
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficult. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("Invalid input")
while lives != 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == num:
        print(f"You got it! The answer was {num}.")
        break
    elif guess > num:
        if lives != 1:
            print("Too High!")
        lives -= 1
    else:
        if lives !=1:
            print("Too Low!")
        lives -= 1
if lives == 0:
    print(f"You've run out of guesses.The answer was {num}. Refresh the page to run again.")
