class Robot_Dog:
    # 1. The __init__() method lets us initialize the robot's properties
    # 2. The self keyword is required, it refers to the instance you're creating
    # 3. Also pass the properties you want to initialize as parameters
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # 4. A class method is created just like a function except it has self as the first parameter
    def bark(self):
        print("Woof Woof!")


my_dog = Robot_Dog("Spot", "Chihuahua")
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()
