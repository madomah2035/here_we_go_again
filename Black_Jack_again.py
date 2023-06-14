import random


def deal_cards():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(deck)
    return card


def calc_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return sum(cards)


def compare(player, computer):
    if player == computer:
        return "It's a draw!"
    elif player == 0:
        return "You won with a BlackJack!"  # this line is not used since the calc_score function ain't working.
    elif computer == 0:
        return "You lose, opponent has a BlackJack!"
    elif player > 21:
        return "You went over, you lose!"
    elif computer > 21:
        return "Opponent went over, you win!"
    elif player > computer:
        return "You win!"
    else:
        return "Opponent wins!"


def play_black_jack():
    player_cards = []
    computer_cards = []
    game_is_over = False
    for _ in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    player_score = sum(player_cards)
    # bugs here that need to be fixed; don't know why the calc_score function is not working.
    print(f'Your hand is: {player_cards} and you have a score of {sum(player_cards)}')
    computer_score = sum(computer_cards)
    print(f'Computer\'s first card is: {computer_cards[0]}')
    while not game_is_over:
        if player_score == 0 or computer_score == 0 or sum(player_cards) > 21:
            game_is_over = True
        else:
            deal_again = input("Do you want to draw another card? (Y/N): ").lower()
            if deal_again == "y":
                player_cards.append(deal_cards())
                player_score = calc_score(player_cards)
                print(f'Your hand is: {player_cards} and you have a score of {sum(player_cards)}')
            else:
                game_is_over = True

    while sum(computer_cards) != 0 and sum(computer_cards) < 17:
        computer_cards.append(deal_cards())
        computer_score = sum(computer_cards)
    print(f'Opponent\'s hand: {computer_cards} and a score of {computer_score}\n')

    print(f"     Your final hand is: {player_cards} and final score of {sum(player_cards)}")
    print(f"     Opponent\'s final hand is: {computer_cards} and a score of {sum(computer_cards)}")
    result = compare(player=sum(player_cards), computer=sum(computer_cards))
    print(result)


while input("Do you want to play a game of Black_Jack? (Y/N): \n").lower() == "y":
    print("Hello, Welcome to the BlackJack deck; let's have fun!\n")
    play_black_jack()

# will have to modify it later and fix bugs as well, but it's fine for now...
