import chess
import random
import numpy

board = chess.Board()

piece_values = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
central_squares = [chess.E4, chess.D4, chess.E5, chess.D5]

def score_count(board):
    score = 0
    for piece_type in piece_values:
        score += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]

    for square in central_squares:
        if board.piece_at(square) is not None:
            if board.piece_at(square).color == chess.WHITE:
                score += 0.5
            else:
                score -= 0.5

    return score

side = input("Ecolha um lado(w/b): ").strip().lower()
if side == 'w':
    player_is_white = True
elif side == 'b':
    player_is_white = False
else:
    print("Escolha invalida. Jogará como branco.")
    player_is_white = True

while not board.is_checkmate() and not board.is_stalemate():
    print(board)

    if (board.turn == chess.WHITE and player_is_white) or (board.turn == chess.BLACK and not player_is_white):
        print('Faça sua jogada!\n')
        print('jogadas permitidas: \n')
        for i in range(board.legal_moves.count() - 1):
            print(list(board.legal_moves)[i])

        player_move = input()
        board.push_san(player_move)
        
    else:
        board_l4_array = []
        board_l3_array = []
        board_l2_array = []
        board_l1_array = []
        board_array = []

        for i in range(board.legal_moves.count() - 1):
            board_l1 = board.copy()
            for j in range(board_l1.legal_moves.count() - 1):
                board_l2 = board_l1.copy()
                for k in range(board_l2.legal_moves.count() - 1):
                    board_l3 = board_l2.copy()
                    for l in range(board_l3.legal_moves.count() - 1):
                        board_l4 = board_l3.copy()
                        move = str(list(board_l4.legal_moves)[l])
                        board_l4.push_san(move)
                        score = score_count(board_l4)
                        board_l4_array.append(score)
                    board_l3_array.append(numpy.max(board_l4_array))
                board_l2_array.append(numpy.max(board_l3_array))
            board_l1_array.append(numpy.max(board_l2_array))
        board_array.append(numpy.max(board_l1_array))
        board.push_san(str(list(board.legal_moves)[board_array.index(numpy.max(board_array))]))

    print('\n\n')

print('Game Over!')
print(board)
