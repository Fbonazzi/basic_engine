import chess

piece_weights = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
    }

result_weights = {
    "1-0": 1000,
    "0-1": -1000,
    "1/2-1/2": 0
    }

def evaluate_material(board) -> int:
    material = 0

    if board.is_game_over():
        material = result_weights[board.result()]
    else:
        for p in board.piece_map().values():
            v = piece_weights[p.piece_type]
            if p.color == chess.BLACK:
                v = -v
            material += v

    return material

def better_move(side, a, b) -> bool:
    if (side == chess.WHITE and a > b) or (side == chess.BLACK and a < b):
        return True
    else:
        return False

def select_candidate_move(side, evaluations) -> chess.Move:
    candidate, candidate_eval = list(evaluations.items())[0]
    
    for m, v in evaluations.items():
        if better_move(side, v, candidate_eval):
            candidate = m
            candidate_eval = v
        
    return candidate

def internal_evaluate(board, depth=0):
    evaluation = evaluate_material(board)

    if depth == 0 or board.is_game_over():
        return ([], evaluation)
    else:
        move_evaluations = {}
        move_sequences = {}
        for i in board.legal_moves:
            board.push(i)
            move_sequence, move_evaluation = internal_evaluate(board, depth - 1)
            move_evaluations[i] = move_evaluation
            move_sequences[i] = move_sequence
            board.pop()
        move = select_candidate_move(board.turn, move_evaluations)
        return ([move] + move_sequences[move], move_evaluations[move])

def evaluate(board, depth=0):
    sequence, evaluation = internal_evaluate(board, 2 * depth)

    print(board.variation_san(sequence))

    internal_board = board.copy()

    for m in sequence:
        internal_board.push(m)

    print(internal_board.result() if internal_board.is_game_over() else evaluation)

if __name__ == "__main__":
    # Initialise structures
    board = chess.Board()

    # Push some moves
    board.push_san("e4")
    board.push_san("e5")
    board.push_san("Bc4")
    board.push_san("a6")
    board.push_san("Qh5")
    board.push_san("Nf6")
    #board.push_san("Qf7")

    # Initialise board
    # board.set_board_fen("r5rk/5p1p/5R2/4B3/8/8/7P/7K w")

    print(board.board_fen())

    print(chess.Board().variation_san(board.move_stack))
    print()
    print(board)
    print()

    evaluate(board, 1)
