import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f"{self.name}, а нас напали!")
        enemy = 100
        days = 0
        while enemy:
            enemy -= self.power
            days += 1
            time.sleep(1)
            print(f"{self.name} сражается {days} день(дня), осталость {enemy} войнов")

        print(f"{self.name} одержал победу спустя {days} день(дня)!")


first_knight = Knight('Sir Lancelot', 10)

second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы окончены.")
