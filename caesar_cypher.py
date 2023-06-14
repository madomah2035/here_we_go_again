# alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z'
# alpha = alphabet.split()
# end_of_game = False
#
# while end_of_game:
#     what_to_do = input("Type 'encode' to encrypt and 'decode' to decrypt\n:")
#     message = input("Enter your message here\n:").lower()
#     shift_num = int(input("Enter your shift number\n:"))
#
#     go_again = input("Want to go again? Yes or No \n").lower()
#     if go_again == 'no':
#         end_of_game = True
#         print("Goodbye, cone back again soon!")
#     else:
#         end_of_game = False
#
# new_msg = []
#
#
# def encrypt(msg, shift):
#     shift %= 25
#     encrypted_msg = ''
#     for char in msg:
#         if char in alpha:
#             char_position = alpha.index(char)
#             char = alpha[char_position + shift]
#             new_msg.append(char)
#             encrypted_msg = ''.join(new_msg)
#         else:
#             new_msg.append(char)
#             print(f'Your encrypted message is {encrypted_msg}.')
#
#
# encrypt(msg=message, shift=shift_num)

# alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z'
# alpha = alphabet.split()
# end_of_game = False
#
# while not end_of_game:  # Changed from "end_of_game" to "not end_of_game"
#     what_to_do = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")  # Removed unnecessary ":" from input
#     # prompt
#     message = input("Enter your message here:\n").lower()
#     shift_num = int(input("Enter your shift number:\n"))
#
#     go_again = input("Want to go again? Yes or No:\n").lower()
#     if go_again == 'no':
#         end_of_game = True
#         print("Goodbye, come back again soon!")
#     else:
#         end_of_game = False
#
#
#     def encrypt(msg, shift):
#         shift %= 26  # Changed from "25" to "26"
#         encrypted_msg = ''
#         for char in msg:
#             if char in alpha:
#                 char_position = alpha.index(char)
#                 char = alpha[char_position + shift]
#                 encrypted_msg += char  # Concatenate to encrypted_msg
#             else:
#                 encrypted_msg += char  # Concatenate to encrypted_msg
#         print(f'Your encrypted message is {encrypted_msg}.')  # Moved outside the loop
#
#
#     encrypt(msg=message, shift=shift_num)  # Moved outside the else block


# def encrypt(msg, shift):
#     encrypted_msg = ''
#     for char in msg:
#         if char in alpha:
#             char_position = alpha.index(char)
#             char = alpha[char_position + shift]
#             encrypted_msg += char
#         else:
#             encrypted_msg += char
#     print(f'Your encrypted message is: {encrypted_msg}')


# encrypt(msg=message, shift=shift_num)


# def decrypt(msg, shift):
#     decrypted_msg = ''
#     for char in msg:
#         if char in alpha:
#             char_position = alpha.index(char)
#             char = alpha[char_position - shift]
#             decrypted_msg += char
#         else:
#             decrypted_msg += char
#     print(f'Your decrypted message is: {decrypted_msg}')


# decrypt(msg=message, shift=shift_num)

# if what_to_do == 'encode':
#     encrypt(msg=message, shift=shift_num)
# elif what_to_do == 'decode':
#     decrypt(msg=message, shift=shift_num)
# else:
#     print('We don\'t understand your command. Enter "encode" to encrypt and "decode" to decrypt.\n')


alphabet = 'a b c d e f g h i j k l m n o p q r s t u   v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z'
alpha = alphabet.split()
not_end_of_game = True


def caesar(command, msg, shift):
    end_text = ''
    if command == 'decode':
        shift *= -1
    for char in msg:
        if char in alpha:
            char_position = alpha.index(char)
            char = alpha[char_position + shift]
            end_text += char
        else:
            end_text += char

    print(f'Your {command}d message is: {end_text}')


while not_end_of_game:
    print('''
 _______  _______  _______  _______  _______  _______    _______           _______           _______  _______ 
(  ____ \(  ___  )(  ____ \(  ____ \(  ___  )(  ____ )  (  ____ \|\     /|(  ____ )|\     /|(  ____ \(  ____ )
| (    \/| (   ) || (    \/| (    \/| (   ) || (    )|  | (    \/( \   / )| (    )|| )   ( || (    \/| (    )|
| |      | (___) || (__    | (_____ | (___) || (____)|  | |       \ (_) / | (____)|| (___) || (__    | (____)|
| |      |  ___  ||  __)   (_____  )|  ___  ||     __)  | |        \   /  |  _____)|  ___  ||  __)   |     __)
| |      | (   ) || (            ) || (   ) || (\ (     | |         ) (   | (      | (   ) || (      | (\ (   
| (____/\| )   ( || (____/\/\____) || )   ( || ) \ \__  | (____/\   | |   | )      | )   ( || (____/\| ) \ \__
(_______/|/     \|(_______/\_______)|/     \||/   \__/  (_______/   \_/   |/       |/     \|(_______/|/   \__/
                                                                                                                                                                                   
    ''')
    what_to_do = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    message = input("Enter your message here:\n").lower()
    shift_num = int(input("Enter your shift number:\n"))
    shift_num %= 26

    caesar(command=what_to_do, msg=message, shift=shift_num)

    go_again = input("Want to go again? Yes or No:\n").lower()
    if go_again == 'no':
        not_end_of_game = False
        print("Goodbye, come back again soon!")
