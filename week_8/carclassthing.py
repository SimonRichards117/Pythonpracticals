"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from week_8.car import Car


def main():
    bus = Car(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=bus))
    limo = Car(100)
    limo.add_fuel(20)
    print("Limo's Fuel is: {}".format(limo.fuel))
    limo.drive(115)
    print("Limo's Odometer is: {}".format(limo.odometer))
main()