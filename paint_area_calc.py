from math import ceil


def cans_of_paint(name, wall_length, wall_width):
    cans = ceil((wall_length * wall_width) / one_can_of_paint_covers)
    print(f'{name}, you will need {cans} cans of paint to paint your wall.')


one_can_of_paint_covers = 5
length = int(input("Input height of wall in meters: "))
width = int(input("Enter width of wall in meters: "))

cans_of_paint("Nana", wall_width=width, wall_length=length)
