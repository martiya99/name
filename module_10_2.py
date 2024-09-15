from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        self.kname = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.kname}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.kname} сражается {days} суток, осталось {enemies} врагов.')
        print(f'{self.kname} одержал победу спустя {days} дней(я)!')

knight1 = Knight('Луффи', 15)
knight2 = Knight('Зоро', 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы завершены! Враг разгромлен!')
