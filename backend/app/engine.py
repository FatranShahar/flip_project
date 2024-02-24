from flip_project.backend.database.flip_db_manager import FlipDB
from flask import Flask
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
PATH = "C:\\Users\\Shachr\\OneDrive - The Academic College of Tel-Aviv Jaffa - MTA\\Documents\\GitHub\\flip_project\\backend\\database\\flip_database.db"


class Engine:
    def __init__(self):
        #curr_dir = os.path.dirname(os.path.realpath(__file__))
        #db_json_path = os.path.join(curr_dir, "..","database","jsondb.json")
        #self.db = FlipData(db_json_path)
        self.db = FlipDB(PATH)


@app.route('/get-current-data', methods=['GET'])
def get_current_data():
    flip_count = engine.db.get_flip_count()
    current_state = engine.db.get_current_state()
    return json.dumps({"flips_count": flip_count,
                    "current_state": current_state})
        

@app.route('/update-data', methods=['GET'])
def update_data():
    flips_count = engine.db.get_flip_count()
    current_state = engine.db.get_current_state()
    flips_count += 1
    current_state *= -1
    output = {"current_state": current_state, "flips_count": flips_count}
    engine.db.set_current_state(current_state)
    engine.db.set_flip_count(flips_count)
    return json.dumps(output)
    

if __name__ == '__main__':
    engine = Engine()
    app.run(debug=True, port=5000)
    