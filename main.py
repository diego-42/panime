import sys

from PIL import Image

CHARS = [".", ",", ":", ";", "+", "?", "%", "$", "#", "@"]
WIDTH = 300

def resize_image(image, new_width = WIDTH):
    old_width, old_height = image.size

    aspect_ratio = old_height / old_width
    new_height = int(aspect_ratio * new_width * 0.55)

    return image.resize((new_width, new_height))

def grayscalify(image):
    return image.convert("L")

def convert_image_to_pixels(image):
    pixels = list(image.getdata())

    return "".join(CHARS[pixel // 25] for pixel in pixels)

def construct_image_from_pixels(pixels, width = WIDTH):
    len_pixels = len(pixels)

    image = [pixels[index:index + width] for index in range(0, len_pixels, width)]

    return "\n".join(image)

def image_to_ascii(image):
    image_resized = resize_image(image)
    image_grayscale = grayscalify(image_resized)

    pixels_of_image = convert_image_to_pixels(image_grayscale)

    image_ascii = construct_image_from_pixels(pixels_of_image)

    return image_ascii

def main():
    try:
        path = sys.argv[1]
        image = Image.open(path)
    except:
        print("USAGE: python3 main.py  <image/path.jpg>")
        exit()

    image = image_to_ascii(image)

    print(image)

if __name__ == "__main__":
    main()