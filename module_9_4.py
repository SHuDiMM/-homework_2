first = 'Мама мыла раму'

second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "a", encoding="utf-8") as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything


import random


class MysticBall:
    def __init__(self, *words):
        if not isinstance(words, (list, tuple, set)) or not all(isinstance(word, str) for word in words):
            raise ValueError("Атрибут 'words' должен быть коллекцией строк.")
        self.words = list(words)

    def __call__(self):
        return random.choice(self.words)


write = get_advanced_writer('example.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())

print(first_ball())

print(first_ball())
