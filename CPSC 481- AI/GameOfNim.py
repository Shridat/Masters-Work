
from games import *

class GameOfNim(Game):
    def __init__(self, board):
        moves = [(r, n) for r in range(len(board)) for n in range(1, board[r] + 1)]
        self.initial = GameState(to_move="MAX", utility=0, board=board, moves=moves)
        
    def actions(self, state):
        return [(r, n) for r in range(len(state.board)) for n in range(1, state.board[r] + 1)]
    
    def result(self, state, move):
        board = state.board.copy()
        r, n = move
        board[r] -= n
        moves = [(r, n) for r in range(len(board)) for n in range(1, board[r] + 1)]
        next_move = "MIN" if state.to_move == "MAX" else "MAX"
        
        util = 0
        if not moves:
            util = 1 if state.to_move == "MAX" else -1
        
        return GameState(to_move=next_move, utility=util, board=board, moves=moves)
    
    def terminal_test(self, state):
        return not state.moves
    
    def to_move(self, state):
        return state.to_move
    
    def utility(self, state, player):
        return state.utility if player == "MAX" else -state.utility