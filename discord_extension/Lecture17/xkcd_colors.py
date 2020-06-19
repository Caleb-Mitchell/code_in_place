import tkinter
import colorsys
import math

# Make the window large so that we can see more detail.
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000
BIG_CIRCLE_RADIUS = 450
DATA_FILE = 'small.txt'
DOT_SIZE = 4


def main():
    # get a drawing canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'XKCD Colors')

    dataset = load_data()


def load_data():
    # recall each line looks like "lemon,252,251,181\n"
    data = {}
    return data

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def plot_rgb(canvas, r, g, b):
    hsv = colorsys.rgb_to_hsv(r / 256, g / 256, b / 256)

    radius = BIG_CIRCLE_RADIUS * hsv[1]

    theta = hsv[0] * math.pi * 2.0

    x = CANVAS_WIDTH / 2.0 + radius * math.cos(theta)
    y = CANVAS_HEIGHT / 2.0 - radius * math.sin(theta)

    color_str = colorstr_from_rgb(r, g, b)
    plot_pixel(canvas, x, y, color_str)


def clear_canvas(canvas):
    canvas.delete("all")


def plot_pixel(canvas, x, y, color_str):
    # Create a 1x1 rectangle
    canvas.create_oval(x, y, x+DOT_SIZE, y+DOT_SIZE,
                       fill=color_str, outline=color_str)


def colorstr_from_rgb(red, green, blue):
    assert 0 <= red <= 256
    assert 0 <= green <= 256
    assert 0 <= blue <= 256
    return "#%02x%02x%02x" % (red, green, blue)


def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
