"""

"""


class Vehicle:
    def __init__(self, fuel):
        self.fuel = fuel
        self.trips = []

    def add_distance(self, trip):
        self.trips.append(trip)

    def sum_trips_distance(self):
        return sum(self.trips)

    def calc_remained_distance(self):
        raise NotImplementedError()


class GroundVehicle(Vehicle):
    FUEL_PER_100KM = 12

    def calc_remained_distance(self):
        distance = self.sum_trips_distance()
        spent_fuel = distance / 100 * self.FUEL_PER_100KM
        result = (self.fuel - spent_fuel) / self.FUEL_PER_100KM
        return f"Топливо осталось {result} км"


class AirVehicle(Vehicle):
    FUEL_PER_HOUR = 300

    def calc_remained_distance(self):
        distance = self.sum_trips_distance()
        spent_fuel = distance * self.FUEL_PER_HOUR
        result = (self.fuel - spent_fuel) / self.FUEL_PER_HOUR
        return f"Топливо осталось {result} ч"


car = GroundVehicle(100)
car.add_distance(10)
car.add_distance(30)
print(car.calc_remained_distance())
fly = AirVehicle(1000)
fly.add_distance(2)
fly.add_distance(3)
print(fly.calc_remained_distance())

