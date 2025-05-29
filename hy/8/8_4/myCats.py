import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
# [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
