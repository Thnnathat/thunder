from .connect import Connector

class Field(Connector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_key(self, table_name):
        mydb = self.conn
        cs = mydb.cursor(dictionary=True)
        cs.execute(f"SELECT * FROM {table_name}")
        data = cs.fetchall()
        key = {i for i in data[0]}
        key_set = set(key) 
        cs.close()
        mydb.close()
        return key_set

    def show_table(self):
        try:
            mydb = self.conn
            cs = mydb.cursor()
            cs.execute(f"SHOW TABLES FROM {self.database}")
            data = cs.fetchall()
            return data
        except Exception as err:
           return err
        
    def insert(self, *args, table_name):
        global sql
        try:
            mydb = self.conn
            cs = mydb.cursor()
            sql = f"INSERT INTO {table_name} VALUES {args}"
            cs.execute(sql)
            mydb.commit()
            return True
        except Exception as err:
            print(err)
            print("Error at insert")
            return False
        finally:
            cs.close()
            mydb.close()

if __name__ == "__main__":
    pass
