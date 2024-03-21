import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment


def create_average_file(gen_name, avg_name):
    wb = Workbook()
    book = openpyxl.load_workbook((a[0]))
    sheets_num = len(book.sheetnames)
    row_num = [0 for i in range(sheets_num)]
    for i in range(sheets_num):
        wa = book.worksheets[i]
        ws = wb.create_sheet(wa.title)  # создание листа
        for row in wa:
            r = 0
            for cell in row:
                if (int(cell.coordinate[1::]) == 1 or int(cell.coordinate[1::]) > 7) and r == 0:
                    row_num[i] += 1
                    r = 1
                    if cell.value is None:
                        ws[cell.coordinate[0] + str(row_num[i])].value = cell.value
                    else:
                        if str(cell.value).isdigit():
                            ws[cell.coordinate[0] + str(row_num[i])].number_format = cell.number_format[:23]
                            ws[cell.coordinate[0] + str(row_num[i])].value = cell.value
                        else:
                            ws[cell.coordinate[0] + str(row_num[i])].value = cell.value
                elif int(cell.coordinate[1::]) == 1 or int(cell.coordinate[1::]) > 7 and r == 1:
                    if cell.value is None:
                        ws[cell.coordinate[0] + str(row_num[i])].value = cell.value
                    else:
                        if str(cell.value).isdigit():
                            ws[cell.coordinate[0] + str(row_num[i])].number_format = cell.number_format[:23]
                            ws[cell.coordinate[0] + str(row_num[i])].value = cell.value

                        else:
                            ws[cell.coordinate[0] + str(row_num[i])].value = cell.value
    del wb['Sheet']
    wb.save(f"{gen_name}.xlsx")
