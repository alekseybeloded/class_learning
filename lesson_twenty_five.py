class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        print('init Mixinlog')
        self.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f'{self.id}: товар был продан в 00:00 часов')

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class NoteBook(Goods, MixinLog):
    pass


n = NoteBook('Acer', 1.5, 30000)
n.print_info()
print(NoteBook.__mro__)
