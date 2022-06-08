from .database_connect import Connector

class Selector(Connector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def select_all(self, table):
        try:
            mydb = self.conn
            cs = mydb.cursor(dictionary=self.dictionary)
            cs.execute(f"SELECT * FROM {self.database}.{table}")
            data = cs.fetchall()
        except:
            print("Error at select all")
        finally:
            cs.close()
            mydb.close()
        return data