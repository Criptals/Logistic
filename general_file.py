import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment
from average_file import create_average_file

def create_general_file(a, gen_name, avg_name):
    wb = Workbook()
    book = openpyxl.load_workbook((a[0]))
    sheets_num = len(book.sheetnames)
    row_num = [0 for i in range(sheets_num)]
    for i in range(sheets_num):
        wa = book.worksheets[i]
        ws = wb.create_sheet(wa.title) #создание листа
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
    files_num = len(a)
    for i in range(1, files_num):
        book = openpyxl.load_workbook((a[i]))
        wb = openpyxl.load_workbook(f"{gen_name}.xlsx")
        a = book.sheetnames.index('авто')
        row_num[a] -= 9
        for j in range(sheets_num):
            wa = book.worksheets[j]
            ws = wb.worksheets[j]
            for row in wa:
                r = 0
                for cell in row:
                    if int(cell.coordinate[1::]) > 9 and r == 0:
                        row_num[j] += 1
                        r = 1
                        if cell.value is None:
                            ws[cell.coordinate[0] + str(row_num[j])].value = cell.value
                        else:
                            if str(cell.value).isdigit():
                                ws[cell.coordinate[0] + str(row_num[j])].number_format = cell.number_format[:23]
                                ws[cell.coordinate[0] + str(row_num[j])].value = cell.value
                            else:
                                ws[cell.coordinate[0] + str(row_num[j])].value = cell.value
                    elif int(cell.coordinate[1::]) > 9 and r == 1:
                        if cell.value is None:
                            ws[cell.coordinate[0] + str(row_num[j])].value = cell.value
                        else:
                            if str(cell.value).isdigit():
                                ws[cell.coordinate[0] + str(row_num[j])].number_format = cell.number_format[:23]
                                ws[cell.coordinate[0] + str(row_num[j])].value = cell.value
                            else:
                                ws[cell.coordinate[0] + str(row_num[j])].value = cell.value
            wb.save(f"{gen_name}.xlsx")
    wb = openpyxl.load_workbook(f"{gen_name}.xlsx")
    del wb["Лист1"]
    wb.save(f"{gen_name}.xlsx")

    wb = openpyxl.load_workbook(f"{gen_name}.xlsx")
    for i in range(sheets_num-1):
        ws = wb.worksheets[i]
        columns = ws.max_row
        rows = ws.max_column
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
    wb.save(f"{gen_name}.xlsx")
    #create_average_file(gen_name=gen_name, avg_name=avg_name)

     # сохранение таблицы