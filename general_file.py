from openpyxl import Workbook
from openpyxl.styles import Alignment
import os
from average_file import create_average_file


def check_files(a):
    check = False
    errs = []
    for i in range(len(a)):
        if os.path.exists(a[i]) == False:
            check = True
            errs.append(str(i+1))

    if check == True:
        b = ", ".join(errs)
        return f'Ошибки в путях к файлам: {b}'
    else:
        create_general_file(a)
        #create_average_file()
        return "Файлы созданы."


def create_general_file(a):
    wb = Workbook()
    b = ["Морской фрахт в порты Дальнего Востока", "Морской фрахт через порт Новороссийска", "Морской фрахт в порт Санкт-Петербург"]
    a = ["фрахт POD DV", "фрахт POD NOV", "фрахт POD SPB", "жд DV", "автовывоз"]
    for i in range(3):
        ws = wb.create_sheet(a[i]) #создание листа
        ws.append((b[i], "", "", "", "", "", "", "", "", "", "", ""))
        ws.append(("", "", "", "", "20\"", "", "40\"", "", "Валидность ставки", "", "", ""))
        ws.append(("Страна", "POL(порт отгрузки)", "Условия ставки", "POD", "фрахт 20\"", "DTHC 20\"", "фрахт 40\"", "DTHC 40\"", "от", "до", "комментарии ( В ТОМ ЧИСЛЕ ЕСЛИ НЕОБХОДИМО,  УКАЗЫВАЕТСЯ ПОРТ ТРАНСШИПМЕНТА, И ЛИНИЯ)", "Экспедитор")) #создание шапки
        rows = 4
        columns = 14
        for j in range(1, columns + 1):
            for k in range(1, rows + 1):
                ws.cell(j, k).alignment = Alignment(horizontal="center", vertical="top")
        ws.merge_cells("A1:L1")
        ws.merge_cells("E2:F2")
        ws.merge_cells("G2:H2")
        ws.merge_cells("I2:J2")
        ws.column_dimensions['A'].width = 15
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 20
        ws.column_dimensions['E'].width = 15
        ws.column_dimensions['F'].width = 15
        ws.column_dimensions['G'].width = 15
        ws.column_dimensions['H'].width = 15
        ws.column_dimensions['I'].width = 10
        ws.column_dimensions['J'].width = 10
        ws.column_dimensions['K'].width = 100
        ws.column_dimensions['L'].width = 20
        rows = ws.max_row+1
        columns = ws.max_column+1
        for j in range(1, columns+1):
            for k in range(1, rows + 1):
                ws.cell(j, k).alignment = Alignment(horizontal="center", vertical="top")


    del wb['Sheet']
    wb.save("ПримерОбъединения.xlsx") #сохранение таблицы