# Function Practice
# Author" Kevin Wong
# November 24 2023

def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.
    Params:
    sidelength - length of one side of the square
    """
    area = sidelength**2
    return area
def print_area_of_a_square(sidelength: float) -> None:
    """Calculate and print the area of a square.
    Results are in units squared.
    Params:
    sidelength - length of one side of the square
    """
    area = sidelength**2
    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )
print(print_area_of_a_square(12.2))
# print_area_of_a_square(12)
# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares
# area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
# print(area_of_squares)

# Question 1
def stars(num_stars: int) -> str:
    """Returns a number of stars
    
    Params:
    
    num_stars - the number of stars to return
    """

    return "*" * num_stars


print(stars(100))

# Question 2
def biggest_of_three(num_1: int, num_2: int, num_3: int) -> int:
    """Returns biggest number out of three
    
    Params:
    
    biggest_num - the biggest number out of the three
    """

    if num_1 > num_2 and num_1 > num_3:
        return num_1
    if num_2 > num_1 and num_2 > num_3:
        return num_2
    if num_3 > num_1 and num_3 > num_2:
        return num_3
    
print(biggest_of_three(100,1000,10000))

# Question 3
# Question 4
# Create functions called pyramid() and pyramid_mirror()
# Takes one number as a parameter
# Give a pyramid either regular way or mirrored

def pyramid(num_layers: int) -> None:
    """Returns a pyramid of stars
    
    Params:
    
    num_layers - the number of layers of stars in the pyramid
    """

    for current_layers in range(1, num_layers):
        print(stars(num_layers)) 

pyramid (2)
pyramid (3)
pyramid (4)
pyramid (5)


def pyramid(num_layers: int) -> None:
    """Prints out a mirrored pyramid
    
    Params:
    
    num_layers - the number of layers of stars in the pyramid
    """

    for current_layer in range(1, num_layers+1):
        # Print the spaces then print the stars
        # " " * 1 + stars(1)
        # "" * 0 + stars(2) 
        # num_layers == 3
        # " " * 2 + stars(1)
        # " " * 1 + stars(2)
        # " " * 0 + stars(3)
        print(" " * + stars(current_layer))