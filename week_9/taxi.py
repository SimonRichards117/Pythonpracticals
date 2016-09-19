"""
CP1404/CP5632 Practical
Car class
"""
import random

class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """
    price_per_km = 1.2

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, ${:.2f}/km, {}km on current fare".format(super().__str__(), Taxi.price_per_km,
                                                             self.current_fare_distance)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


class UnreliableCar(Car):

    def __init__(self, name='', fuel=0, reliability=0):
        super(UnreliableCar, self).__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        drive_variable = random.randint(0,100)
        if drive_variable <= self.reliability:
            if distance > self.fuel:
                distance_driven = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
                distance_driven = distance
            self.odometer += distance_driven
            return distance_driven


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super(SilverServiceTaxi, self).__init__(name, fuel)
        self.fanciness = fanciness

    def get_fare(self):
        return self.fanciness * self.price_per_km * self.current_fare_distance + self.flagfall

# Actual Work #

# prius_1 = Taxi('prius 1', 100)
# prius_1.drive(40)
# print(prius_1, prius_1.get_fare())
# prius_1.start_fare()
# prius_1.drive(100)
# print(prius_1, prius_1.get_fare())

# crapbox = UnreliableCar("Missan Crapbox", 100, 50)
# crapbox.drive(100)
# print(crapbox)
#
# rich_car = SilverServiceTaxi("Rich Bitch", 100, 2)
# rich_car.drive(10)
# print(rich_car.get_fare())

limo = SilverServiceTaxi("Limo", 100, 2)
prius = Taxi("Prius", 100)
hummer = Taxi("Hummer", 200)

taxis = [limo, prius, hummer]

def taxi_simulator():
    print("Let's Drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>>")
    total_bill = 0.0
    current_taxi = taxis[0]
    while menu_choice != 'q':
        if menu_choice == 'c':
            taxi_choice = choose_taxi()
            current_taxi = taxis[taxi_choice]
        elif menu_choice == 'd':
            drive_cost = drive_taxi(current_taxi)
            total_bill += drive_cost
        else:
            print("Invalid Input")
        print("Bill to date: ${:.2f}".format(total_bill))
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>>")
    print("Bill to date: ${:.2f}".format(total_bill))
    counter = 0
    for taxi in taxis:
        print("{} - {}".format(counter, taxi))
        counter += 1


def choose_taxi():
    counter = 0
    for taxi in taxis:
        print("{} - {}".format(counter, taxi))
        counter += 1
    taxi_choice = int(input("Choose Taxi: "))
    return taxi_choice


def drive_taxi(current_taxi):
        drive_distance = int(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(drive_distance)
        print("That trip cost you: {}".format(current_taxi.get_fare()))
        trip_cost = current_taxi.get_fare()
        return trip_cost

taxi_simulator()