from database_manager import DatabaseManagement
from database_selector import Selector

class Database(DatabaseManagement, Selector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
# instant = Database(user="root", password="2362539", database="universcity")
# instant.select_all