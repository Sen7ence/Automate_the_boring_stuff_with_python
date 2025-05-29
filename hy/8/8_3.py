import shelve
shelfFile = shelve.open('mydata')
cats = ['a', 'b', 'c']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))  # <class 'shelve.DbfilenameShelf'>
print(shelfFile['cats'])  # ['a', 'b', 'c']
print(list(shelfFile.keys()))  # ['cats']
print(list(shelfFile.values()))  # [['a', 'b', 'c']]
