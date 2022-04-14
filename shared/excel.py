from openpyxl import Workbook
from write.config import EXCEL_SAVE_PATH

wb = Workbook( )
ws = wb.active
ws.title = "sellings"
ws.cell(row=1, column=2, value=70)
wb.save(EXCEL_SAVE_PATH)