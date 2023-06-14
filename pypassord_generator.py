import random

program_name = "PyPassword Generator"
alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ' \
        'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alpha = alpha.split()
# print(alpha)
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["_", "@", "-", ".", "<", ">", "/", "!", "*", "#", "$", "%", "^", "&", "(" "~", ")", "|", '?']
name = input("Tell us your name: ")
name_correct = name.capitalize()
msg = f"Hello {name_correct}, a warm welcome from the {program_name} team."
print(msg)
num_of_alpha = int(input("How many alphabets would you like in your password?\n: "))
num_of_numerals = int(input("How many numbers would you like in your password?\n: "))
num_of_symbols = int(input("How many symbols would you like in the password?\n: "))

password_alpha = ""
for a in range(1, num_of_alpha + 1):
    random_alpha = random.choice(alpha)
    password_alpha += str(random_alpha)
print(password_alpha)

password_num = ""
for n in range(1, num_of_numerals + 1):
    random_num = random.choice(num)
    password_num += str(random_num)
print(password_num)

password_symbols = ""
for s in range(1, num_of_symbols + 1):
    random_symbol = random.choice(symbols)
    password_symbols += str(random_symbol)
print(password_symbols)

# I will put all the pieces together.
result = password_alpha + password_num + password_symbols

# here, I will convert the result into a list, so I can alter the order since strings are immutable
password_list = list(result)
# print(password_list)

# the next line shuffles the elements of the list just created
random.shuffle(password_list)
# print(password_list)
# in order to concatenate, I have to convert to string and join the elements since in list, they are separated with ","
password_string = "".join(password_list)
# print(password_string)
password = 'Your password is: ' + password_string
print(password)
