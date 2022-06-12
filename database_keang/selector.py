from .connect import Connector

class Selector(Connector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def select(self, table_name):
        try:
            global data_set
            mydb = self.conn
            cs = mydb.cursor(dictionary=self.dictionary)
            cs.execute(f"SELECT * FROM {table_name}")
            data_set = cs.fetchall()
        except Exception as err:
            print(err)
            data_set = err
        finally:
            cs.close()
            mydb.close()
        return data_set