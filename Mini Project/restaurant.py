class Res:
    def __init__(self,id,name,price,type,qty):
        self.id = id
        self.name = name
        self.price = price
        self.type = type
        self.quantity = qty

    def __str__(self):
        data = str(self.id)+","+self.name+","+str(self.price)+","+self.type+","+str(self.quantity)
        return data