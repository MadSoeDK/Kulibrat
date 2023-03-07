from src.Model.BoardState import Node, BoardState


class BoardStateTree(object):

    def __init__(self):
        self.root = Node(BoardState(), None, None)

    def actions(self, node: Node):  # Creates a new state, given previous state and new action
        self.node.boardState.moves
        # For all pieces
        # Check all possible legal moves

    def expandNode(self, node: Node):  # Creates the children of the node

        # Get list of legal moves
        legalMoves = node.boardState.moves

        # For each move, create a child node
        for x in legalMoves:
            node.children.append(Node(node.boardState, x, node))

        # Transform each child node state, based on the move
        for x in node.children:
            self.result(x)

    def result(self):

        # Move

        # Score

        # Spawn

        return False
