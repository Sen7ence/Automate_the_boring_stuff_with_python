def printTable(tableData):
    # 初始化各列宽度列表
    colWidths = [0] * len(tableData)
    # 计算每列的最大宽度
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])
    # 打印表格，注意原来每行变为了每列
    for i in range(len(tableData[i])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print()


tableData = [['apples', 'oranges', 'sherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
