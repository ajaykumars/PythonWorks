# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 200

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

    def get_value_range(self):
        return self.value > 200

# your code goes here
car1 = Vehicle()
car2 = Vehicle()
car1.name = "BMW"
car1.color = "Black"
car1.value = 500

car2.name = "Mercedes"
car2.color = "Sliver"
car2.value = 1000

# test code
print(car1.description())
print(car2.description())
print(car2.get_value_range())