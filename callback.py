from activity import Activity

class Callback(Activity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def register(self, user, table_name):
        boolean = super().register(user, table_name=table_name)
        return {"error": False} if boolean else {'error': True}