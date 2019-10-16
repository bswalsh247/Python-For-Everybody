import re

fhand = open('mbox-short.txt')

#starts up some required variables
count = 0
sum = 0

for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    # if len(stuff) !=[]: continue
    if len(x) > 0:
        num = float(x[0])
        sum += num
        count += 1

# calculations average prints it
average = sum / count

print(average)
