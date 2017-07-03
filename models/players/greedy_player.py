class GreedyPlayer:
    def __init__(self, color):
        self.color = color

    def maximize_current_score(self, board):
        #Find the move that scores best
        best_val = None
        best_move = None

        # valid moves
        moves = board.valid_moves(self.color)

        #try each move in valid moves
        if self.color is board.BLACK:
            for move in moves:
                newBoard = board.get_clone()
                newBoard.play(move, self.color)
                score = newBoard.score()
                if best_val is None or score[1] > best_val:
                    best_val, best_move = score[1], move
        elif self.color is board.WHITE:
            for move in moves:
                newBoard = board.get_clone()
                newBoard.play(move, self.color)
                score = newBoard.score()
                if best_val is None or score[0] > best_val:
                    best_val, best_move = score[0], move
        return best_move

    def play(self, board):
        move = self.maximize_current_score(board)
        return move
