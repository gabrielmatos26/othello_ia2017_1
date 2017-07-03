from models.board import Board

class MinimaxPlayer:
    def __init__(self, color):
        self.color = color
        #bigger weights to corners and edges
        self.boardWeights = [
                                0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
                                0, 150, -10,  10,   3,   3,  10, -10, 150,   0,
                                0, -10, -20,  -3,  -3,  -3,  -3, -20, -10,   0,
                                0,  10,  -3,   8,   1,   1,   8,  -3,  10,   0,
                                0,   3,  -3,   1,   1,   1,   1,  -3,   3,   0,
                                0,   3,  -3,   1,   1,   1,   1,  -3,   3,   0,
                                0,  10,  -3,   8,   1,   1,   8,  -3,  10,   0,
                                0, -10, -20,  -3,  -3,  -3,  -3, -20, -10,   0,
                                0, 150, -10,  10,   3,   3,  10, -10, 150,   0,
                                0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
                            ]

    def eval_board(self, board, color):
        point = 0
        #get opponent's color
        opp = board._opponent(color)
        point = 0
        for row in range(8):
            for col in range(8):
                #add weighted square points to current player
                if board.get_square_color(row,col) is color:
                    point += self.boardWeights[(row+1)*10+1+col]
                #subtract weighted opponent square points from current player
                elif board.get_square_color(row,col) is opp:
                    point -= self.boardWeights[(row+1)*10+1+col]
        return point

    def minimax(self, board, color, depth):
        #Find the best move in the game tree
        #if depth = 0, we have reached maximum depth of tree then we calculate the score
        if depth == 0:
            return self.eval_board(board, color)

        best_val = None
        best_move = None
        #get opponent's color
        opp = board._opponent(color)
        # valid moves
        moves = board.valid_moves(color)

        #try each move in valid moves
        #evaluate max's moves and choose the best value
        if color is board.BLACK:
            for move in moves:
                newBoard = board.get_clone()
                newBoard.play(move, color)
                val = self.minimax(newBoard, opp, depth-1)
                if best_val is None or val > best_val:
                    best_val, best_move = val, move
        #evaluate min's moves and choose the best value
        if color is board.WHITE:
            for move in moves:
                newBoard = board.get_clone()
                newBoard.play(move, color)
                val = self.minimax(newBoard, opp, depth-1)
                if best_val is None or val < best_val:
                    best_val, best_move = val, move
        return best_val, best_move

    def play(self, board):
        depth = 3
        _, move = self.minimax(board, self.color, depth)
        return move
