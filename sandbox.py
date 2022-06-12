def test(boolean):    
    return {"error": False} if boolean == True else {'error': True}

data = test(False)
print(data)