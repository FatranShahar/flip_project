from flip_project.backend.database.db_json_manager import DBJsonManager
from flip_project.backend.database.db_flip_manager import FlipData
from flask import Flask
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

class Engine:
    def __init__(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        db_json_path = os.path.join(curr_dir, "..","database","jsondb.json")
        #db_customer_json_path = os.path.join(curr_dir, "..","database","customerdb.json")
        #db_product_json_path = os.path.join(curr_dir, "..","database","productdb.json")
        #self.cust_db = DBJsonManager(db_customer_json_path)
        #self.prod_db = DBJsonManager(db_product_json_path)
        self.db = FlipData(db_json_path)

engine = Engine()    

@app.route('/register-new-customer', methods=['POST'])
def add_customer(id, first_name, last_name):
    engine.cust_db[id] = first_name + ' ' + last_name
    return None

@app.route('/get-current-data', methods=['GET'])
def get_current_data():
    return json.dumps({"flips_count": engine.db.get_flip_count(),
                    "current_state": engine.db.get_current_state()})
        
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
    #engine = Engine()
    app.run(debug=True, port=5000)
    