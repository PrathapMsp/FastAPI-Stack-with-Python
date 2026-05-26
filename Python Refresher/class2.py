class Car:
    def __init__(self, type, color, cc, brand, model):
        self.type = type
        self.color = color
        self.cc = cc
        self.brand = brand
        self.model = model

    def get_overall(self):
        return self.type + " " + self.color + " " + self.brand
