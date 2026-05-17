import art
import game_data
import random

my_data = game_data.data
score = 0
next_time = 0
winning = True
def option(dict_i_choose):
    old_dict = dict_i_choose

    new_dict = random.choice(my_data)
    while old_dict == new_dict:
        new_dict = random.choice(my_data)

    print(f'Compare A: {old_dict["name"]}, a {old_dict["description"]}, from {old_dict["country"]}')
    print(art.vs)
    print(f'Against B: {new_dict["name"]}, a {new_dict["description"]}, from {new_dict["country"]}')
    if old_dict["follower_count"] < new_dict["follower_count"]:
        return ["B",my_data.index(new_dict)]
    else:
        return ["A",my_data.index(new_dict)]



while winning:
    if score == 0:
        starting_dict = random.choice(my_data)
    else:
        starting_dict = my_data[next_time]
    print(art.logo)

    if score != 0:
        print(f"You are right! Current score: {score}")

    return_list = option(starting_dict)
    play = return_list[0].lower()
    next_time = return_list[1]

    judgement = input("Who has more followers? Type 'A' or 'B': ").lower()

    if play == judgement:
        score += 1
        print('\n' * 20)
    else:
        print(play)
        print(judgement)
        winning = False
        print('\n' * 20)

print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")

