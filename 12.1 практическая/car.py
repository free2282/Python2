class Car(object):

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_car(self):
        print("Автомобиль заведен")

    def stop_car(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color

def main():
    car_1 = Car("red", "hatch", 1950)
    car_1.stop_car()
    car_1.start_car()

    car_2 = Car("black", "uni", 2019)
    print(car_2.color, car_2.type, car_2.year)

    car_2.set_color("white")
    car_2.set_type("hatch")
    car_2.set_year(2022)
    print(car_2.color, car_2.type, car_2.year)

main()