from src.Model.BoardState import BoardState, Action


def possibleMoves(state: BoardState):
    moves = 0
    pieceOnBoard = 0
    listOfMoves = list()

    # Search through board for pieces
    for i in range(12):
        if state.board.squares[i].owner is state.currentPlayer:
            pieceOnBoard += 1

            # blacks turn
            if state.currentPlayer is state.players[0]:
                # attack move
                if state.board.squares[i - 3].owner is not state.currentPlayer and state.board.squares[i - 3].owner is not None:
                    listOfMoves.append(Action(state.board.squares[i], state.board.squares[i-3]))
                    moves += 1
                    # Skip move
                    jumpTo = i
                    while True:
                        jumpTo -= 3
                        if jumpTo < 0:
                            listOfMoves.append(Action(state.board.squares[i], state.board.squares[12]))
                            moves += 1
                            break
                        if state.board.squares[jumpTo].owner is state.currentPlayer:
                            break
                        if state.board.squares[jumpTo].owner is None:
                            listOfMoves.append(Action(state.board.squares[i], state.board.squares[jumpTo]))
                            moves += 1
                            break

                if 0 <= i <= 2:
                    listOfMoves.append(Action(state.board.squares[i], state.board.squares[12]))
                else:
                    # Forward Right and Left move
                    if (i % 3 == 1 or i % 3 == 0) and state.board.squares[i - 2].owner is None:
                        listOfMoves.append(Action(state.board.squares[i], state.board.squares[i - 2]))
                        moves += 1
                    if (i % 3 == 1 or i % 3 == 2) and state.board.squares[i - 4].owner is None:
                        listOfMoves.append(Action(state.board.squares[i], state.board.squares[i - 4]))
                        moves += 1

            # Reds turn
            else:
                # Goal Move
                if 9 <= i <= 11:
                    listOfMoves.append(Action(state.board.squares[i], state.board.squares[13]))
                else:
                    # Forward Right and Left move
                    if (i % 3 == 1 or i % 3 == 0) and state.board.squares[i + 4].owner is None:
                        listOfMoves.append(Action(state.board.squares[i], state.board.squares[i + 4]))
                        moves += 1
                    if (i % 3 == 1 or i % 3 == 2) and state.board.squares[i + 2].owner is None:
                        listOfMoves.append(Action(state.board.squares[i], state.board.squares[i + 2]))
                        moves += 1
                    # attack move
                    if state.board.squares[i + 3].owner is not state.currentPlayer and state.board.squares[i + 3].owner is not None:
                        listOfMoves.append(Action(state.board.squares[i], state.board.squares[i + 3]))
                        moves += 1
                        # Skip move
                        jumpTo = i
                        while True:
                            jumpTo += 3
                            if jumpTo > 11:
                                listOfMoves.append(Action(state.board.squares[i], state.board.squares[13]))
                                moves += 1
                                break
                            if state.board.squares[jumpTo].owner is state.currentPlayer:
                                break
                            if state.board.squares[jumpTo].owner is None:
                                listOfMoves.append(Action(state.board.squares[i], state.board.squares[jumpTo]))
                                moves += 1
                                break

    # spawn option
    if pieceOnBoard < 4:
        if state.currentPlayer is state.players[0]:
            for i in range(3):
                if state.board.squares[i + 9].owner is None:
                    listOfMoves.append(Action(state.board.squares[13], state.board.squares[i + 9]))
                    moves += 1
        else:
            for i in range(3):
                if state.board.squares[i].owner is None:
                    listOfMoves.append(Action(state.board.squares[12], state.board.squares[i]))
                    moves += 1
    return listOfMoves

