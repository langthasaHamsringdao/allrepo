from openpyxl import Workbook

workbook = Workbook()

sheet = workbook.active

sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

workbook.save(filename='hello_world.xlsx')
