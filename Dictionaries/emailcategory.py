# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

fname = input('Enter file name: ')
fhand = open(fname)

counts = dict()
for line in fhand:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[2]
    counts[line] = counts.get(line,0) + 1

print(counts)
