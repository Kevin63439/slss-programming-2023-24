import colour_helper
from PIL import Image
#Recall that we can open up files in Python
with Image.open("./Images/best_pizza.jpg") as im:
    # Algorithm to visit every pixel in the kid-green
    # Store the height and width of the image
    image_height = im.height
    image_width = im.width
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))
            # Check pixel if it's green
            if colour_helper.is_light(pixel):
                # replace with bg_pixel
                im.putpixel((x, y), (255,255,255)) 
            else:
                im.putpixel((x,y), (0,0,0))

# Save the image
im.save("./Images/output.jpg")