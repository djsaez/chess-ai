from chess.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end

        if self.board.move_piece(self, start_row, start_col, end_row, end_col):
            self.turn = "black" if self.turn == "white" else "white"
            return True
        
        return False