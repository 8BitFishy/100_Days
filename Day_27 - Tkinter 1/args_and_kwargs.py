def add(*args):
    k = 0
    for n in args:
        k += n

    return k

def calculate(n, **kwargs):
    print(n, end=" ")
    for key, value in kwargs.items():
        print(key, value, end = " ")

    print()
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


print(add(2, 5))
print(add(2, 3, 4, 5, 6, 2, 4, 6, 7, 3, 5, 6, 3, 56, 6, 7, 4, 5, 7, 7))

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.doors = kw.get("doors")


my_car = Car(make="Seat", colour = "Black", doors = 5)

print(f"A {my_car.colour}, {my_car.doors} door {my_car.make} {my_car.model}")