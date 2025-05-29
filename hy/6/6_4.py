# 在Wiki标记中添加无序列表 bulletPointAdder.py
import pyperclip
text = pyperclip.paste()  # 从剪贴板中获取文本

lines = text.split('\n')  # 将文本按行分割
for i in range(len(lines)):  # 遍历每一行
    lines[i] = '* ' + lines[i]  # 在每一行前添加'* '

text = '\n'.join(lines)  # 将列表转换为字符串

pyperclip.copy(text)  # 将文本复制到剪贴板
