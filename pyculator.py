def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


solution = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def do_the_math():
    x = float(input("Enter first number: "))
    continue_calculation = True
    while continue_calculation:
        choice_of_operator = input("Choose your operator (+, -, *, /): ")
        y = float(input("Enter the next number: "))
        calculation = solution[choice_of_operator]
        result = calculation(x, y)
        print(f'{x} {choice_of_operator} {y} = {result}')

        wanna_go_again = input("Want to continue with the previous answer? (Y/N): ").lower()
        if wanna_go_again == 'y':
            x = result
        else:
            continue_calculation = False
            do_the_math()


do_the_math()

# choice_of_operator = input("Choose another operator (+, -, *, /): ")
# z = float(input("Enter the next number: "))
# calculation = solution[choice_of_operator]
# result1 = calculation(result, z)
# print(f'{result} {choice_of_operator} {z} = {result1}')
