import re

input_regex = input('Enter a regular expression: ')
str_regex = str(input_regex)
fhand = open('mbox-short.txt')

count = 0

for line in fhand:
    line = line.rstrip()
    if re.findall(str_regex, line) != []:
        count += 1

print('mbox.txt had ' +  str(count) + ' lines that matched ' + str_regex)
