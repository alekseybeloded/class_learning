class ExceptionPrint(Exception):
    '''Общий класс исключения принтера'''

class ExceptionPrintSendData(ExceptionPrint):
    '''Класс исключения при отправке данных принтеру'''


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('принтер не отвечает')

    def send_to_print(self, data):
        return False


p = PrintData()
p.print('123')
