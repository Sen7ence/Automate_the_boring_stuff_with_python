import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}
for character in message:
    count.setdefault(character, 0)  # 记录出现的字符，第一次出现时设为0
    count[character] += 1  # 统计字符出现的次数

pprint.pprint(count)
