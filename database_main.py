import sys
sys.path.insert(0, "/home/keang/Documents/coding/python/thunder/database") #replace your path directory
from database.call_database import Database

database = Database(user="root", password="2362539", database="", dictionary=True)

# head = "" 
# table_data = []
# for item in data:
#     for di in item:
#         # print(f"{di}: {item[di]}")
#         head.append(di)
#         table_data.append(item[di])

# print(head, "\n", table_data)
