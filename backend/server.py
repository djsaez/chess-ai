from flask import Flask, jsonify, request
from flask_cors import CORS
from chess.game import Game  # Import your Game class

app = Flask(__name__)
CORS(app)

# Initialize the chess game
game = Game()

@app.route('/')
def home():
    return jsonify({"message": "Chess backend is running!"})

@app.route('/get_board', methods=['GET'])
def get_board():
    """Returns the current board state and turn"""
    return jsonify(game.get_game_state())

@app.route('/move_piece', methods=['POST'])
def move_piece():
    """Attempts to move a piece and updates the game state"""
    data = request.get_json()
    start = tuple(data.get("start"))  # Expecting [row, col]
    end = tuple(data.get("end"))

    success = game.move_piece(start, end)
    if success:
        return jsonify({"success": True, "message": "Move successful", "gameState": game.get_game_state()})
    else:
        return jsonify({"success": False, "message": "Invalid move"})

if __name__ == '__main__':
    app.run(debug=True)