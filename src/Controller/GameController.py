from src.Model.BoardModel import BoardModel


class GameController(object):

    def __init__(self):
        self.board = BoardModel()

    def get_owner(self, num):
        return self.board.get_square(num).get_owner()




