try:
    x, y = map(int, input().split())
    res = x / y
except ValueError:
    print('Ошибка типа данных')
except ArithmeticError:
    print('Деление на ноль')
