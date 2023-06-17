def profit(num_of_days, initial_capital):
    overall_profit = initial_capital
    daily_interest = 2 / 100
    for num in range(num_of_days):
        investing_capital = initial_capital - 0.062499
        daily_gain = investing_capital * daily_interest
        overall_profit += daily_gain
        overall_profit = round(overall_profit, 2)
    print(f"Your compound profit over {num_of_days} days will be: ${overall_profit}")


end_of_calc = True
while end_of_calc:
    principal = float(input('Enter your capital:$ '))
    days = int(input('How many days are you looking to invest? '))
    profit(num_of_days=days, initial_capital=principal)
    go_again = input("calculate again? (Y/N): ").lower()
    if go_again != "y":
        end_of_calc = False
