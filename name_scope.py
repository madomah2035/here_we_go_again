age = 0  # global  variable


def increase_age():
    for _ in range(1, 10):
        # global age
        return age + _  # local variable
    # print(age)


print(increase_age())
print(age)

