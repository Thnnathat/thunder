import mysql.connector

class Connector:
    def __init__(self, **kwargs):
        self.user = kwargs["user"]
        self.password = kwargs["password"]
        self.database = kwargs["database"]
        self.dictionary = kwargs["dictionary"]
        
        
    @property
    def conn(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user=self.user,
                password=self.password
            )
        except:
            print("Error at connector")
        return mydb
    