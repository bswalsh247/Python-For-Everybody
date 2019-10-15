fname = input('Enter file name: ')
fhand = open(fname)

counts = dict()
for line in fhand:
    if not line.startswith('From ') : continue
    line = line.split()
    line = line[1]
    counts[line] = counts.get(line, 0) + 1

print(counts)
