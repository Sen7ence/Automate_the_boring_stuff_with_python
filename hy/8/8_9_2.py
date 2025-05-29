import re

str = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

adjRegex = re.compile(r'ADJECTIVE')
noun1Regex = re.compile(r'NOUN ([and])')
verbRegex = re.compile(r'VERB')
noun2Regex = re.compile(r'NOUN ([was])')

adj = input('Enter an adjective: ')
noun1 = input('Enter a noun: ')
verb = input('Enter a verb: ')
noun2 = input('Enter a noun: ')


str = adjRegex.sub(adj, str)
str = noun1Regex.sub(noun1+r' \1', str)
str = verbRegex.sub(verb, str)
str = noun2Regex.sub(noun2+r' \1', str)

print(str)
