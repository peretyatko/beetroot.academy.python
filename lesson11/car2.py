class Car():
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.total_driven_km = 0

    def repaint(self, color):
        self.color = color

    def drive(self, km_driven):
        self.total_driven_km += km_driven

    def __repr__(self):
        return (self.brand + ',' + self.model + ' ' + str(self.year) + ' ' + self.color)

    def __str__(self):
        return self.brand +  ' ' + self.model + ' ' + str(self.year)

class Truck(Car):
    def __init__(self, brand, model, year, color, trailers):
        super().__init__(brand, model, year, color)
        self.trailers = trailers
    def attach_trailer(self, num_of_trailers=1):
        self.trailers += num_of_trailers

    def detach_trailer(self, num_of_trailes=1):
        self.trailers -= num_of_trailes

my_truck = Truck('MAN', 'TRX', 2012, 'black', 1)
print(repr(my_truck))
print(str(my_truck))