"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'


def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # assign simba picture to name 'simba_pic'
    simba_pic = SimpleImage(PATCH_NAME)
    # simba_pic = make_recolored_patch(1.5, 0, 1.5)

    for x_patches in range(N_COLS):
        for y_patches in range(N_ROWS):
            # # pull all pixels from 'simba_pic', set to 'final image'
            # in original location
            for y in range(PATCH_SIZE):
                for x in range(PATCH_SIZE):
                    pixel = simba_pic.get_pixel(x, y)
                    # this works for single image
                    # final_image.set_pixel(x, y, pixel)
                    # looking for multiple columns here
                    final_image.set_pixel((x + (PATCH_SIZE * x_patches)), (y + (PATCH_SIZE * y_patches)), pixel)
            simba_pic = make_recolored_patch(x_patches, y_patches, N_COLS)
        # makes pink
        # make_recolored_patch(1.5, 0, 1.5)

    # # This is an example which should generate a pinkish patch
    # patch = make_recolored_patch(1.5, 0, 1.5)

    simba_pic.show()
    final_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
        # pixel.red == red_scale
        # pixel.green == green_scale
        # pixel.blue == blue_scale
    return patch

if __name__ == '__main__':
    main()

