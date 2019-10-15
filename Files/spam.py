#Gets the name of the file
fname = input('Enter the file name: ')
fhand = open(fname)

#Tries to open the file and if it fails kill the program
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

#starts up some required variables
count = 0
sum = 0

#If a line start X_DSPAM...it will add the float to the sum and 1 to count
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        num = float(line[21:])
        sum += num
        count += 1

# calculations average prints it
average = sum / count

print('Average spam confidence', average)
