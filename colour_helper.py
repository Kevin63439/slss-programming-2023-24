# Colour helper
# Author: Kevin Wong
# December 13 2023

def pixel_to_string(pixel: tuple) -> str:
    """Take a rgb 3-tuple and "interpret it"
    as a colour and return that colour's name

    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel

    if g > 125 and r < 100 and b < 100:
        return "green"


def is_light(pixel: tuple) -> bool:
    """Returns true if given pixel is "light"
    
    Params: 
    pixel - 3-tuple of values red. green, blue
    
    Returns:
        True if pixel is light false if not
    """
    return pixel >= (128,128,128)

    average = (red + green + blue) / 3

    if average >= 128:
        return True
    else:
        return False

    return

black_pixel = (0,0,0)
dark_gray_pixel = (127,127,127)
light_gray_pixel = (128,128,128)
white_pixel = (255,255,255)

print(is_light(black_pixel))   # False
print(is_light(dark_gray_pixel))  # False
print(is_light(light_gray_pixel))  # True
print(is_light(white_pixel))    # True


