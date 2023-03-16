import copy
import math

from src.Controller.MoveController import possibleMoves
from src.Model.BoardState import BoardState, Action


def pruning_start(state: BoardState, desired_player_index: int) -> Action:
    moves = possibleMoves(state)
    best_action: Action
    best_value = float('-inf')
    for move in moves:
        value = pruning(result(state, move), 1, desired_player_index, eval_state(state))
        if value > best_value:
            best_action = move
            best_value = value
    return best_action


def pruning(state: BoardState, dept, desired_player_index: int, initial_state_value: float) -> float:
    # Max dept to check
    if dept == 7:
        return eval_state(state)

    #Game Done
    if state.players[0].points == 5:
        return float('-inf')
    elif state.players[1].points == 5:
        return float('inf')


    moves = possibleMoves(state)
    calc = float('-inf') if state.players.index(state.currentPlayer) == desired_player_index else float('inf')

    # The player have no legal moves
    if not moves:
        new_state = copy.deepcopy(state)
        new_state.currentPlayer = new_state.players[0] if new_state.currentPlayer is new_state.players[1] else new_state.players[1]
        if not possibleMoves(new_state):
            return float('inf') if new_state.currentPlayer is new_state.players[0] else float('-inf')

        pruning(new_state, dept, desired_player_index, initial_state_value)

    for move in moves:
        if state.players.index(state.currentPlayer) == desired_player_index:
            calc = max(calc, pruning(result(state, move), dept + 1, desired_player_index, initial_state_value))
        else:
            calc = min(calc, pruning(result(state, move), dept + 1, desired_player_index, initial_state_value))
    return calc


score_row = (1, 2, 3, 4)
goal_point = 6


def eval_state(state: BoardState) -> float:
    score = state.players[1].points * goal_point - state.players[0].points * goal_point
    for i in range(12):
        if state.board.squares[i].owner is state.players[0]:
            score -= score_row[math.floor((11 - i) / 3)]
        if state.board.squares[i].owner is state.players[1]:
            score += score_row[math.floor(i / 3)]
    return score


def result(state: BoardState, action: Action) -> BoardState:
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

