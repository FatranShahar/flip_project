from flip_project.backend.database.db_json_manager import DBJsonManager

class FlipData(DBJsonManager):
    def __init__(self, path):
        super().__init__(path)
        current_keys = self.get_keys()
        if "flips_count" not in current_keys:
            self.set_flip_count(0)
        if "current_state" not in current_keys:
            self.set_current_state(-1)

    def get_flip_count(self):
        return self.get_value("flips_count")
    
    def get_current_state(self):
        return self.get_value("current_state")
    
    def set_flip_count(self, num: int):
        self.update_values({"flips_count": num})

    def set_current_state(self, num: int):
        #TODO: change to eNum
        if num == -1 or num == 1:
            self.update_values({"current_state": num})