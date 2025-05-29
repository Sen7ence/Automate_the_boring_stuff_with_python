# 逗号代码
def string_to_list(list):
    string = ''
    for i in list:
        if i == list[-1]:
            string = string + ' and ' + i
        elif i == list[0]:
            string = string + i
        else:
            string = string + ', ' + i
    return string


spam = ['apples', 'bananas', 'tofu', 'cats']
print(string_to_list(spam))
