from flip_project.backend.database.sql_database_manager import Database 

PATH = "C:\\Users\\Shachr\\OneDrive - The Academic College of Tel-Aviv Jaffa - MTA\\Documents\\GitHub\\flip_project\\backend\\database\\flip_database.db"


PRODUCTS_ALL = 'products_all'
PRODUCTS_ALL_CONTENT = f"""CREATE TABLE IF NOT EXISTS {PRODUCTS_ALL} (
    prod_id INTEGER PRIMARY KEY,
    prod_name TEXT,
    prod_group TEXT,
    prod_title TEXT,
    prod_available BOOLEAN
    )
"""


USERS = 'users'
USERS_CONTENT = f"""CREATE TABLE IF NOT EXISTS {USERS} (
    user_id INTEGER PRIMARY KEY,
    user_name TEXT,
    user_email TEXT,
    user_phone TEXT,
    user_role TEXT
    )
"""


ACTIONS = 'actions'
ACTIONS_CONTENT = f"""CREATE TABLE IF NOT EXISTS {ACTIONS} (
    id INTEGER PRIMARY KEY,
    prod_id INTEGER,
    user_id INTEGER,
    action_date DATE,
    action_type TEXT
    )
"""


PRODUCTS_TAKEN = 'products_taken'
PRODUCTS_TAKEN_CONTENT = f"""CREATE TABLE IF NOT EXISTS {PRODUCTS_TAKEN} (
    id INTEGER PRIMARY KEY,
    prod_id INTEGER,
    user_id INTEGER,
    take_date DATE,
    expected_return DATE
    )
"""


class AppDB(Database):
    def __init__(self, path):
        super().__init__(path)


if __name__== '__main__':
    db = AppDB(PATH)
    table_contents = [PRODUCTS_ALL_CONTENT, PRODUCTS_TAKEN_CONTENT, ACTIONS_CONTENT, USERS_CONTENT]
    table_names = [PRODUCTS_ALL, PRODUCTS_TAKEN, ACTIONS, USERS]
    #for content in tables_content:
    #    db.create_table(content)

    for name in table_names:
        db.test_print(name)

    print(db)
