class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # initialize parent
        self.breed = breed      # own attribute

    def speak(self):
        super().speak()         # call parent method
        print(self.name, "barks")
