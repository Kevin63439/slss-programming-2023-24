# Robot dog
# Kevin Wong
# January 12 2024

from PIL import Image

red_ball_img = Image.open("./Images/Red Ball.jpeg")

red_pixels = []

def is_red(pixel:tuple)->bool: 
    r,g,b = pixel 
    return r>200 and g<100 and b<100

def middle():
    for y in range(red_ball_img.height):
        for x in range(red_ball_img.width):
            current_pixel = red_ball_img.getpixel((x, y))

            if is_red(current_pixel):
                red_pixels.append((x, y))

    mid_x = sum(coord[0] for coord in red_pixels) / len(red_pixels)
    mid_y = sum(coord[1] for coord in red_pixels) / len(red_pixels) 
    return f'{mid_x}, {mid_y}'

print (middle())

red_ball_img.close()
