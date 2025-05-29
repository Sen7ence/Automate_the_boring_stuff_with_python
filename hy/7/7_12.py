import re
namesRegex = re.compile(r'Agent \w+')  # 正则表达式为字符串Agent加上空格及空格后第一个单词
mo = namesRegex.sub(
    'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

# 正则表达式为字符串Agent加上空格及空格后第一个单词，其中单词第一个字母放入分组1
agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(
    r'\1*****', 'Agent Alice gave the secret documents to Agent Bob.')  # \1表示第一个括号内的内容
print(mo)  # 输出: A***** gave the secret documents to B*****
