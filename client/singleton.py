def csingleton(cls):
    instance = {}
    def getInstance():
        print ("cls = ", cls)
        if cls not in instance :
            instance[cls] = cls()
        return instance[cls]
    return getInstance
