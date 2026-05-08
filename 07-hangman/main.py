import random
import hangman_words
import hangman_art

check = False
lives = 6
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

while placeholder != chosen_word and lives!=0:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for i in range(0,len(chosen_word)):
        if guess==chosen_word[i]:
            if guess in placeholder:
                lives +=1
                check = True
            display +=  guess
        else:
            display += placeholder[i]
    if placeholder == display:
        lives -=1
        if check:
            check = False
            print(f"You have already guessed {guess}")
        else:
            print(f"You guessed {guess}.that's not in the word.You lose a life")

    else:
        placeholder = display
    print(f"Word to guess: {placeholder}")
    if placeholder != chosen_word and lives!=0:
        print(hangman_art.stages[lives])

if lives==0:
    print(f"****************************IT WAS {chosen_word}! You Lose!****************************")
    print()
else:
    print("****************************You Win!****************************")

print(hangman_art.stages[lives])
