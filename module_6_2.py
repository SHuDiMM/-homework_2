class Vehicle():
    __COLOR_VARIANTS = ['black', 'magenta', 'orange', 'green', 'white', 'yellow']

    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):
        print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        print(f"Цвет: {self.__color}")

    def print_info(self):
        print(f"Модель: {self.__model}")
        print(f"Мощность двигателя: {self.__engine_power}")
        print(f"Цвет: {self.__color}")
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if isinstance(new_color, str) and new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}.")


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5


vehicle1 = Sedan('Dmitry', 'Mazda Familia', 105, 'brown')

vehicle1.print_info()

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Valentina'

vehicle1.print_info()
