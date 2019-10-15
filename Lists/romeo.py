#Opens the name of the file
fhand = open('romeo.txt')

#create empty list
lst = list()

# Iterate through each line in filehandle
for line in fhand:
    # Iterate through each word on line
    for wrd in line.split():
        #Checks to see if word is already in list
        if not wrd in lst:
            #Appends words to list
            lst.append(wrd)

lst.sort()
print(lst)
