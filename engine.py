import chess

piece_weights = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
    }

def evaluate_material(board):
    material = 0
    if board.is_game_over():
        return None
    else:
        for p in board.piece_map().values():
            v = piece_weights[p.piece_type]
            if p.color == chess.BLACK:
                v = -v
            material += v
        return material

def evaluate(board):
    evaluation = evaluate_material(board)
    print(evaluation if evaluation is not None else board.result())

if __name__ == "__main__":
    board = chess.Board()
    # Push some moves
    board.push_san("e4")
    board.push_san("e5")
    board.push_san("Bc4")
    board.push_san("a6")
    board.push_san("Qh5")
    board.push_san("Nf6")
    #board.push_san("Qf7")

    print(board)
    
    evaluate(board)
