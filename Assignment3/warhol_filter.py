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
    color = 0
    # assign simba picture to name 'simba_pic'
    simba_pic = SimpleImage(PATCH_NAME)

    for x_patches in range(N_COLS):
        for y_patches in range(N_ROWS):
            simba_pic = color_patch(color, simba_pic)
            color += 1
            for y in range(PATCH_SIZE):
                for x in range(PATCH_SIZE):
                    pixel = simba_pic.get_pixel(x, y)
                    final_image.set_pixel((x + (PATCH_SIZE * x_patches)), (y + (PATCH_SIZE * y_patches)), pixel)

    final_image.show()


def color_patch(color, simba_pic):
    if color == 0:
        simba_pic = make_recolored_patch(1.5, 0, 1.5)
    elif color == 1:
        simba_pic = make_recolored_patch(2, 2, 2)
    elif color == 2:
        simba_pic = make_recolored_patch(0, 1.5, 1.5)
    elif color == 3:
        simba_pic = make_recolored_patch(0, 0, 1.5)
    elif color == 4:
        simba_pic = make_recolored_patch(1.5, 1.5, 0)
    elif color == 5:
        simba_pic = make_recolored_patch(.5, .5, .5)
    return simba_pic

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
    return patch

if __name__ == '__main__':
    main()
