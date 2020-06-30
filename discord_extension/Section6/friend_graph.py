import tkinter

FRIENDS_FILE = 'users.txt'
COORDINATES_FILE = 'coords.txt'


def main():
    canvas = make_canvas(800, 800)
    draw_friend_graph(canvas, FRIENDS_FILE, COORDINATES_FILE)
    canvas.mainloop()


def draw_friend_graph(canvas, friends_file, coordinates_file):
    pass


# provided function, this code is complete (Nick's Code from lecture for make_canvas)
def make_canvas(width, height):
    """
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)

    canvas = tkinter.Canvas(top, width=width, height=height)
    canvas.pack()
    canvas.xview_scroll(6, "units")  # hack so (0, 0) works correctly
    canvas.yview_scroll(6, "units")

    # draw blue boundaries - sides
    canvas.create_line(0, 0, 0, height-1, width=1, fill='blue')
    canvas.create_line(width-1, 0, width-1, height-1, width=1, fill='blue')
    # top bottom
    canvas.create_line(0, 0, width - 1, 0, width=1, fill='blue')
    canvas.create_line(0, height - 1, width - 1,
                       height - 1, width=1, fill='blue')

    return canvas


if __name__ == "__main__":
    main()
