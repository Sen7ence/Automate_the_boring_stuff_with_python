# 电话号码和E-mail地址提取程序
import pyperclip
import re

# 创建一个正则表达式对象，用于匹配电话号码和E-mail地址
phoneRegex = re.compile(r'''(
            (\d{3}|\(d{3}\))?           #区号两种形式三个数或带括号的三个数，可选
            (\s|-|\.)?                  #分隔符三种，空格，-，.，可选
            (\d{3})                     #前三位数，必选
            (\s|-|\.)                   #分隔符三种，空格，-，.，必选
            (\d{4})                     #后四位数，必选
            (\s*(ext|x|ext.)\s*\d{2,5})?#分机号，任意空格，ext或x或ext.，任意空格，2-5位数，可选
            )''', re.VERBOSE)

emailRegex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+           #用户名：字母，数字，下划线，点，百分号，加号，减号
            @                           #@符号
            [a-zA-Z0-9.-]+              #域名：字母，数字，下划线，点，百分号，加号，减号
            (\.[a-zA-Z]{2,4})           #后缀名：点加2-4位字母
            )''', re.VERBOSE)

# 获取剪贴板中的文本
text = str(pyperclip.paste())

# 在文本中查找所有匹配的电话号码和E-mail地址
matches = []
for groups in phoneRegex.findall(text):
    # groups[1]是区号，groups[3]是前三位数，groups[5]是后四位数
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':  # groups[8]是分机号，如果不为空，则添加分机号
        phoneNum += ' x' + groups[8]  # groups[8]是分机号，
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])  # groups[0]是E-mail地址

# 将匹配的电话号码和E-mail地址复制到剪贴板
if len(matches) > 0:
    # 将匹配的电话号码和E-mail地址用换行符连接起来，变为一整个字符串，复制到剪贴板
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))  # 打印匹配的电话号码和E-mail地址
else:
    print('No phone numbers or email addresses found.')
# 如果没有匹配的电话号码和E-mail地址，则打印提示信息
