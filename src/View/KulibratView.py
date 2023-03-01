from tkinter import *
import math

from src.Controller.GameController import GameController

gameController = GameController()
window: Tk
canvas: Canvas


@staticmethod
def launch():
    global window
    global canvas

    width = 1000
    height = 840

    window = Tk()
    window.minsize(width, height)
    window.resizable(False, False)

    canvas = Canvas(window, width=width, height=height)
    canvas.pack()

    draw_grid(840, 640)

    window.bind('<Button-1>', callback)

    exit_button1 = Button(window,
                          bd=5,
                          text="Close Game",
                          command=exit)
    exit_button1.place(x=900, y=20)

    for i in range(12):
        if gameController.board.squares[i].owner is not None:
            canvas.create_rectangle(
                20 + 200 * (i % 3), 20 + 200 * int(i / 3),
                (20+200*((i % 3)+1)), (20+200*(int(i/3)+1)),
                fill=gameController.board.squares[i].owner)

    #if gameController.board.squares[0].owner is not Non
    canvas.pack()
    window.mainloop()


def callback(e):
    """
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
    """

    calc = int((e.x - 21) / 200) + 1 + int((e.y - 21) / 200) * 3
    print(calc)
    if 0 < calc < 13 and 20 <= e.x <= 620 and 20 <= e.y <= 820:
        gameController.click(calc)
        print("within")
    # need to add calc for the spawn/goal buttons
    elif math.sqrt(((e.x - 740) ** 2) + ((e.y - 120) ** 2)) < 100:
        gameController.click(13)
        print("13")
    elif math.sqrt(((e.x - 740) ** 2) + ((e.y - 720) ** 2)) < 100:
        gameController.click(14)
        print("14")

    print("x=%d, y=%d", e.x, e.y)

    if gameController.board.squares[0] is gameController.board.squares[1]:
        print("true")
    #launch()


def draw_grid(height, width):
    global canvas
    spacing = 20
    draw_width = 10

    canvas.create_line(
        spacing, spacing,
        spacing, height - spacing,
                 width - spacing, height - spacing,
                 width - spacing, spacing,
        spacing, spacing,
        width=draw_width)


    for i in range(2):
        canvas.create_line(
            ((width - spacing * 2) / 3) * (i + 1) + spacing, spacing,
            ((width - spacing * 2) / 3) * (i + 1) + spacing, height - spacing,
            width=draw_width
        )
    for i in range(3):
        canvas.create_line(
            spacing, ((height - spacing * 2) / 4) * (i + 1) + spacing,
                     width - spacing, ((height - spacing * 2) / 4) * (i + 1) + spacing,
            width=draw_width
        )

    # Drawing the circles
    canvas.create_oval(640, 620, 840, 820, width=draw_width)
    canvas.create_text(740, 720, font='Pursia 20', text="Spawn")

    canvas.create_oval(640, 20, 840, 220, width=draw_width)
    canvas.create_text(740, 120, font='Pursia 20', text="Goal")

    canvas.pack()
