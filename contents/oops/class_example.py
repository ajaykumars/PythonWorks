class Duck:
    def __init__(self, _name="", type=""):
        print("Duck object initialized")

    def description(self):
        return 'Duck Description'

    def walk(self):
        print("Walks like a duck")

    def quack(self):
        print("Quacks like a duck")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


test_duck = Duck()
test_duck.quack()
test_duck.walk()
test_duck.set_name("Test Duck")
print(test_duck.get_name())


class Dog:

    def __init__(self, _breed="", _color=None, _breed_code=None):
        self.breed = _breed;
        self.color = _color;
        self.breed_code = _breed_code
        print('Dog object initialized')

    def get_breed(self):
        return self.breed



dog1 = Dog('Golden Retriever', 'Golden', 321)
print(dog1.get_breed())

dog2 = Dog('Boxer')
print(dog2.color)



