def square(x):
    return x * x
for i in range(10):
    print(f"The square of {i} is {square(i)}")

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(2, 8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passengers(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")


print("\n\n\n\n")
#Functions
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper
@announce
def hello():
    print("Hello, world!")

hello()

square = lambda x: x * x
for i in range(2, 5):
    print(f"the square of {i} is {square(i)}")


people = [
    {"name": "Harry", "house": "Gryfindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
def f(person):
    return person["name"]
people.sort(key=f)
print('\n', people)

#we try using lamda function
print("\nUsing lamda function we still get the same response")
f = lambda person: person["name"]
people.sort(key=f)
print(people)

#diving numbers by zero
import sys
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
    except ValueError:
        print("Error: Invalid input")
        sys.exit(1)

    try: result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by 0.")
        sys.exit(1)
    print(f"{x} / {y} = {result}", "\nEnter another pair numbers")
