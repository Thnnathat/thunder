from .manager import DatabaseManagement
from .selector import Selector
from .field import Field

class Database(DatabaseManagement, Selector, Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
# instant = Database(user="root", password="2362539", database="universcity")
# instant.select_all