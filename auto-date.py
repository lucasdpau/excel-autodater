import openpyxl, datetime

wb = openpyxl.load_workbook("test.xlsx")
worksheet = wb.active
print(worksheet)
cell_a1 = worksheet["A1"]
cell_a2 = worksheet["A2"]
cell_a3 = worksheet["A3"]
cell_a4 = worksheet["A4"]
cell_b1 = worksheet["B1"]

def format_cell_date(cell): 
    cell_in_iso_format = cell.value.date().isoformat()
    return cell_in_iso_format

def get_today():
    today = datetime.date.today().isoformat()
    print(today)
    return today

def see_if_date_has_passed(date):
    print(date)
    return date <= get_today()
    
if __name__ == "main":
    pass