from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in your Flask app

class FlipApp:
    def __init__(self) -> None:
        self._current_state = -1

    def update_state(self):
        self._current_state *= -1

    def get_current_state(self):
        return self._current_state

flip_app = FlipApp()

@app.route('/update-color', methods=['GET'])
def update_color():
    flip_app.update_state()
    return jsonify({"status": flip_app.get_current_state()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
