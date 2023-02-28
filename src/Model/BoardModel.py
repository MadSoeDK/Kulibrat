from src.Model.Square import Square


class BoardModel(object):
    squares = [Square for i in range(12)]

    def get_square(self, index):
        return self.squares[index]
