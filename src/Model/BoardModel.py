from src.Model.Square import Square


class BoardModel(object):
    squares = [Square for i in range(14)]

    def __init__(self):
        self.squares = [Square() for i in range(14)]
