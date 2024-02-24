from flip_project.backend.database.sql_database_manager import Database 

TABLE_NAME = 'flip_data'

TABLE_CONTENT = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    id INTEGER PRIMARY KEY,
    current_state INTEGER,
    flip_count INTEGER
    )
"""


class FlipDB(Database):
    def __init__(self, path: str):
        super().__init__(path)
        self.create_table(TABLE_CONTENT)
        self.init_table()

    
    def init_table(self):
        if self.is_table_empty(TABLE_NAME):
            data_dict = {'id': 1, 'current_state': -1, 'flip_count': 0}
            self.insert_data(TABLE_NAME, data_dict)


    def get_flip_count(self):
        return self.get_data(TABLE_NAME, 'flip_count')
        
    
    def get_current_state(self):
        return self.get_data(TABLE_NAME, 'current_state')
    
        
    def set_flip_count(self, num: int):
        self.update_record_by_id(TABLE_NAME, 1, 'flip_count', num)


    def set_current_state(self, num: int):
        #TODO: change to eNum
        if num == -1 or num == 1:
            self.update_record_by_id(TABLE_NAME, 1, 'current_state', num)
