from tkinter import *
import math

from src.Controller.GameController import GameController

gameController = GameController()
window: Tk
canvas: Canvas
count = 0


@staticmethod
def launch():
    global window
    global canvas

    width = 1000
    height = 840

    window = Tk()
    window.minsize(width, height)
    window.resizable(False, False)

    canvas = Canvas(window, width= width, height= height)
    canvas.pack()

    draw_grid()

    window.bind('<Button-1>', callback)

    exit_button1 = Button(window,
                          bd=5,
                          text="Close Game",
                          command=exit)
    exit_button1.place(x=900, y=20)

    window.mainloop()


def callback(e):
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
    global canvas
    canvas.delete('all')
    draw_grid()


def draw_grid():
    global count
    global canvas
    global gameController
    width = 640
    height = 840

    count += 1

    canvas.delete('all')
    canvas.pack()
    spacing = 20
    draw_width = 10

    canvas.create_line(
        spacing, spacing,
        spacing, height - spacing,
        width - spacing, height - spacing,
        width - spacing, spacing,
        spacing, spacing,
        width=draw_width
    )

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

    for i in range(12):
        if gameController.board.squares[i].owner is not None:
            canvas.tag_raise(canvas.create_oval(
                40 + 200 * (i % 3), 40 + 200 * int(i / 3),
                (0 +200*((i % 3)+1)), (0+200*(int(i/3)+1)),
                fill=gameController.board.squares[i].owner.color
            ))

    if gameController.fromSquare is not None:
        square_index = gameController.board.squares.index(gameController.fromSquare)
        canvas.tag_lower(canvas.create_rectangle(
            20 + (square_index % 3) * 200, 20 + int(square_index / 3) * 200,
            220 + (square_index % 3) * 200, 220 + int(square_index / 3) * 200,
            fill="yellow"
        ))

    canvas.pack()
    canvas.update()
