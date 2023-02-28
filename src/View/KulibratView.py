from tkinter import *

from src.Controller.GameController import GameController


@staticmethod
def launch():
    width = 1000
    height = 900

    gameController = GameController()
    window = Tk()
    window.minsize(width, height)
    window.resizable(False, False)
    canvas = Canvas(window, width= width, height= height)
    canvas.pack()

    draw_grid(canvas, 800, 600)

    window.bind('<Button-1>', callback)

    window.mainloop()


def callback(e):
    width = 1000
    height = 800
    spacing = 20
    if e.x > 20 & e.x < 600 & e.y > 20 & e.y < 820:
        print("within")
    print("x=%d, y=%d", e.x, e.y)


def draw_grid(canvas, height, width):
    # outer line
    spacing = 20
    draw_width = 10
    canvas.create_line(
        spacing, spacing,
        spacing, height - spacing,
         width + spacing, height - spacing,
         width + spacing, spacing,
        spacing, spacing,
        width=draw_width)

    canvas.create_line(
        (width / 3) + spacing, spacing,
        (width / 3) + spacing, height - spacing,
        width=draw_width
    )

    canvas.create_line(
        ((width / 3) * 2) + spacing, spacing,
        ((width / 3) * 2) + spacing, height - spacing,
        width=draw_width
    )

    canvas.create_line(
        spacing, height/4,
        width + spacing, height/4,
        width=draw_width
    )

    canvas.create_line(
        spacing, 3*height/4,
        width + spacing, 3*height/4,
        width=draw_width
    )

    canvas.create_line(
        spacing, 2 * height / 4,
         width + spacing, 2 * height / 4,
        width=draw_width
    )
