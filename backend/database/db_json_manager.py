import json
import os

class DBJsonManager():
    def __init__(self, path:str):
        self.json_path = path
        if not os.path.exists(path=path):
            print("in creation of data")
            with open(self.json_path, 'wt') as fh:
                json.dump({}, fh)

    def _get_db_json(self):
        with open(self.json_path, 'rt') as fh:
            db_json = json.load(fh)
        return db_json
    
    def update_values(self, update_dic):
        db_json = self._get_db_json()
        db_json.update(update_dic)
        with open(self.json_path, 'wt') as fh:
            json.dump(db_json, fh)
        
    def get_value(self, key_name):
        db_json = self._get_db_json()
        if key_name in db_json:
            value = db_json[key_name]
        else:
            value = None
        return value
    
    def get_keys(self):
        db_json = self._get_db_json()
        return db_json.keys() 