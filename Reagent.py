class Reagent:
    def __init__(self, name, brand, quantity, location, owner="Public"):
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.location = location
        self.owner = owner
    def __str__(self):
        return '<%s => Name: %s; Brand: %s; Quantity: %s ;Location: %s; Owner: %s>' % (self.__class__.__name__, self.name, self.brand, self.quantity, self.location, self.owner)



if __name__ == '__main __':
    qPCR = Reagent('Sybr Green Master Mix', 'Roche', 8, 'Freezer1 the first layer', 'Xiao')
    print(qPCR)
