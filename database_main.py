from database_keang.call_database import Database


class Activity(Database):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def activity_select_all(self, table):
        return self.select_all(table)