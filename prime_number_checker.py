def prime_num_check(number):
    not_prime = True
    # not_odd = True
    for num in range(2, number - 1):
        if number % num == 0:
            not_prime = False

    # for n in number:
    #     if number % 2 != 0:
    #         not_odd = False
    #     print('This is an odd number.')
    # else:
    #     print("This is an even number.")

    if not_prime:
        print("This is a prime number.")
    else:
        print("This is not a prime number.")


n = int(input("Enter the number to check: "))
prime_num_check(number=n)
