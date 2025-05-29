# 强口令检测
import re


def check_password_strength(password):
    # 长度不少于8个字符
    if len(password) < 8:
        return False
    # 至少有一位数字
    if not re.search(r'\d', password):
        return False
    # 至少有一个小写字母
    if not re.search(r'[a-z]', password):
        return False
    # 至少有一个大写字母
    if not re.search(r'[A-Z]]', password):
        return False
    return True


password = input("请输入密码：")
if check_password_strength(password):
    print("密码强度合格")
else:
    print("密码强度不合格")
