import random
from data import vs, database


# insert the higher or lower logo

# choose a random character to compare with another from the same list


def format_data(choice):
    """It takes the details of the data chosen at random and returns it presentable to the user"""
    name = choice["name"]
    country = choice["country"]
    description = choice["description"]
    num_followers = choice["followers"]
    if choice == first_choice:
        return (f"{name}, a {description} from {country} with {num_followers} million followers on "
                f"Instagram.")
    else:
        return f"{name}, a {description} from {country}."


# the game itself
score = 0

not_end_of_game = True
second_choice = random.choice(database)
# print(second_choice)
while not_end_of_game:
    first_choice = second_choice
    # print(first_choice)
    second_choice = random.choice(database)
    # print(second_choice)
    while first_choice == second_choice:
        second_choice = random.choice(database)
    # print(second_choice)

    print(f"Compare A: {format_data(first_choice)}")
    print(vs)
    print(f"Against B: {format_data(second_choice)}")


    def get_user_choice(user):
        global not_end_of_game
        global score
        if user == "A":
            user = first_choice["followers"]
            if user > second_choice["followers"]:
                score += 1
                print(f"You are right! Your score is {score}.")
            else:
                print(f"You are wrong! Your final score is {score}.")
                not_end_of_game = False
        else:
            user = second_choice["followers"]
            if user > first_choice["followers"]:
                score += 1
                print(f"You are right! Your score is {score}.")
            else:
                print(f"Sorry, that's wrong! Your final score is {score}.")
                not_end_of_game = False


    user_choice = input("Who do you think has more followers? A or B: ").lower()

    get_user_choice(user=user_choice)
