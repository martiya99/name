import queue
from threading import Thread
from time import sleep
from random import randint

class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None

    def __bool__(self):
        if self.guest == None:
            return False
        return True

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        tau = randint(3, 10)
        sleep(tau)

    def __str__(self):
        return self.name

class Cafe:
    def __init__(self, *tables: Table):
        self.queue = queue.Queue()
        self.tables = {table.number: table for table in tables}
        # self.tables = tables

    def _find_free_table(self):
        for n, table in self.tables.items():
            if not table:
                return n

    def _all_tables_free(self):
        for n, table in self.tables.items():
            if table:
                return False
        return True

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            n = self._find_free_table()
            if n is None:
                self.queue.put(guest)
                print(f'{guest} ждет в очереди...')
            else:
                self.tables[n].guest = guest
                guest.start()
                print(f'{guest} сел(-а) за стол номер {n}.')

    def discuss_guests(self):
        while not (self._all_tables_free() and self.queue.empty()):
            for n, t in self.tables.items():
                if not t.guest is None:
                    if not t.guest.is_alive():
                        print(f'{t.guest} покушал(-а) и ушёл(ушла).\nСтол номер {n} свободен.')
                        if not self.queue.empty():
                            self.tables[n].guest = self.queue.get()
                            self.tables[n].guest.start()
                            print(f'{t.guest} вышел(-ла) из очереди и сел(-а) за стол номер {n}.')
                        else:
                            self.tables[n].guest = None

tables = [Table(number) for number in range(1, 6)]
guests_names = ['Анна-Мария', 'Робин', 'Нами', 'Зоро', 'Санджи', 'Фрэнки', 'Чоппер', 'Луффи', 'Усопп', 'Брук', 'Джимбей']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
