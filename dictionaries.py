# # dictionaries in python are very common to dictionaries in real life; let's take a quick look at a "pytionary" as I
# # will call it
#
#
# my_Dictionary = {
#     "Ugh": "Used to express disgust or horror.",
#     "Sigh": "emit a long, deep, audible breath expressing sadness, relief, tiredness, or a similar feeling: Harry "
#             "sank into a chair and sighed with relief"
#
# }
# # retrieving info from a dictionary in python
# print(my_Dictionary["Ugh"])
#
# # adding elements to a dictionary; I can make changes to a dictionary using this method as well.
# my_Dictionary["Rage"] = "violent, uncontrollable anger."
#
# print(my_Dictionary)
#
# # one can also start out to create a new dictionary with the empty {}; this can also be used to wipe out an already
# # existing dictionary
# # I can loop through a dictionary by using the for loop, for instance.
# for element in my_Dictionary:
#     print(element)  # this prints only the key
#     print(my_Dictionary[element])  # this prints the value of the given key.
#
# countries = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon", "Marseille"], "num_of_visits": [2, 1, 3, 2]},
#     "Canada": {"cities_visited": ["Ontario", "Toronto"], "num_of_visits": [3, 5]}
# }
# print(countries["Canada"])

travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon", "Marseille"],
     "num_of_visits": 5},

    {"country": "Canada",
     "cities_visited": ["Ontario", "Toronto"],
     "num_of_visits": 8}
]


def add_new_country(country_vis, cities, visits):
    new_country = {"country": country_vis, "cities_visited": cities, "num_of_visits": visits}
    travel_log.append(new_country)
    print(new_country)
    print(travel_log)


add_new_country("Ghana", ["Kumasi", "Berekum", "Accra"], [10, 30, 3])

# print(travel_log[0])

# not_end_of_bid = True
# while not_end_of_bid:
#     name = input("Enter name here: ").capitalize()
#     bid = int(input("Enter your bid here: $"))
#
#     bidders = {name: bid}
#     other_bidders = input("Are there other bidders? Yes or No ").lower()
#     if other_bidders == 'no':
#         not_end_of_bid = False
#         print(f'{name} is the winner with a bid of ${bid}')
#     for a in bidders:
#         highest_bid = 0
#         if bidders[name] > highest_bid:
#             result = f'{name} is the highest bidder'
#
# #     def declare_winner(name1, bid1):
# #         for a in bidders:
# #             a = bidders[name1]
# #             highest_bid = 0
# #             if a > highest_bid:
# #                 print(a)
# #         print(f'{name1} is the winner with a bid of ${bid1}')
# #
# # declare_winner(name1=name, bid1=bid)
