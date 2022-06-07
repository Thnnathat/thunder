import mysql.connector
from database_connect import Connector

class DatabaseManagement(Connector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def drop(self, database):
        try:
            mydb = self.conn
            cs = mydb.cursor()
            cs.execute(f"DROP DATABASE {database}")
        except:
            print("Drop database fail")