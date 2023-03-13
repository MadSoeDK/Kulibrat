import copy
from queue import PriorityQueue

from src.Model.BoardState import Action, Node, BoardState
from src.Controller.MoveController import possibleMoves


class Problem(object):
    def __init__(self, init_state: BoardState):
        self.init_state = init_state

    def is_goal(self, state: BoardState) -> bool:
        if state.currentPlayer.points == 1:
            return True
        return False

    def actions(self, state: BoardState) -> list:
        moves = possibleMoves(state)
        print(moves)
        return moves

    def result(self, state: BoardState, action: Action) -> BoardState:
        # Copy the old state
        newState = copy.deepcopy(state)

        fromSquareIndex = newState.board.squares.index(action.fromSquare)
        toSquareIndex = newState.board.squares.index(action.toSquare)

        # Rearrange squares
        newState.board.squares[fromSquareIndex].owner = None
        newState.board.squares[toSquareIndex].owner = action.player

        # Define next player
        if action.player is state.players[0]:
            nextPlayer = state.players[1]
        else:
            nextPlayer = state.players[0]

        state.currentPlayer = nextPlayer
        return newState

    def action_cost(self, state: BoardState, action: Action, newState: BoardState) -> int:
        return 1


def expand(problem: Problem, node: Node):
    state = node.state
    for action in problem.actions(state):
        new_state = problem.result(state, action)
        cost = node.path_cost + problem.action_cost(state, action, new_state)
        yield Node(state=new_state, parent=node, action=action, path_cost=cost)


def best_first_search(problem: Problem):
    node = Node(problem.init_state, path_cost=0)
    frontier = PriorityQueue()
    frontier.queue.append(node)
    reached = {problem.init_state: node}
    while not frontier.empty():
        node = frontier.queue.pop()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            state = child.state
            if state not in reached or child.path_cost < reached[state].path_cost:
                reached[state] = child
                frontier.queue.append(child)

    raise Exception

