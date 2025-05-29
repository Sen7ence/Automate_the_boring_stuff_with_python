# 定义collatz函数
def collatz(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)

# 使用try-except捕获用户输入错误
while True:
    try:
        # 用户输入一个整数
        num = int(input("请输入一个整数: "))
        break  # 如果输入有效，跳出循环
    except ValueError:
        # 如果发生ValueError，提示用户输入错误
        print("错误: 必须输入一个整数！请重新输入。")

# 不断调用collatz直至num值为1
while num!=1:
    num=collatz(num)
    print(num)