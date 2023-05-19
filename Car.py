# Simple test program that is part of the PyCharm
# first steps tutorial

# declare a class and define attributes of the class
class Car:
    # function to initialize an instance of the class
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    # the following functions are used to alter the values of the attributes
    # or display the current attribute values
    def say_state(self):
        print("Moving at {} mph.".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def avg_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


# entry to main
if __name__ == '__main__':
    # declare an instance of the class
    my_car = Car()
    print("CAR")
    while True:
        action = input("Choose action:  [A]ccelerate, [B]rake, "
                       "display [O]dometer, or show the average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("Action not valid.")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("Car has traveled {} miles.".format(my_car.odometer))
        elif action == 'S':
            print("Car average speed was {} mph.".format(my_car.avg_speed))
        my_car.step()
        my_car.say_state()
