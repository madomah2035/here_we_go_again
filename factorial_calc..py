def factorial(val):
    if type(val) is not int:
        return None
    if val < 0:
        return None
    if val == 0:
        return 1
    return val * factorial(val - 1)


factorial(3)
