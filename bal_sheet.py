def cal_bal():
    bal_before = float(input("Enter your previous balance: "))
    expenditure = []

    while True:
        daily_exp = float(input("Enter your expenses: "))
        expenditure.append(daily_exp)
        if daily_exp == 0:
            break

    balance = check_bal(bal_before, expenditure)
    print(f"Your new balance today is {bal_before} - {sum(expenditure)} = GHC{balance}")


def check_bal(x, y):
    bal = x - sum(y)
    return bal


cal_bal()
