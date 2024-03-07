from openpyxl import Workbook
from openpyxl.styles import Alignment


def create_average_file(a):
    wb = Workbook()
    ws = wb.create_sheet("") #создание листа
    ws.append(()) #создание шапки

    wb.save("") #сохранение таблицы

