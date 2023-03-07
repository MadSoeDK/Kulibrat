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

            # Reds turn
            if state.currentPlayer is state.players[1]:
                None

    finalList = [moves]
    for i in range(16):
        finalList.append(listOfMoves.pop())
    return finalList
