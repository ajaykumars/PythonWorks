class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass


cat = Cat()
cat.walk()

Cat().walk()
Dog().walk()