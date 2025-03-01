from typing import Optional
from chess.piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King 

class Board:

    def __init__(self):
        self.board = self.create_board()
        self.black_pieces = self.get_black_pieces()
        self.white_pieces = self.get_white_pieces()

    def create_board(self) -> list[list[Optional[Piece]]]:
        board = [[None] * 8 for _ in range(8)]

        # Place white and black pawns
        for i in range(8):
            board[1][i] = Pawn("black", (1, i))
            board[6][i] = Pawn("white", (6, i))

        # Place black pieces
        board[0][0] = Rook("black", (0, 0))
        board[0][1] = Knight("black", (0, 1))
        board[0][2] = Bishop("black", (0, 2))
        board[0][3] = Queen("black", (0, 3))
        board[0][4] = King("black", (0, 4))
        board[0][5] = Bishop("black", (0, 5))
        board[0][6] = Knight("black", (0, 6))
        board[0][7] = Rook("black", (0, 7))       

        # Place white pieces
        board[7][0] = Rook("white", (7, 0))
        board[7][1] = Knight("white", (7, 1))
        board[7][2] = Bishop("white", (7, 2))
        board[7][3] = Queen("white", (7, 3))
        board[7][4] = King("white", (7, 4))
        board[7][5] = Bishop("white", (7, 5))
        board[7][6] = Knight("white", (7, 6))
        board[7][7] = Rook("white", (7, 7))     

        return board
    
    def get_black_pieces(self) -> list[Piece]:
        black_pieces = []

        for i in range(2):
            for j in range(8):
                black_pieces.append(self.board[i][j])

        return black_pieces


    
    def get_white_pieces(self) -> list[Piece]:
        white_pieces = []

        for i in range(6, 8):
            for j in range(8):
                white_pieces.append(self.board[i][j])
                
        return white_pieces
    

    def remove_piece_from_board(self, piece) -> None:
        if piece.get_color() == "white":
            self.white_pieces.remove(piece)
        else:
            self.black_pieces.remove(piece)

    # In case of promotion (or potentially take back?)
    def add_piece_to_board(self, piece) -> None:
        if piece.get_color() == "white":
            self.white_pieces.append(piece)
        else:
            self.black_pieces.append(piece)

    def get_piece(self, row, col):
        return self.board[row][col]
    
    def move_piece(self, r1, c1, r2, c2):
        piece = self.get_piece(r1, c1)
        potential_capture = self.get_Piece(r2, c2)

        if not piece:
            return False
        
        if (r2, c2) in piece.moves(self.board):
            if potential_capture:
                self.remove_piece_from_board(potential_capture)

            self.board[r2][c2] = piece
            self.board[r1][c1] = None

            return True
        
        # Return false if invalid move
        return False

    def get_game_state(self):
        return {"board" : [[piece.to_dict() if piece else None for piece in row] for row in self.board], 
                "turn"  : self.turn}

        
        

    
    



        
