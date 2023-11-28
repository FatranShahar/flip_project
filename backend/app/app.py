from flask import Flask, jsonify
from flask_cors import CORS

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, resources={r"/*": {"origins": "*"}})

    def get_app(self):
        return self.app
