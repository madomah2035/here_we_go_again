# TODO: 1. prompt user by asking which flavor they want(Latte, Cappuccino and Espresso)
make_a_cup_of_coffee = True
choice_of_flavor = input("What would you like:(Latte(l)/Cappuccino(c)/Espresso(e): ").lower()


# TODO: 2. Turn off the coffee machine by typing "off" in the prompt
def off():
    global make_a_cup_of_coffee
    if choice_of_flavor == "off":
        return
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
    print("Insert your coins here.")
    coin = 0
    # penny = 1 cent == $ 0.01
    num_penny = int(input("How many pennies? "))
    coin += 0.01 * num_penny

    # nickel = 5 cents == $ 0.05
    num_nickel = int(input("How many nickels? "))
    coin += 0.05 * num_nickel

    # dime = 10 cents == $ 0.10
    num_dime = int(input("How many dimes?"))
    coin += 0.10 * num_dime

    # quarter = 25 cents == $ 0.25
    num_quarter = int(input("How many quarters?"))
    coin += 0.25 * num_quarter
    return coin


# TODO: 6. Tell whether the user gets a change or it's not enough or it's just sufficient to make the coffee
def flav():
    flavors = [
        {"flavor": "Expresso", "water(ml)": 50, "coffee(g)": 18, "milk(ml)": 0, "price": 1.50},
        {"flavor": "Latte", "water(ml)": 200, "coffee(g)": 24, "milk(ml)": 150, "price": 2.50},
        {"flavor": "Cappuccino", "water(ml)": 250, "coffee(g)": 24, "milk(ml)": 100, "price": 3.00}
    ]

    price = flavors["price"]
    coffee = flavors["flavor"]

    if choice_of_flavor == flavors["flavor"]:
        print(f"That'll be ${price} for a cup of {coffee}")


# TODO: 7. Check the success of the transaction and make the coffee
def make_the_coffee():
    off()
    resources()
    flav()


make_the_coffee()
