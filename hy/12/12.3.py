import openpyxl

wb = openpyxl.load_workbook(r"hy\12\example.xlsx")
sheets = wb.sheetnames  # 获取所有工作表名称
print(sheets)  # 打印工作表名称列表
sheet = wb["Sheet1"]  # 获取指定工作表
print(sheet.title)  # 打印工作表名称
