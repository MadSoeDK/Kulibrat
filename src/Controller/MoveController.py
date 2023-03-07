from src.Model.BoardState import BoardState


def possibleMoves(state: BoardState) -> list[int, (int, int) in range[16]]:
    moves = 0
    pieceOnBoard = 0
    listOfMoves = list((int, int) for i in range(16))

    # Search through board for pieces
    for i in range(12):
        if state.board.squares[i].owner is state.currentPlayer:
            pieceOnBoard += 1

            # blacks turn
            if state.currentPlayer is state.players[0]:
                # attack move
                if state.board.squares[i - 3].owner is not state.currentPlayer:
                    listOfMoves.insert(moves, (i, i - 3))
                    moves += 1
                    # Skip move
                    jumpTo = i
                    while True:
                        jumpTo -= 3
                        if jumpTo < 0:
                            listOfMoves.insert(moves, (i, 13))
                            moves += 1
                            break
                        if state.board.squares[jumpTo].owner is state.currentPlayer:
                            break
                        if state.board.squares[jumpTo].owner is None:
                            listOfMoves.insert(moves, (i, jumpTo))
                            moves += 1
                            break

                # Forward Right and Left move
                if (i % 3 == 1 or i % 3 == 0) and state.board.squares[i - 2].owner is None:
                    listOfMoves.insert(moves, (i, i - 2))
                    moves += 1
                if (i % 3 == 1 or i % 3 == 2) and state.board.squares[i - 4].owner is None:
                    listOfMoves.insert(moves, (i, i - 4))
                    moves += 1

            # Reds turn
            else:
                # attack move
                if state.board.squares[i + 3].owner is not state.currentPlayer:
                    listOfMoves.insert(moves, (i, i + 3))
                    moves += 1
                    # Skip move
                    jumpTo = i
                    while True:
                        jumpTo += 3
                        if jumpTo > 11:
                            listOfMoves.insert(moves, (i, 14))
                            moves += 1
                            break
                        if state.board.squares[jumpTo].owner is state.currentPlayer:
                            break
                        if state.board.squares[jumpTo].owner is None:
                            listOfMoves.insert(moves, (i, jumpTo))
                            moves += 1
                            break

                # Forward Right and Left move
                if (i % 3 == 1 or i % 3 == 0) and state.board.squares[i + 2].owner is None:
                    listOfMoves.insert(moves, (i, i + 2))
                    moves += 1
                if (i % 3 == 1 or i % 3 == 2) and state.board.squares[i + 4].owner is None:
                    listOfMoves.insert(moves, (i, i + 4))
                    moves += 1


    # spawn option
    if pieceOnBoard < 4:
        if state.currentPlayer is state.players[0]:
            for i in range(3):
                if state.board.squares[i + 9].owner is None:
                    listOfMoves.insert(moves, (13, i + 9))
                    moves += 1
        else:
            for i in range(3):
                if state.board.squares[i].owner is None:
                    listOfMoves.insert(moves, (13, i))
                    moves += 1

    finalList = [moves]
    for i in range(16):
        finalList.append(listOfMoves.pop())
    return finalList
