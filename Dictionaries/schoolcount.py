fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'
fhand = open(fname)

counts = dict()     # Initialize variables
for line in fhand:
    if not line.startswith('From '): continue
    line = line.split()
    atpos = line[1].find('@')   # Position of '@'
    domain = line[1][atpos+1:]  # Store characters after '@'
    counts[domain] = counts.get(domain,0) + 1

print(counts)
