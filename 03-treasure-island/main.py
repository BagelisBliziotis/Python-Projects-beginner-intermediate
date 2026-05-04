print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("\nYou have arrived in a cross road! Where do you want to go?")
choice1 = input(''' Type "left" or "right": ''').lower().strip()
if choice1 == "right":
    print("\nTwo assassins paid by your brother were waiting for you, so he could get your parents inheritance! GAME OVER!")
elif choice1 == "left":
    print("\nYou have come to a lake. There is an island in the middle of the lake.")
    choice2 = input('''Type "wait" to wait for a boat. Type "swim" to swim across: ''').lower().strip()
    if choice2 == "swim":
        print("\nThe lake is full with alligators that really dont like you. GAME OVER!")
    elif choice2 == "wait":
        print("\nYou arrive at the island unharmed. There is a house with 3 doors.")
        choice3 = input("One red,one yellow and one blue. Which door do you choose? ").lower().strip()
        if choice3 == "blue":
            print("\nThe owner of the house, a pirate , comes out and shoots you for trying to steal his treasure. GAME OVER!")
        elif choice3 == "red":
            print("\nA dragon comes out sneezes and you die. GAME OVER!")
        elif choice3 == "yellow":
            print("\nYes yellow is for gold. YOU WON !!?!!!?!")
        else:
            print("\nWrong input!! Time passes and you die of old age. GAME OVER!")
    else:
        print("\nWrong input! GAME OVER!")
else:
   print("\nWrong input! GAME OVER!")
