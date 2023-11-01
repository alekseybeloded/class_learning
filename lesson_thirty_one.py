def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as z:
        print(z)
        return 0, 0
    finally:
        print('finally выполняется до return')


x, y = get_values()
print(x, y)
