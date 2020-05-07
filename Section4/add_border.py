from simpleimage import SimpleImage

BORDER_SIZE = 10

DEFAULT_FILE = 'images/simba-sq.jpg'


def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original image
    original_image = SimpleImage(filename)
    original_image.show()

    # Show image with a black border
    bordered_image = add_border(filename, BORDER_SIZE)
    bordered_image.show()


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    original_img = SimpleImage(original_img)
    bordered_image = SimpleImage.blank((original_img.width + (border_size * 2)),
                                       (original_img.height + (border_size * 2)), 'black')

    # could also include a for each loop to create totally black background *first*,
    # or, could try to implement a second double 4 loop to add black only in the border_with sized edges
    # or, just use the .blank method parameter of a back_color, implemented here.

    for y in range(original_img.height):
        for x in range(original_img.width):
            pixel = original_img.get_pixel(x, y)
            bordered_image.set_pixel(x + border_size, y + border_size, pixel)
    return bordered_image


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
