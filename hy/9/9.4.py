# 将带有美国风格日期的文件改名为欧洲风格日期

import shutil, os, re

# 创建一正则表达式用于识别美国风格日期
datePattern = re.compile(
    r"""
        ^(.*?) # 匹配文件名的开头部分
        ((0|1)?\d)- # 匹配月份
        ((0|1|2|3)?\d)- # 匹配日期
        ((19|20)\d{2}) # 匹配年份
        (.*?)$ # 匹配文件名的结尾部分
    """,
    re.VERBOSE,
)

# 识别文件名中的日期部分
for amerFilename in os.listdir("."):  # 遍历当前目录下的所有文件
    mo = datePattern.search(amerFilename)  # 搜索符合日期格式的文件名

    # 如果没有匹配到日期格式，则跳过
    if mo == None:
        continue
    # 如果匹配到日期格式，则提取各部分
    beforePart = mo.group(1)  # 文件名前缀
    monthPart = mo.group(2)  # 月份部分
    dayPart = mo.group(4)  # 日期部分
    yearPart = mo.group(6)  # 年份部分
    afterPart = mo.group(8)  # 文件名后缀

    # 构建新的文件名
    euroFilename = f"{beforePart}{dayPart}-{monthPart}-{yearPart}{afterPart}"

    # 获取文件的绝对路径
    absWorkingDir = os.path.abspath(".")  # 获取当前工作目录的绝对路径
    amerFilename = os.path.join(absWorkingDir, amerFilename)  # 拼接绝对路径和文件名
    euroFilename = os.path.join(absWorkingDir, euroFilename)  # 拼接绝对路径和新文件名
    # 重命名文件
    print(f"Renaming '{amerFilename}' to '{euroFilename}'...")
    shutil.move(amerFilename, euroFilename)  # 使用shutil.move重命名文件
