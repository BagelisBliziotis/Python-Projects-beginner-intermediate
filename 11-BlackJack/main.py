import random

import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
question = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
print("\n"*20)
while True:
    card = []
    computer_card = []
    if question == 'y':
        print(art.logo)
        card1 = random.choice(cards)
        card2 = random.choice(cards)
        card.append(card1)
        card.append(card2)
        computer_card1 = random.choice(cards)
        computer_card2 = random.choice(cards)
        computer_card.append(computer_card1)
        computer_card.append(computer_card2)
        score = card1 + card2
        computer_score = computer_card1 + computer_card2
        print(f"Your cards: {card}, current score: {score} ")
        print(f"Computer's first card: {computer_card1}")
        while score <= 21:
            pull = input("Type 'y' to get another card, type 'n' to pass: ")
            if pull == 'y' :
                choice = random.choice(cards)
                card.append(choice)
                score += choice
                print(f"Your cards: {card}, current score: {score} ")
                print(f"Computer's first card: {computer_card1}")
                if score > 21 and 11 in card:
                    score -= 10
                    for i in range(0,len(card)):
                        if card[i] == 11:
                            card[i] = 1
            else:
                break

        while computer_score <= 16:
            choice = random.choice(cards)
            computer_card.append(choice)
            computer_score += choice
            if computer_score >21 and 11 in computer_card:
                computer_score -= 10
                for i in range(0,len(computer_card)):
                    if computer_card[i] == 11:
                        computer_card[i] = 1
                        break

        if score > 21:
            print(f"Your final hand: {card}, final score: {score}")
            print(f"Computer's final hand: [{computer_card1}], final score: {computer_card1}")
            print("You went over. You lose!!")
        elif score == computer_score:
            print(f"Your final hand: {card}, final score: {score}")
            print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
            print("Draw!!")
        elif computer_score > 21:
            print(f"Your final hand: {card}, final score: {score}")
            print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
            print("Opponent went over. You Win !!")
        elif score > computer_score:
            print(f"Your final hand: {card}, final score: {score}")
            print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
            print("You Win !!")
        else:
            print(f"Your final hand: {card}, final score: {score}")
            print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
            print("You Lose!!")
        question = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
        if question != 'y':
            break
        print('\n' *20)

