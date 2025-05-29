import re
noNewlineRegex = re.compile('.*')
mo1 = noNewlineRegex.search(
    'Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(mo1.group())

NewlineRegex = re.compile('.*', re.DOTALL)
mo2 = NewlineRegex.search(
    'Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(mo2.group())
