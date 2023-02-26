class Square(object):
    selected = False
    owner = 0

    def get_owner(self):
        return self.owner

    def set_owner(self, num):
        self.owner = num

    def get_selected(self):
        return self.selected

    def set_selected(self, state):
        self.selected = state
