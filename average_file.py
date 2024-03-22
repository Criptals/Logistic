import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment


def create_average_file(gen_name, avg_name):
    wb = Workbook()
    book = openpyxl.load_workbook(f"{gen_name}.xlsx")
    sheets_num = len(book.sheetnames)
    all_data = []
    #row_num = [0 for i in range(sheets_num)]
    for i in range(sheets_num):
        sheet_data = []
        wa = book.worksheets[i]
        ws = wb.create_sheet(wa.title)  # создание листа
        for row in wa:
            row_data = []
            for cell in row:
                if int(cell.coordinate[1::]) < 4:
                    ws[cell.coordinate].value = cell.value
                else:
                    row_data.append(cell.value)
            sheet_data.append(row_data)
        if i < 3:
            ws.delete_cols(4, 1)
            ws.delete_cols(5, 1)
            ws.delete_cols(6, 5)
            for k in sheet_data:
                k.pop(3)
                k.pop(4)
                k.pop(5)
                k.pop(5)
                k.pop(5)
                k.pop(5)
                k.pop(5)
        elif i == 3:
            ws.delete_cols(2, 1)
            ws.delete_cols(3, 1)
            ws.delete_cols(7, 6)
            for k in sheet_data:
                k.pop(1)
                k.pop(2)
                k.pop(6)
                k.pop(6)
                k.pop(6)
                k.pop(6)
                k.pop(6)
                k.pop(6)
        elif i == 4:
            ws.delete_cols(10, 2)
            for k in sheet_data:
                k.pop(9)
                k.pop(9)
    del wb['Sheet']
    wb.save(f"{avg_name}.xlsx")
    wb = openpyxl.load_workbook(f"{avg_name}.xlsx")
    for i in range(sheets_num):
        ws = wb.worksheets[i]
        columns = ws.max_row
        rows = ws.max_column
        for j in range(1, columns + 1):
            for k in range(1, rows + 1):
                ws.cell(j, k).alignment = Alignment(horizontal="center", vertical="top")
        if i < 3:
            ws.merge_cells("A1:E1")
            ws.column_dimensions['A'].width = 15
            ws.column_dimensions['B'].width = 30
            ws.column_dimensions['C'].width = 15
            ws.column_dimensions['D'].width = 15
            ws.column_dimensions['E'].width = 15
        elif i == 3:
            ws.merge_cells("A1:G1")
            ws.column_dimensions['A'].width = 15
            ws.column_dimensions['B'].width = 10
            ws.column_dimensions['C'].width = 20
            ws.column_dimensions['D'].width = 20
            ws.column_dimensions['E'].width = 20
            ws.column_dimensions['F'].width = 20
        elif i == 4:
            ws.merge_cells("A1:J1")
            ws.merge_cells("E2:G2")
            ws.merge_cells("H2:I2")
            ws.column_dimensions['A'].width = 20
            ws.column_dimensions['B'].width = 15
            ws.column_dimensions['C'].width = 25
            ws.column_dimensions['D'].width = 35
            ws.column_dimensions['E'].width = 20
            ws.column_dimensions['F'].width = 20
            ws.column_dimensions['G'].width = 15
            ws.column_dimensions['H'].width = 20
            ws.column_dimensions['I'].width = 15
            ws.column_dimensions['J'].width = 80
    wb.save(f"{avg_name}.xlsx")
