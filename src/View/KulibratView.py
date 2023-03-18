from tkinter import *
import math

from src.Controller.GameController import GameController

gameController = GameController()
window: Tk
canvas: Canvas


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

    draw_grid()

    window.bind('<Button-1>', callback)

    exit_button1 = Button(window,
                          bd=5,
                          text="Close Game",
                          command=exit)
    exit_button1.place(x=900, y=20)

    window.mainloop()


def callback(e):
    # Calculate what square was clicked in the grid.
    calc = int((e.x - 21) / 200) + 1 + int((e.y - 21) / 200) * 3
    if 0 < calc < 13 and 20 <= e.x <= 620 and 20 <= e.y <= 820:
        gameController.click(calc)

    # need to add calc for the spawn/goal buttons
    elif math.sqrt(((e.x - 740) ** 2) + ((e.y - 120) ** 2)) < 100:
        gameController.click(13)
    elif math.sqrt(((e.x - 740) ** 2) + ((e.y - 720) ** 2)) < 100:
        gameController.click(14)

    # calc for Game-over buttons
    if gameController.players[1].points == 5 or gameController.players[0].points == 5:
        if math.sqrt(((e.x - 725) ** 2) + ((e.y - 550) ** 2)) < 65:
            gameController.restart()
        elif math.sqrt(((e.x - 905) ** 2) + ((e.y - 550) ** 2)) < 65:
            exit()

    # Clear the old canvas to prepare drawing a new screen
    global canvas
    canvas.delete('all')

    # Draw the new screen
    draw_grid()

    # Set the AI to play
    while gameController.currentPlayer is gameController.players[1]:
        gameController.AI_turn()
        draw_grid()


def draw_grid():
    global canvas
    global gameController
    width = 640
    height = 840

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
    canvas.create_oval(640, 20, 840, 220, width=draw_width)

    # Switch button text depending on currentplayer
    if gameController.currentPlayer is gameController.players[0]:
        canvas.create_text(740, 720, font='Pursia 20', text="Spawn")
        canvas.create_text(740, 120, font='Pursia 20', text="Goal")
    else:
        canvas.create_text(740, 720, font='Pursia 20', text="Goal")
        canvas.create_text(740, 120, font='Pursia 20', text="Spawn")

    for i in range(12):
        if gameController.board.squares[i].owner is not None:
            canvas.tag_raise(canvas.create_oval(
                40 + 200 * (i % 3), 40 + 200 * int(i / 3),
                (0 + 200 * ((i % 3) + 1)), (0 + 200 * (int(i / 3) + 1)),
                fill=gameController.board.squares[i].owner.color
            ))

    # highlights the selected square
    if gameController.fromSquare is not None:
        if gameController.board.squares.index(gameController.fromSquare) < 12:
            square_index = gameController.board.squares.index(gameController.fromSquare)
            canvas.tag_lower(canvas.create_rectangle(
                20 + (square_index % 3) * 200, 20 + int(square_index / 3) * 200,
                220 + (square_index % 3) * 200, 220 + int(square_index / 3) * 200,
                fill="yellow"
            ))
        elif gameController.board.squares.index(gameController.fromSquare) == 13:
            canvas.tag_lower(canvas.create_oval(
                640, 620, 840, 820, fill="yellow"
            ))
        else:
            canvas.tag_lower(canvas.create_oval(
                640, 20, 840, 220, fill="yellow"
            ))

    # Game-over Text and buttons
    if gameController.players[1].points == 5 or gameController.players[0].points == 5:

        if gameController.players[1].points == 5:
            canvas.create_text(815, 480, font='Pursia 25', text=gameController.players[1].color + " Player has WON")

        if gameController.players[0].points == 5:
            canvas.create_text(815, 480, font='Pursia 25', text=gameController.players[1].color + " Player has WON")

        canvas.create_oval(650, 520, 800, 580, width=draw_width)
        canvas.create_text(725, 550, font='Pursia 20', text="Restart")

        canvas.create_oval(830, 520, 980, 580, width=draw_width)
        canvas.create_text(905, 550, font='Pursia 20', text="Exit Game")

        return None

    # Current-player and points text
    canvas.create_text(800, 260, font='Pursia 20', text="current player: " + gameController.currentPlayer.color)
    canvas.create_text(800, 320, font='Pursia 30', text="Red point: " + str(gameController.players[1].points))
    canvas.create_text(800, 370, font='Pursia 30', text="Black point: " + str(gameController.players[0].points))

    canvas.pack()
    canvas.update()
