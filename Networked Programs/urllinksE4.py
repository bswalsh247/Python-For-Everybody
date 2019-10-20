# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
paragraphs = soup.find('p')
# count = 0
# for paragraph in paragraphs:
#     count += len(paragraph)
#     print(count)


    linecount = 0
    paragraphcount = 0
    empty = True
    for i in f:
        if '\n' in i:
            linecount += 1
            if len(i) < 2:
                empty = True
            elif len(i) > 2 and empty is True:
                paragraphcount = paragraphcount + 1
                empty = False
            if empty is True:
                paragraphnumber = 0
            else:
                paragraphnumber = paragraphcount
        print('%-4d %4d %s' % (paragraphnumber, linecount, i))
