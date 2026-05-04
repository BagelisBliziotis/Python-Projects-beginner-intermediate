import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper , scissors]

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

if choice == "0" or choice == "1" or choice == "2":
    choice = int(choice)

computer = random.randint(0,2)
progress = False

if choice == computer:
    outcome = "Its a draw"
elif choice == 0 and computer == 1:
    outcome = "You lose!"
elif choice == 0 and computer == 2:
    outcome = "You win!"
elif choice == 1 and computer == 0:
    outcome = "You win!"
elif choice == 1 and computer == 2:
    outcome = "You lose!"
elif choice == 2 and computer == 0:
    outcome = "You lose!"
elif choice == 2 and computer == 1:
    outcome = "You win!"
else:
    progress = True
    print("Wrong input")

if(not progress):
    print(options[choice])
    print("\nComputer chose: ")
    print(options[computer])
    print(f"\n{outcome}")
