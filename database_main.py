from database_keang.call_database import Database

database = Database(user="root", password="2362539", database="sample", dictionary=True)
data = database.select_all("student")

for item in data:
    for di in item:
        print(f"{di}: {item[di]}")

