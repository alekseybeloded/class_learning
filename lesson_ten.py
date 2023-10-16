from string import ascii_letters


class Person:

    def __init__(self, fio: str, old: int, ps: int, weight: float) -> None:
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio: str):
        if type(fio) is not str:
            raise TypeError('ФИО должны быть строкой')

        fio_split = fio.split()
        if len(fio_split) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters
        for word in fio_split:
            if len(word) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(word.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 60:
            raise TypeError('Возраст должен быть целым числом в диапазоне [14; 120]')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 40:
            raise TypeError('Вес должен быть вещественным числом от 40 и выше')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой')

        passport_split = ps.split()
        if len(passport_split) != 2 or len(passport_split[0]) != 4 or len(passport_split[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for number in passport_split:
            if not number.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @old.setter
    def passport(self, passport):
        self.verify_ps(passport)
        self.__passport = passport




p = Person('Ivanov Ivan Ivanovich', 30, '1234 567890', 80.0)
p.old = 50
p.passport = '4567 123456'
p.weight = 70.0
print(p.old)
