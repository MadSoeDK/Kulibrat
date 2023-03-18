import copy
from queue import PriorityQueue

from src.AI.min_max_DFS import eval_state, actions
from src.Model.BoardState import Action, Node, BoardState


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
        return actions(state)

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

    def action_cost(self, state: BoardState) -> float:
        return eval_state(state)


def expand(problem: Problem, node: Node):
    state = node.state
    for action in problem.actions(state):
        new_state = problem.result(state, action)
        cost = node.path_cost + problem.action_cost(state)
        yield Node(state=new_state, parent=node, action=action, path_cost=cost)


def best_first_search(problem: Problem):
    maxNodesSearched = 6
    node = Node(problem.init_state, path_cost=0)
    problem.layered_graph.append(list())
    frontier = PriorityQueue()
    frontier.queue.append(node)
    reached = {problem.init_state: node}
    for x in range(maxNodesSearched):
        node = frontier.queue.pop()
        problem.layered_graph[len(problem.layered_graph) - 1].append(node)
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            state = child.state
            problem.layered_graph[len(problem.layered_graph)-1].append(child)
            if state not in reached or child.path_cost < reached[state].path_cost:
                reached[state] = child
                frontier.queue.append(child)

        problem.layered_graph.append(list())