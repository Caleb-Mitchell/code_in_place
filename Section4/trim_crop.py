from simpleimage import SimpleImage

DEFAULT_FILE = 'images/karel.png'
TRIM_SIZE = 30

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original karel
    original_karel = SimpleImage(filename)
    original_karel.show()

    # Show karel with the image cropped
    trim_size = TRIM_SIZE
    cropped_karel = trim_crop_image(filename, trim_size)
    cropped_karel.show()


def trim_crop_image(filename, trim_size):
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    cropped_image = SimpleImage.blank(width - (trim_size * 2), height - (trim_size * 2))
    # cropped_image = SimpleImage.blank(width, height)

    for y in range(0, (height - (trim_size * 2))):
        for x in range(0, (width - (trim_size * 2))):
            pixel = image.get_pixel((0 + trim_size), (0 + trim_size))
            cropped_image.set_pixel(x, y, pixel)
    return cropped_image


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
