from PIL import Image

def create_avatar(path: str)->None:
    image = Image.open(path)

    red, green, blue = image.split()

    red_cropped_left = red.crop((50, 0, red.width, red.height))
    red_cropped = red.crop((25, 0, red.width - 25, red.height))
    final_red = Image.blend(red_cropped_left, red_cropped, 0.5)

    blue_cropped_right = blue.crop((0, 0, blue.width - 50, blue.height))
    blue_cropped = blue.crop((25, 0, blue.width - 25, blue.height))
    final_blue = Image.blend(blue_cropped_right, blue_cropped, 0.5)

    green_cropped = green.crop((25, 0, green.width - 25, green.height))

    merged_image = Image.merge("RGB", (final_red, green_cropped, final_blue))
    merged_image.thumbnail((80, 80))
    merged_image.save('monro_80x80.jpg')

