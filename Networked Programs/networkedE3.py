import urllib.request, urllib.parse, urllib.error

user_url = input('Enter URL: ')

try:
    fhand = urllib.request.urlopen(user_url)
except:
    print('Please enter a valid URL')
    exit()

characters = 0
for line in fhand:
    print(line.decode().strip())
    wordslist = line.split()
    characters += len(line)
    if characters > 3000:
        break
print(characters)

#http://data.pr4e.org/romeo-full.txt
