import urllib.request
import re


def gteurl(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (Kurl, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    rep = urllib.request.urlopen(req)
    url = rep.read().decode('utf-8')
    print(url)
    return url


def getimg(url):
    p = r'<img class="BDE_Image" pic_type="1" src="([^"+\.jpg)"'
    imglist = re.findall(p, url)
    # for each in imglist:
    #     print(each)
    for each in imglist:
        filename = each.split('/')[-1]
        urllib.request.urlretrieve(each, filename)


def downloadtieba():
    url = 'https://tieba.baidu.com/p/5812213113'
    getimg(gteurl(url))


if __name__ == '__main__':
    downloadtieba()
