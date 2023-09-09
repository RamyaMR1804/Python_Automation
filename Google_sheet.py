import gspread

gc=gspread.service_account('Secret.json')

spreadsheet = gc.open('Sample')
#sheet by index
worksheet = spreadsheet.get_worksheet(0)
# sheet by name
#worksheet = spreadsheet.worksheet('Sheet1')
data = worksheet.get_all_records()
print(data[10])

Value = worksheet.get_values('A5:E5')
print(Value)

column = worksheet.col_values(2)
print(column)

rows= worksheet.row_values(7)
print(rows)

cell = worksheet.acell('B9').value
print(cell)

cell = worksheet.find('13')
print(cell.row,cell.col)

cell = worksheet.findall('13')

for i in cell:
    print(i.row,i.col)


worksheet.update('F1', "it's down there somewhere, let me take another look.")

worksheet.update_cells(11,11,-9999)