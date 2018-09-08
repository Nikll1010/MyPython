import urllib.request
import os


def url_open(url):
    # req = urllib.request.Request('url')
    # # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (Kurl, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    # req1 = urllib.request.urlopen(req)
    req = urllib.request.urlopen(url)
    url = req.read()  # j将网页元素抓取下来
    # print(url)
    return url


def geturl(url):
    url = url_open(url).decode('utf-8')
    # url = url.encode('utf-8')
    # print(url)
    a = url.find("current-comment-page") + 23
    b = url.find("]", a)
    c = url[a:b]
    # print(c)
    return url[a:b]


def get_page(url):
    pass


#
# with open('002.jpg', 'wb') as f:
#     f.write(url)

def find_imgs(url):
    url = url_open(url).decode('utf-8')
    print(url)
    img_adress = []
    a = url.find("src=")
    while a != -1:
        b = url.find('jpg', a, a + 255)
        if b != -1:
            img_adress.append(url[a + 9:b + 4])
            print(img_adress)
        else:
            b = a + 9
        a = url.find("src=", b)
    return img_adress


def save_imgs(img_adress):
    for each in img_adress:
        filename = each.split('/'[-1])
        # assert isinstance(each.split, object)
        img = url_open(each)
        # print(each)
        # img = imgread.read()
        with open(filename, 'wb') as f:
            f.write(img)


def downloadmm(folder='xxoo', page=10):
    os.rmdir('xxoo')
    os.makedirs(folder)
    os.chdir(folder)
    url = "http://i.jandan.net/ooxx/"  # http://i.jandan.net/ooxx/page-41#comments
    try:
        page_num = int(geturl(url))
        # page_num = 41
    except:
        print('一场错误')

    for i in range(page):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_adress = find_imgs(page_url)
        save_imgs(img_adress)


if __name__ == '__main__':
    downloadmm()
