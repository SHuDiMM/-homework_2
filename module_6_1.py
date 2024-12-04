class Animal():
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
        else:
            print(f'Это не растение. {self.name} не стал это есть')
            self.alive = False



class Plant():
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
print(a1.name)
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')

a3 = Mammal("Выхухоль")

print(a1.name)

print(p1.name)

print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)

print(a3.name)

a2.eat(a3)

print(a2.alive)

f1 = "Шашлык"

a1.eat(f1)

print(a1.fed)

print(a1.alive)