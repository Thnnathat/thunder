import mysql.connector 

class Database:
    def conn(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="thunder",
            password="",
            database="test"
        )
        return mydb
    
    def select_all(self):
        mydb = self.conn()
        cs = mydb.cursor(dictionary=True)
        cs.execute(f"SELECT * FROM person")
        data = cs.fetchall()
        cs.close()
        mydb.close()
        return data

    def select_where(self, ID):
        mydb = self.conn()
        cs = mydb.cursor(dictionary=True)
        cs.execute(f"SELECT * FROM person WHERE id = {ID}")
        data = cs.fetchall()
        cs.close()
        mydb.close()
        return data 

    def insert(self, student_id, name, fname, lname):
        mydb = self.conn()
        cs = mydb.cursor()
        cs.execute(f"INSERT INTO person (student_id, name, first_name, last_name)VALUE ('{student_id}', '{name}', '{fname}', '{lname}')")
        mydb.commit()
        cs.close()
        mydb.close()

    def update(self, student_id, name, fname, lname, ID):
        mydb = self.conn()
        cs = mydb.cursor()
        person = (student_id, name, fname, lname)
        cs.execute(f"UPDATE person SET student_id = '%s', name = '%s', first_name = '%s', last_name = '%s'  WHERE id = {ID}" %person)
        mydb.commit()
        cs.close()
        mydb.close()
        
    def remove(self, where):
        mydb = self.conn()
        cs = mydb.cursor()
        cs.execute(f"DELETE FROM person WHERE id = {where}")
        mydb.commit()
        cs.close()
        mydb.close()


database = Database()
activity = database.select_all()
print(activity)