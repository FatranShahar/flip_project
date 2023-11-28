from flask_sqlalchemy import SQLAlchemy
from flip_project.backend.app.app import Server
import json

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flipdata.db'
#db = SQLAlchemy(app)
#CORS(app, resources={r"/*": {"origins": "*"}})

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flipdata.db'
    db = SQLAlchemy(app)
    return db

server = Server()
app = server.get_app()
db = init_db(app=app)

class Flip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flips_count = db.Column(db.Integer, default=0)
    current_state = db.Column(db.Integer, default=-1)


# Route to get the current flip data from the database
@app.route('/get-current-data', methods=['GET'])
def get_current_data():
    flip_data = Flip.query.first()
    if not flip_data:
        # If there's no data in the database, create a new entry
        flip_data = Flip()
        db.session.add(flip_data)
        db.session.commit()

    return json.dumps({"flips_count": flip_data.flips_count,
                        "current_state": flip_data.current_state})

# Route to update flip count and status in the database
@app.route('/update-data', methods=['GET'])
def update_data():
    flip_data = Flip.query.first()
    if not flip_data:
        return json.dumps({"message": "No data found in the database"})

    flip_data.flips_count += 1
    flip_data.current_state *= -1
    db.session.commit()

    return json.dumps({"status": flip_data.current_state})

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True, port=5000)
    
