# strip()正则表达式版本
import re


def strip(s, str=None):
    if str == None:
        return re.sub(r'^\s+|\s+$', '', s)
    else:
        pattern = f'^[{str}]+|[{str}]+$'
        return re.sub(pattern, '', s)


s = '   Hello, World!   '
print(strip(s))  # 输出: 'Hello, World!'
print(strip(s, ' '))  # 输出: 'Hello, World!'
print(strip(s, 'H'))  # 输出: '   Hello, World!   '
print(strip(s, 'H '))  # 输出: 'ello, World!'
