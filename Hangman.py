import random
from word_list import word_list
from stages import stages
end_of_game=False

choosen_word=random.choice(word_list)
lives=6
word_length=len(choosen_word)
display=[]
for _ in range(word_length):
    display +="_"


while not end_of_game:
    guess=input("Guess the letter").lower()
    if guess in display:
        print(f"you already guessed the leter {guess}")
    for position in range(word_length):
        letter=choosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in choosen_word:
        print(f"you guessed {guess} that's not in the word, you lose a life")
        lives -= 1
        if lives==0:
            end_of_game=True
            print("you lose")
        
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("you win")
    
    print(stages[lives])