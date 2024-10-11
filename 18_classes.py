class Vehicle:
    def __init__(self, make, model):  # constructor
        self.make = make  # attributes
        self.model = model

    def moves(self):
        print("moves")

    def get_make_and_model(self):
        return self.make, self.model


my_car = Vehicle("Toyota", "Camry")
my_car.moves()

print(my_car.get_make_and_model())


your_car = Vehicle("Honda", "Civic")
your_car.moves()
print(your_car.get_make_and_model())


class Airplane(Vehicle):

    def __init__(self, make, model, wingspan):  # constructor
        super().__init__(
            make, model
        )  # call the constructor of the parent class so we dont repeat initiation of attributes
        self.wingspan = wingspan  # new attribute

    def moves(self):  # overriding
        print("fly")


class Truck(Vehicle):
    def moves(self):  # overriding
        print("vroom")


class GolfCart(Vehicle):
    pass  # empty class


airplane = Airplane("Boeing", "747", 15)
airplane.moves()

my_truck = Truck("Ford", "Mustang")
my_truck.moves()


golfCart = GolfCart("Nissan", "Cessna")
golfCart.moves()

# classes: 

# inheritance: you can override the methods of the parent class. and also add new methods and attributes to the child class
# polymorphism : is the ability to behave differently depending on the input messages , as you see in the for loop below, all the classes has the same method , but these methods behave differently depending on the class

for vehicle in [airplane, my_truck, golfCart]:
    vehicle.moves()
    vehicle.get_make_and_model()
