from queue import PriorityQueue

from src.Model.BoardState import Action, Node, BoardState
from src.Controller.MoveController import possibleMoves


def main():
    problem = Problem(BoardState())
    possibleMoves()


class Problem(object):
    def __init__(self, init_state: BoardState):
        self.initial = init_state

    def is_goal(self, state: BoardState):
        return True

    def actions(self, state: BoardState) -> list:
        return

    def result(self, state: BoardState, action: Action) -> BoardState:
        return

    def action_cost(self, state: BoardState, action: Action, newState: BoardState) -> int:
        return 1


def expand(problem: Problem, node: Node):
    state = node.state

    for action in problem.actions(state):
        new_state = problem.result(state, action)
        cost = node.path_cost + problem.action_cost(state, action, new_state)
        yield Node(state=new_state, parent=node, action=action, path_cost=cost)


def best_first_search(problem: Problem):
    node = Node(problem.initial)
    frontier = PriorityQueue()
    frontier.queue.append(node)
    reached = {problem.initial: node}
    while not frontier.empty():
        node = frontier.queue.pop()
        if problem.is_goal(node.boardState):
            return node

        for child in expand(problem, node):
            state = child.state
            if state not in reached or child.path_cost < reached[state].path_cost:
                reached[state] = child
                frontier.queue.append(child)

    return Exception

