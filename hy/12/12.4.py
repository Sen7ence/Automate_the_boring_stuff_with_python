# 从电子表格中读取数据，计算总人口，以及每个县的普查区的数目

import openpyxl

# 第一步：读取电子表格数据
wb = openpyxl.load_workbook(r"hy\12\censuspopdata.xlsx")
sheet = wb["Population by Census Tract"]  # 获取指定工作表

# 第二步：创建一个字典来存储每个州的总人口和县的普查区数目
data = {}  # 字典格式：{州名: {县名: {'population': 总人口, 'tracts': 普查区数目}}}
for row in range(2, sheet.max_row + 1):
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    data.setdefault(state, {})  # 确保州名存在于字典中
    data[state].setdefault(
        county, {"population": 0, "tracts": 0}
    )  # 确保县名存在于州的字典中
    data[state][county]["population"] += pop  # 累加人口
    data[state][county]["tracts"] += 1  # 累加普查区数目

# 第三步：将结果打印出来
for state, counties in data.items():
    print(f"{state}州:")
    for county, info in counties.items():
        print(f'  {county}县: {info["population"]}人, {info["tracts"]}个普查区')
    print()  # 添加空行以便于阅读
