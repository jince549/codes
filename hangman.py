import random
hangman_stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |    
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |    
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |    
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |    
    ---
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |    
    ---
    """,
    """
     ------
     |    |
     |    O
     |    
     |    
     |    
    ---
    """,
    """
     ------
     |    |
     |    
     |    
     |    
     |    
    ---
    """
]

fruits = ["apple", "banana", "orange", "grape", "mango", "pineapple", "strawberry", "blueberry", "watermelon", "kiwi"]
life = 6
def word(lst):
    choosen_word = random.choice(lst)
    return choosen_word


def placeholder(wrd):
    display = ""
    for i in range(len(wrd)):
        display += "_"
    return display

def guessed_letter():
    letter = input("Please guess a letter :")
    return letter

def display_dash(wrd, gue, lst):
    letter_and_dash = ""
    for i in wrd:
        if gue == i:
            letter_and_dash += i
            lst.append(i)
        elif i in lst:
            letter_and_dash += i
        else:
            letter_and_dash += "_"
    return letter_and_dash


def guessed_or_not(gue, lst):
    if gue in lst:
        print(f"{gue} already guessed")
    
def life_remain(wrd, gue, lyf):
    if gue not in wrd:
        print(f"{gue} not in the word")
        lyf -= 1
        if lyf == 0:
            print(f"************************ YOU LOSE!!!************************\nThe word is {picked_word}")
            global gameover
            gameover = True
    return lyf
 

def win(wrd_dash):
    if "_" not in wrd_dash:
        print("************************ YOU WIN!!!************************")
        global gameover
        gameover = True
    

picked_word = word(fruits)
# print(picked_word)

word_list = []
gameover = False

dashes = placeholder(picked_word)
print(dashes)
while not gameover: 
    guess = guessed_letter()
    guessed_or_not(guess, word_list)
    word_dash = display_dash(picked_word, guess, word_list)
    print(word_dash)
    life = life_remain(picked_word, guess, life)
    win(word_dash)

    print(hangman_stages[life])
