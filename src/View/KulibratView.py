from tkinter import *

from src.Controller.GameController import GameController

gameController = GameController()


@staticmethod
def launch():
    width = 1000
    height = 840

    window = Tk()
    window.minsize(width, height)
    window.resizable(False, False)
    canvas = Canvas(window, width=width, height=height)
    canvas.pack()

    draw_grid(canvas, 840, 640)

    window.bind('<Button-1>', callback)

    spawn_button1 = Button(window,
                           bd=5,
                           text="Spawn button 1",
                           command=exit)
    spawn_button1.place(x=640, y=20)

    spawn_button2 = Button(window,
                           bd=5,
                           text="Spawn button 2",
                           command=exit)
    spawn_button2.place(x=640, y=710)

    exit_button1 = Button(window,
                          bd=5,
                          text="Close Game",
                          command=exit)
    exit_button1.place(x=900, y=20)

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

    calc = int((e.x - 21) / 200) + 1 + int((e.y - 21) / 200) * 3
    print(calc)
    if 0 < calc < 13 and 20 <= e.x <= 620 and 20 <= e.y <= 820:
        gameController.click(calc)
        print("within")
    # need to add calc for the spawn/goal buttons

    print("x=%d, y=%d", e.x, e.y)


def draw_grid(canvas, height, width):
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
