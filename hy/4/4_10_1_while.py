# 逗号代码
def string_to_list(list):
    string = list[0]
    index = 1
    while index < len(list)-1:
        string = string + ',' + list[index]
        index += 1
    else:
        string = string + ' and ' + list[index]
    return string


spam = ['apples', 'bananas', 'tofu', 'cats']
print(string_to_list(spam))
