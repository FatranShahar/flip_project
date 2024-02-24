import sqlite3
import pandas as pd

class Database():
    def __init__(self, path: str):
        self.path = path
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        self.close_connection()


    # table content should be in the format of:
    # """
    # CREATE TABLE IF NOT EXISTS test (
    # id INTEGER PRIMARY KEY,
    # name TEXT,
    # age INTEGER,
    # height REAL,
    # data BLOB
    # )
    # """
        

    #TODO add try and execpt to open connection    
    def create_table(self, table_content: str):
        self.open_connection()
        self.cursor.execute(table_content)
        self.connection.commit()
        self.close_connection()


    def insert_data(self, table_name: str, dict_obj: dict):
        columns = ', '.join(dict_obj.keys())
        values = ', '.join(['?'] * len(dict_obj))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        # Convert the dictionary values to a tuple
        data_tuple = tuple(dict_obj.values())
        # Execute the query
        self.open_connection()
        self.cursor.execute(query, data_tuple)
        self.connection.commit()
        self.close_connection()


    def test_print(self, name: str):
        self.open_connection()
        query = f"select * from {name}"
        df = pd.read_sql_query(query, self.connection)
        print(df)    
        self.close_connection()

    def delete_record_from_table(self, record_id: int, table_name: str):
        query = f"DELETE FROM {table_name} WHERE id = {record_id}"
        self.open_connection()
        self.cursor.execute(query)
        self.connection.commit()
        self.close_connection()


    def delete_table_by_name(self, table_name: str):
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.open_connection()
        self.cursor.execute(query)
        self.connection.commit()
        self.close_connection()


    def is_table_empty(self, table_name: str) -> bool:
        query = f"SELECT COUNT(*) FROM {table_name}"
        self.open_connection()
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        self.close_connection()
        return count == 0    


    def get_data(self, table_name: str ,column: str):
        query = f"SELECT {column} FROM {table_name} WHERE id = 1"
        self.open_connection()
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.close_connection()
        if result:
            return result[0]  # return the flip_count value
        else:
            return None  # return None if no record with the given id is found


    def update_record_by_id(self, table_name: str, record_id: int, column_name: str, new_value):
        query = f"UPDATE {table_name} SET {column_name} = ? WHERE id = ?"
        self.open_connection()
        self.cursor.execute(query, (new_value, record_id))
        self.connection.commit()
        self.close_connection()


    def close_connection(self):
        self.connection.close()


    def open_connection(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

# if __name__== '__main__':
#     database = Database()
#     # table_content = """
#     # CREATE TABLE IF NOT EXISTS test (
#     # id INTEGER PRIMARY KEY,
#     # current_state INTEGER,
#     # flip_count INTEGER
#     # )
#     # """
#     # database.create_table(table_content)
#     # data_dict = {'id': 1, 'current_state': -1, 'flip_count': 0}
#     # database.insert_data('test', data_dict)
#     # database.delete_record_from_table(1, 'test')
#     database.delete_table_by_name('test')
#     database.test_print()