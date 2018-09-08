import urllib.request
import os
response = urllib.request.urlopen('http://placekitten.com/g/200/300')
cat_img = response.read()
with open('cat_200_301.jpg','wb') as f:
    f.write(cat_img)
