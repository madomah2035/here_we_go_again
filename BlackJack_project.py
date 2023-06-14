# import random
#
# print("Welcome to the BlackJack Game!\n")
# interact = input("Would you like to play? (Y/N): ").lower()
# if interact == "y":
#     def deal_cards():
#         deal = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#         for _ in range(2):
#             dealer = [random.choice(deal)]
#             print(f'Dealer\'s hand: {dealer[0]}')
#
#             player_choice = [random.choice(deal)]
#             print(f"Your hand: {player_choice}")
# deal_again = input("Would you like dealer to deal you in again?: (Y/N) ").lower()
#     if deal_again == "y":
#         deal_cards()
#
#     else:
#
#         for a in dealer:
#             sum_of_dealer = sum(dealer)
#             player_sum = sum(player_choice)
#             if 17 > sum_of_dealer or player_sum:
#                 player_choice.append(random.choice(deal))
#                 print(f"Your hand: {player_choice}")
#                 dealer.append(random.choice(deal))
#                 print(f'Dealer\'s hand: {dealer}')
#                 if sum_of_dealer == player_sum:
#                     print(f"You both have {sum_of_dealer}, It's a draw!")
#                 elif sum_of_dealer > 21:
#                     print(f"You win with {player_sum}")
#                 elif player_sum > 21:
#                     print(f"Dealer wins with {sum_of_dealer}")
#                 elif 21 < sum_of_dealer and player_sum:
#                     if player_sum > sum_of_dealer:
#                         print(f"You win with {player_sum}")
#                 else:
#                     print(f"Dealer wins with {sum_of_dealer}")
#             else:
#
#                 if sum_of_dealer == player_sum:
#                     print(f"You both have {sum_of_dealer}, It's a draw!")
#                 elif sum_of_dealer > 21:
#                     print(f"You win with {player_sum}")
#                 elif player_sum > 21:
#                     print(f"Dealer wins with {sum_of_dealer}")
#                 elif 21 < sum_of_dealer and player_sum:
#                     if player_sum > sum_of_dealer:
#
#                         print(f"You win with {player_sum}")
#                     else:
#                         print(f"Dealer wins with {sum_of_dealer}")
#
#                 # elif 17 > sum_of_dealer and player_sum:
#             #     player_choice.append(random.choice(deal))
#             #     print(f"Your hand: {player_choice}")
#             #     dealer.append(random.choice(deal))
#             #     print(f'Dealer\'s hand: {dealer}')
