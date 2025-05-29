# 口令保管箱
# 账户名称及口令
import sys
import pyperclip
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

# 处理命令行参数
if len(sys.argv) < 2:
    print('Usage: python 6_3.py [account]-copy account password')
    sys.exit()

account = sys.argv[1]  # 账户名称

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])  # 复制口令到剪贴板
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account + '.')
