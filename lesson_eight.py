class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()
th2.id = 2
print(th1.id)
