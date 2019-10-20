# # Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.
import socket

user_url = input('Enter URL: ')

try:
    host_name = user_url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    cmd = ('GET ' + user_url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
except:
    print('Please enter a valid URL')
    exit()

count = 0
while True:
    data = mysock.recv(3000)
    count += len(data)
    if len(data) < 1:
        break
    print(data.decode(),count,end='')

mysock.close()

# count = 0
# while True:
#     data = mysock.recv(512)
#     count += len(data)
#     if (len(data) < 1) or count >= 3000:
#         break
#     print data
#
# mysock.close()
# print count
