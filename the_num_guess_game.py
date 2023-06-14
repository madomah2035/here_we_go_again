import random


def play_game():
    print('''
     _     _     _     ____  _________    ______     _________  ____  _  _     _____   _________  _     _____  
/ \  // \ /\/ \__//  _ \/  __/  __\  /  __/ \ /\/  __/ ___\/ ___\/ \/ \  //  __/  /  __/  _ \/ \__//  __/  
| |\ || | ||| |\/|| | //|  \ |  \/|  | |  | | |||  \ |    \|    \| || |\ || |  _  | |  | / \|| |\/||  \    
| | \|| \_/|| |  || |_\\|  /_|    /  | |_// \_/||  /_\___ |\___ || || | \|| |_//  | |_// |-||| |  ||  /_   
\_/  \\____/\_/  \\____/\____\_/\_\  \____\____/\____\____/\____/\_/\_/  \\____\  \____\_/ \|\_/  \\____\                                                                                                         
    ''')
    print("Welcome to The Guessing Number Game!\nI am thinking of a whole number between 1 and 100.")
    choice = random.randint(1, 100)
    print(f"This is a hint to help me debug my programme; the number is: {choice}")

    lives = 0
    difficulty_level = input("Type 'easy' or 'hard' for the level you want to play: ").lower()

    if difficulty_level == "easy":
        lives = 10
        print(f'You have {lives} guesses to guess right.')
    elif difficulty_level == "hard":
        lives = 5
        print(f'You have {lives} guesses to guess right.')
    else:
        print(f'Wrong level, please input the right instruction.')
        return

    continue_guessing = True

    while continue_guessing:
        player_guess = int(input("Guess the number: "))
        if player_guess < choice:
            lives -= 1
            print(f"Too low!\nGuess again\nYou have {lives} live(s) left.")
        elif player_guess > choice:
            lives -= 1
            print(f"Too high!\nGuess again\nYou have {lives} live(s) left.")
        elif player_guess == choice:
            print(f"You guessed right, that's the number I was thinking about; Congrats!")
            continue_guessing = False

        if lives != 0:
            pass
        else:
            print("You ran out of guesses, game over!")
            continue_guessing = False


play_game()

# wanna_play_again = input("Want to play a guessing number game? (Y/N): ").lower()
# while wanna_play_again == 'y':
#     print("Welcome to The Guessing Number Game!\n I am thinking of a whole number between 1 and 100.")
#     play_game()
# else:
#     pass
