from database_connect import Connector

class Selector(Connector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    @property
    def select_all(self):
        try:
            mydb = self.conn
            cs = mydb.cursor(dictionary=self.dictionary)
            cs.execute(f"SELECT * FROM {self.database}.friends")
            data = cs.fetchall()
        except:
            print("Error at select all")
        finally:
            cs.close()
            mydb.close()
        return data