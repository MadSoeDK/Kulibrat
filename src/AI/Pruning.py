import copy
import math

from src.Controller.MoveController import possibleMoves
from src.Model.BoardState import BoardState, Action


def pruning_start(state: BoardState, desired_player_index: int) -> Action:
    """ min/max algorithm for finding the best move from the current position

        initial call in the state tree. The tree is explored using a DFS using recursive call.
        This is seperated from the other pruning method, as we need the initial state to return an action and
        not just how great a position the AI have.

        desired_player_index is to allow for multiple player to run as bots. This could be used to improve on the values
        used to calculate the Heuristic value.

        Args:
            state: The boardState of which we want the best move for
            desired_player_index: The index of the player that we want to find the best move for, from the players list in the given state

        :return the action from the given BoardState that gives the best possible outcome, given that both player, playes ideal by the Heuristic values.
        return None if, and only if there is not possible move in the current state.
    """
    # List of possible moves in the current state
    moves = possibleMoves(state)
    best_action = None
    best_value = float('-inf')
    # for each possible note, we DFS search these as child notes to our root
    for move in moves:
        value = pruning(result(state, move), 1, desired_player_index)
        # Figures what DFS tree had the best value
        if value > best_value:
            best_action = move
            best_value = value

    # if no best_action exist
    if best_value is None:
        raise Exception("Invalid game stated passed")
    return best_action


def pruning(state: BoardState, dept, desired_player_index: int) -> float:
    """ min/max algorithm for finding the best move from the current position

        By using pre-defined values, it computes the Heuristic value by
        adding together the position value of red pieces, with the value for each scored point
        and substracting the same, but calculated for blacks pieces

        Args:
            state: The boardState of which we want the best move for
            dept: How deep in the tree we are, assuming the root is dept 0
            desired_player_index: The index of the player that we want to find the best move for, from the players list in the given state

        :return the Heuristic value that the given board state would lead to if both players play ideal
    """

    # Max dept to check
    if dept == 7:
        return eval_state(state)

    # Game Done
    if state.players[0].points == 5:
        return float('-inf')
    elif state.players[1].points == 5:
        return float('inf')

    # generates the list of possible moves for the current state
    moves = possibleMoves(state)

    # Needed for the min max method. Min is for opponents turn, max is for ours
    calc = float('-inf') if state.players.index(state.currentPlayer) == desired_player_index else float('inf')

    # The player have no legal moves
    if not moves:
        # Make a new BoardState object as a copy of the old and updates the current player
        new_state = copy.deepcopy(state)
        new_state.currentPlayer = new_state.players[0] if new_state.currentPlayer is new_state.players[1] else \
        new_state.players[1]

        # Stalemate happens
        if not possibleMoves(new_state):
            # since the player that cause the stalemate lose, we check if the stalemate is good or bad
            return float('inf') if new_state.currentPlayer is new_state.players[0] else float('-inf')

        # recursively call with the new state
        pruning(new_state, dept, desired_player_index)

    # Recursively call this methods, for each possible gamestate that is reachable from here.
    for move in moves:
        # The bot always want make the best move, and therefor picks the move with the highest Heuristic value
        if state.players.index(state.currentPlayer) == desired_player_index:
            calc = max(calc, pruning(result(state, move), dept + 1, desired_player_index))
        # On the players turns, we expect them to make the best possible move, and therefor we go with the lowest heuristic value
        else:
            calc = min(calc, pruning(result(state, move), dept + 1, desired_player_index))
    return calc


# Values used for calculating the Heuristic value
score_row = (1, 2, 3, 4)
goal_point = 6


def eval_state(state: BoardState) -> float:
    """ Computes the Heuristic value of a given BoardState

    By using pre-defined values, it computes the Heuristic value by
    adding together the position value of red pieces, with the value for each scored point
    and substracting the same, but calculated for blacks pieces

    :param state: The boardState that should be evaluated
    """
    score = state.players[1].points * goal_point - state.players[0].points * goal_point
    for i in range(12):
        if state.board.squares[i].owner is state.players[0]:
            score -= score_row[math.floor((11 - i) / 3)]
        if state.board.squares[i].owner is state.players[1]:
            score += score_row[math.floor(i / 3)]
    return score


def result(state: BoardState, action: Action) -> BoardState:
    """ finds the next board state after an action is done

    Takes the board state and updates the position by the given action
    and change the current player to the next player.

    This method assumes that the action passed is legal, and does not throw
    an exception if the move is illegal.
    The Action passed, should be generated by the possibleMoves method by passing it the state as an argument.
    It is not done here, as this list has most likely already been generated for other uses by the method calling this,
    so it is to reduce the amount of redundant method calls.

    Args:
        state: current boardstate
        action: action that would be taken

    :return BoardState: The new generated board state
    """
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

    if toSquareIndex in (12, 13):
        oldPlayer.points += 1

    newState.board.squares[12].owner = None
    newState.board.squares[13].owner = None

    return newState
