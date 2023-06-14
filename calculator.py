# # # def add(x, y):
# # #     return x + y
# # #
# # #
# # # def subtract(x, y):
# # #     return x - y
# # #
# # #
# # # def multiply(x, y):
# # #     return x * y
# # #
# # #
# # # def divide(x, y):
# # #     return x / y
# # #
# # #
# # # solution = {
# # #     "+": add,
# # #     "-": subtract,
# # #     "*": multiply,
# # #     "/": divide
# # # }
# # #
# # # x = int(input("Enter first number: "))
# # #
# # # for operator in solution:
# # #     print(operator)
# # # choice = input("Pick an operator: ")
# # #
# # # y = int(input("Enter second number: "))
# # #
# # # if choice == "+":
# # #     result = add(x=x, y=y)
# # #     print(f'{x} {choice} {y} = {add(x=x, y=y)}')
# # # elif choice == "*":
# # #     result = multiply(x=x, y=y)
# # #     print(f'{x} {choice} {y} = {multiply(x=x, y=y)}')
# # # elif choice == "-":
# # #     result = subtract(x=x, y=y)
# # #     print(f'{x} {choice} {y} = {subtract(x=x, y=y)}')
# # # else:
# # #     result = divide(x=x, y=y)
# # #     print(f'{x} {choice} {y} = {divide(x=x, y=y)}')
# # #
# # # end_calc = False
# # # continue_calc = input("press 'y' to continue calculation or 'n' to quit. ")
# # # while not end_calc:
# # #     if continue_calc == "y":
# # #         pick_another = input("Pick another operator: ")
# # #         z = int(input("Enter another number: "))
# # #         for another_op in pick_another:
# # #             if another_op in solution:
# # #                 op_2 = solution[pick_another]
# # #                 calc = op_2(result, z)
# # #                 print(f"{result} {pick_another} {z} = {calc}")
# # #                 result = calc
# # #
# # #     else:
# # #         end_calc = True
# #
# #
# # # I could have totally prevented myself from all the stress and gone with this
# #
#
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


def calculator():
    x = int(input("Enter first number: "))

    for operator in solution:
        print(operator)
    operator_choice = input("Pick an operator: ")

    y = int(input("Enter second number: "))

    calculations = solution[operator_choice]
    answer = calculations(x, y)
    print(f"{x} {operator_choice} {y} = {answer}")

    continue_loop = True
    while continue_loop:
        another = input("Want to calculate again? 'Y' to continue with previous ans or 'N' to start fresh "
                        "calculations: ").lower()
        if another == 'y':
            pick = input("Pick another operator: ")
            z = int(input("Enter another number: "))
            answer_2 = solution[pick](answer, z)
            print(f"{answer} {pick} {z} = {answer_2}")
            answer = answer_2
        else:
            continue_loop = False
            calculator()


calculator()
# import os
#
#
# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
#
# def divide(x, y):
#     return x / y
#
#
# solution = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }
#
#
# def clear_console():
#     # Clear console output
#     os.system('clear')
#
#
# def calculator():
#     print("Welcome to the calculator!")
#     previous_result = None
#     while True:
#         if previous_result is not None:
#             print("Previous result:", previous_result)
#
#         x = previous_result or float(input("Enter the first number: "))
#
#         clear_console()
#
#         for operator in solution:
#             print(operator)
#         operator_choice = input("Pick an operator (+, -, *, /): ")
#
#         y = float(input("Enter the second number: "))
#
#         calculations = solution.get(operator_choice)
#         if calculations:
#             answer = calculations(x, y)
#             print(f"{x} {operator_choice} {y} = {answer}")
#             previous_result = answer
#         else:
#             print("Invalid operator choice!")
#
#         another = input("Want to perform another calculation? (Y/N): ")
#         if another.lower() != 'y':
#             print("Thank you for using the calculator!")
#             break
#         else:
#             clear_console()
#             calculator()
#
#
# # Start the calculator
# calculator()
