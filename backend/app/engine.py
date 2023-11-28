from flask_sqlalchemy import SQLAlchemy
from flip_project.backend.app.app import Server
from flip_project.backend.database.db_json_manager import DBJsonManager
import json
import os


server = Server()
app = server.get_app()
class Engine:
    def __init__(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        db_json_path = os.path.join(curr_dir, "..","database","jsondb.json")
        self.db = DBJsonManager(db_json_path)
        self.db.update_values({"flips_count": 0, "current_state": -1})
        self.current_state = -1 
        self.num_of_clicks = 0

engine = Engine()    
        
@app.route('/get-current-data', methods=['GET'])
def get_current_data():
    return json.dumps({"flips_count": engine.num_of_clicks,
                    "current_state": engine.current_state})
        
@app.route('/update-data', methods=['GET'])
def update_data():
    engine.num_of_clicks += 1
    engine.current_state *= -1
    return json.dumps({"status": engine.current_state})
    
if __name__ == '__main__':
    engine = Engine()
    app.run(debug=True, port=5000)
    