fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)


counts = dict()
for line in fhand:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[1]
    counts[line] = counts.get(line,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
