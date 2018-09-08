import urllib.request
import os


def gethtml(url):
    url = urllib.request.Request('http://i.jandan.net/ooxx/page-41#comments')
    req = urllib.request.urlopen(url)
    html = req.read().decode('utf-8')  # j将网页元素抓取下来
    print(html)
    return html


#
# with open('002.jpg', 'wb') as f:
#     f.write(html)

def downloadmm(folder='ooxx', page=10):
    os.makedirs()
