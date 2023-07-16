# TODO: 1. prompt user by asking which flavor they want(Latte, Cappuccino and Espresso)
make_a_cup_of_coffee = True
choice_of_flavor = input("Which flavor would you like:(Latte(l)/Cappuccino(c)/Espresso(e)").lower()


# TODO: 2. Turn off the coffee machine by typing "off" in the prompt
def off():
    global make_a_cup_of_coffee
    if choice_of_flavor == "off":
        make_a_cup_of_coffee = False


# TODO: 3. By typing "report", you should show the user how much of every ingredient is left.
def report():
    if choice_of_flavor == "report":
        resources()


# TODO: 4. Check how much resources is left after the user chooses the flavor they want
def resources():
    started_with = [
        {"water(ml)": 300},
        {"milk(ml)": 200},
        {"coffee(g)": 100},
        {"money($)": 0}
    ]
    return started_with


# TODO: 5. Coin operated i.e; it should calculate how much coins you have given it
def coins():
    # penny = 1 cent == $ 0.01
    penny = int(input("How many pennies? "))

    # nickel = 5 cents == $ 0.05
    nickel = int(input("How many nickels? "))

    # dime = 10 cents == $ 0.10
    dime = int(input("How many dimes?"))

    # quarter = 25 cents == $ 0.25
    quarter = int(input("How many quarters?"))


# TODO: 6. Tell whether the user gets a change or it's not enough or it's just sufficient to make the coffee
# def flavors():
# if choice_of_flavor == "Latte":
#     water = 50
#     coffee = 18
flavors = [
    {"flavor": "Expresso", "water(ml)": 50, "coffee(g)": 18, "milk(ml)": 0},
    {"flavor": "Latte", "water(ml)": 200, "coffee(g)": 24, "milk(ml)": 150},
    {"flavor": "Cappuccino", "water(ml)": 250, "coffee(g)": 24, "milk(ml)": 100}
]

# TODO: 7. Check the success of the transaction and make the coffee
