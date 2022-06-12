from database_keang.call import Database


class Activity(Database):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def register(self, user, table_name):
        username = user.username
        fname = user.first_name
        lname = user.last_name
        password = user.password
        null = 0
        return self.insert(null, username, fname, lname, password, table_name=table_name)
