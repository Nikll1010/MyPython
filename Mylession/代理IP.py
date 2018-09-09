import random
import urllib.request
import re

url = 'https://www.whatismyip.com/'
# url = 'https://www.baidu.com'
proxy_support = urllib.request.ProxyHandler({'https': '114.113.126.82:80'})  # 添加代理IP
opener = urllib.request.build_opener(proxy_support)  # 创建一个opener
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
req = urllib.request.Request(url=url, headers=headers)
# req.add_headers = ['User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (Kurl, like Gecko) Chrome/55.0.2883.87 Safari/537.36']
# req.add_headers = ['User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0']
# urllib.request.install_opener(opener)#将代理IP安装到本机，以后访问就会使用代理IP
# url = opener.open(url)
response = urllib.request.urlopen(req)
# url = urllib.request.urlopen('https://www.whatismyip.com')
url = response.read().decode('utf-8')
p = r'(?:(?:[01]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d?\d|2[0-4]\d|25[0-5])'
a = re.findall(p, url)
# a  = url.find("IPv4")
# while a != -1:
#     b = url.find("<", a)
#     c = url[a:b]


print(a)
# print(b)
# print(c)
# print(url)
print(req.headers)
print(req.get_method())
print(response.geturl())
print(response.info())
print(response.getcode())
