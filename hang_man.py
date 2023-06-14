import random

print(""" 
                             -
                            | |
                            | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
                            | '_ \ / _` | '_ \ / _' | '_ ` _ \ / _` | '_  \ 
                            | | | | (_| | | | | (_| | | | | | | (_| | | | |  
                            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                                __/ |
                                               |___/
WELCOME TO THE HANGMAN GUESS GAME!
""")

life_stages_6 = ['''
     +---+
     |   |   
     O   |
    /|\  |
    / \  |
 ===========	
''']
life_stages_5 = ['''
				+---+
				|   |   
				O   |
			   /|\  |
			   /   |
			===========
''']
life_stages_4 = ['''
				+---+
				|   |   
				O   |
			   /|\  |
			        |
			===========
''']
life_stages_3 = ['''
				+---+
				|   |   
				O   |
			   /|   |
			        |
			        |
			===========
''']
life_stages_2 = ['''
                +---+
                |   |   
                O   |
                |   |
                    |
                    |
                =======
''']
life_stages_1 = ['''
                +---+
                |   |   
                O   |
                    |
                    |
                    |
                =======
''']
life_stages_0 = ['''
                +---+
                |   |
                    |
                    |
                    |
                    |
                =======    
''']

print(life_stages_6)
myList = ["bugatti", "limousine", "mercedes", "lexus", "honda", "hyundai", "ford", "bmw", "opel", "toyota"]
random_chosen_brand = random.choice(myList)
# print(f'The chosen brand is: {random_chosen_brand}')

not_end_of_game = True
lives = 6

display = []
for char in random_chosen_brand:
    display.append('_')
print(f'The word to be guessed has as many letters as there are "_" in the list in: {display}')
while not_end_of_game:
    user_guess = input("Guess a letter in the name of any popular car brand: ").lower()
    for index in range(len(random_chosen_brand)):
        character = random_chosen_brand[index]
        if user_guess == character:
            display[index] = user_guess
    # for alphabet in random_chosen_brand:
    if user_guess in display:
        print(f'Hey, you\'ve guessed {user_guess} already. Guess a different letter.')
    if user_guess not in random_chosen_brand:
        lives -= 1
        print(f'Sorry, you guessed wrong so you lose a life... and you have {lives} live(s) to still be in the game.')
    if lives == 0:
        not_end_of_game = False
        print(f"Oops! You have {lives} live(s) left and you lose.")
    print(f'{display}')

    display_string = "".join(display)

    if "_" not in display:
        not_end_of_game = False
        print(f"You win! The word you guessed is {display_string.upper()} and that's the computer's chosen word.")
