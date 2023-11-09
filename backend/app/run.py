from flask import Flask

app = Flask(__name__)

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
    return {"status": flip_app.get_current_state()}

if __name__ == '__main__':
    app.run(debug=True)
