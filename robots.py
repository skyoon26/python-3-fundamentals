class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]
        print("My name is", self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("New position:", self.position)

    def eat(self):
        print("I'm hungry!")


# Creating a child class
# The parent class goes in the parentheses
class Robot_Dog(Robot):
    # if we leave out the __init__() method, it will call the parent's __init__() method by default
    def make_noise(self):
        print("Woof Woof!")

    # This is an example of method overriding which allows you to customize a method's implementation in the child class
    # This eat method will be run for all Robot Dog objects instead of the generic Robot's eat method
    def eat(self):
        # Calling super gives us access to the parent class's methods
        super().eat()
        print("I like bacon!")


my_robot_dog = Robot_Dog("Bud")
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()
