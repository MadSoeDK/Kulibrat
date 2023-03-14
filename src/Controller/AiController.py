import copy
from queue import PriorityQueue

from src.Model.BoardState import Action, Node, BoardState
from src.Controller.MoveController import possibleMoves


class Problem(object):
    def __init__(self, init_state: BoardState):
        self.init_state = init_state

        # Create Graph structure
        self.layered_graph = list()

    def is_goal(self, state: BoardState) -> bool:
        if state.currentPlayer.points == 1:
            return True
        return False

    def actions(self, state: BoardState) -> list:
        return possibleMoves(state)

    def result(self, state: BoardState, action: Action) -> BoardState:
        newState = copy.deepcopy(state)

        # Set next current player
        if state.currentPlayer is state.players[0]:
            newState.currentPlayer = newState.players[1]
            oldPlayer = newState.players[0]
        else:
            newState.currentPlayer = newState.players[0]
            oldPlayer = newState.players[1]

        fromSquareIndex = state.board.squares.index(action.fromSquare)
        toSquareIndex = state.board.squares.index(action.toSquare)

        # Execute state squares
        newState.board.squares[fromSquareIndex].owner = None
        newState.board.squares[toSquareIndex].owner = oldPlayer

        return newState

    def action_cost(self, num_of_actions: int) -> int:
        return 1


def mini_max():
    self.layered_graph

def expand(problem: Problem, node: Node):
    state = node.state
    actions = problem.actions(state)
    for action in actions:
        new_state = problem.result(state, action)
        cost = node.path_cost + problem.action_cost(len(actions))
        yield Node(state=new_state, parent=node, action=action, path_cost=cost)

def best_first_search(problem: Problem):
    maxNodesSearched = 6
    node = Node(problem.init_state, path_cost=0)
    problem.layered_graph.append(list())
    frontier = PriorityQueue()
    frontier.queue.append(node)
    for x in range(maxNodesSearched):
        node = frontier.queue.pop()
        problem.layered_graph[len(problem.layered_graph) - 1].append(node)
        for child in expand(problem, node):
            problem.layered_graph[len(problem.layered_graph) - 1].append(child)
            frontier.queue.append(child)

        problem.layered_graph.append(list())
