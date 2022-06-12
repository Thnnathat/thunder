from .connect import Connector

class DatabaseManagement(Connector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def create(self, database):
        try:
            mydb = self.conn
            cs = mydb.cursor() 
            cs.execute(f"CREATE DATABASE {database}")
        except:
            print("Create database error.")
        finally:
            cs.close()
            mydb.close()
        
    def drop(self, database):
        try:
            mydb = self.conn
            cs = mydb.cursor()
            cs.execute(f"DROP DATABASE {database}")
        except:
            print("Drop database fail.")
        finally:
            cs.close()
            mydb.close()