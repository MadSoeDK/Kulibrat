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
    if 20 < e.x < 220 and 20 < e.y < 200:
        print("Grid index: 1")
    elif 220 < e.x < 420 and 20 < e.y < 200:
        print("Grid index: 2")
    elif 420 < e.x < 620 and 20 < e.y < 200:
        print("Grid index: 3")
    elif 20 < e.x < 220 and 200 < e.y < 400:
        print("Grid index: 4")
    elif 220 < e.x < 420 and 200 < e.y < 400:
        print("Grid index: 5")
    elif 420 < e.x < 620 and 200 < e.y < 400:
        print("Grid index: 6")
    elif 20 < e.x < 220 and 400 < e.y < 600:
        print("Grid index: 7")
    elif 220 < e.x < 420 and 400 < e.y < 600:
        print("Grid index: 8")
    elif 420 < e.x < 620 and 400 < e.y < 600:
        print("Grid index: 9")
    elif 20 < e.x < 220 and 600 < e.y < 800:
        print("Grid index: 10")
    elif 220 < e.x < 420 and 600 < e.y < 800:
        print("Grid index: 11")
    elif 420 < e.x < 620 and 600 < e.y < 800:
        print("Grid index: 12")

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
