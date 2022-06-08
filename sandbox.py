from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


# class User(BaseModel):
#     id: int
#     signup_ts: Optional[datetime] = None
#     friends: List[int] = []


# external_data = {
#     'id': '123',
#     'signup_ts': '2019-06-01 12:22',
#     'friends': [1, 2, '3'],
# }
# user = User(**external_data)
# print(user.id)
# #> 123
# #> datetime.datetime(2019, 6, 1, 12, 22)
# print(user.friends)
# #> [1, 2, 3]
# print(user.dict())

# class Test(BaseModel):
#     di: int = 10

# test = Test()
# print(test.di)

def test(w, h):
    print(type(w), type(h))

test("1","2")