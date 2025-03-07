# TODO: Need to figure out castling, need to make sure that I can't castle into check
# TODO: Pinned pieces, could maybe set a flag if king is in line of sight
# TODO: Checks, checkmates
# TODO: Piece promotions
# TODO: En passant - can only capture a pawn en passant immediately after a double-move, then you can't
# TODO: Keep track of moves (not a priority)
# TODO: Keep track of captures (not a priority - do this for points system)

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position # Let's have this be the coordinates
                                 # I'll transfer coordinates to squares when printing moves
        self.symbol = None
    
    def to_dict(self):
        return {"piece" : self.symbol, "color" : self.color}
    
    def is_valid(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def get_color(self):
        return self.color
    
    def is_enemy(self, piece):
        return piece.get_color() != self.color


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'p'
        self.just_made_double_move = False

    def moves(self, board):
        # Need to check for en passant somehow
        row, col = self.position
        legal_moves = set()

        direction = -1 if self.color == "white" else 1

        r, c = direction + row, col

        start_row = 6 if self.color == "white" else 1

        # Check pawn pushes
        if self.is_valid(r, c) and not board[r][c]:
            legal_moves.add((r,c))

            # Check if double move is possible
            r, c = direction + r, c
            if row == start_row and self.is_valid(r, c) and not board[r][c]:
                legal_moves.add((r,c))

        # Check captures (don't worry about en passant just yet)
        captures = [(row + direction, col + 1), (row + direction, col - 1)]
        for cap in captures:
            r, c = cap

            if self.is_valid(r, c) and board[r][c] and self.is_enemy(board[r][c]):
                legal_moves.add((r,c))

        return legal_moves

        
class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'r'
        self.has_moved = False
    
    def moves(self, board) -> set:
        row, col = self.position

        # Want to go up, down, left, and right
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        legal_moves = set()
        
        for dr, dc in directions:
            r, c = row + dr, col + dc

            while self.is_valid(r, c):
                if not board[r][c] or self.is_enemy(board[r,c]):
                    legal_moves.add((r,c))
                else:
                    # Can't jump over piece 
                    break
                    
                r += dr  
                c += dc 

        return legal_moves


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'n'

    def moves(self, board) -> set:
        row, col = self.position

        # Want to go in an L-shape in 8 directions
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        legal_moves = set()
        
        for dr, dc in directions:
            r, c = row + dr, col + dc

            if self.is_valid(r, c):
                if not board[r][c] or self.is_enemy(board[r,c]):
                    legal_moves.add((r,c))

        return legal_moves

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'b'

    def moves(self, board) -> set:
        row, col = self.position

        # Want to go diagonally in 4 directions
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        legal_moves = set()
        
        for dr, dc in directions:
            r, c = row + dr, col + dc

            while self.is_valid(r, c):
                if not board[r][c] or self.is_enemy(board[r,c]):
                    legal_moves.add((r,c))
                else:
                    # Can't jump over piece 
                    break
                    
                r += dr  
                c += dc 

        return legal_moves

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'q'


    def moves(self, board) -> set:
        row, col = self.position

        # Want to go in every direction
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]

        legal_moves = set()
        
        for dr, dc in directions:
            r, c = row + dr, col + dc

            while self.is_valid(r, c):
                if not board[r][c] or self.is_enemy(board[r,c]):
                    legal_moves.add((r,c))
                else:
                    # Can't jump over piece 
                    break
                    
                r += dr  
                c += dc 

        return legal_moves

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'k'
        self.has_moved = False

    def moves(self, board) -> set:
        row, col = self.position

        # Want to go in every direction
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]

        legal_moves = set()
        
        for dr, dc in directions:
            r, c = row + dr, col + dc

            if self.is_valid(r, c):
                if not board[r][c] or self.is_enemy(board[r,c]):
                    legal_moves.add((r,c))
            
        return legal_moves
