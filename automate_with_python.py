import openpyxl
workbook = openpyxl.load_workbook('workshop_feeding.xlsx')
sheet = workbook['Feeding']
cell = sheet.cell(1, 1)
print(cell.value)
