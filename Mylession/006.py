import urllib.request
import urllib.parse
import hashlib
import time
import random

# req = urllib.request.Request('http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule')
# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
content = input('请输入要翻译的句子：\n')

u = 'fanyideskweb'
d = content
f = str(int(time.time() * 1000) + random.randint(1, 10))
c = 'ebSeFb%=XZ%T[KZ)c(sy!'

sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
data = {'action': 'FY_BY_CLICKBUTTION', 'client': 'fanyideskweb', 'doctype': 'json', 'from': 'AUTO', 'i': content,
        'keyfrom': 'fanyi.web', 'salt': f, 'sign': sign, 'smartresult': 'dict', 'to': 'AUTO', 'typoResult': 'false',
        'version': '2.1'}
# data = {"i": content,
#         "from": "AUTO",
#         "to": "AUTO",
#         "smartresult": "dict",
#         "client": "fanyideskweb",
#         "salt": f,  ### 盐：很长的随机串，防止用字典反推
#         "sign": sign,  ## 签名：js加密
#         "doctype": "json",
#         "version": "2.1",
#         "keyfrom": "fanyi.web",
#         "action": "FY_BY_REALTIME",
#         "typoResult": "false"}
data = urllib.parse.urlencode(data).encode('utf-8')

# headers = {
#     "Accept": "application/json,text/javascript,*/*;q = 0.01",
#     # "Accept-Encoding": "gzip,deflate",      #### 啥意思。。查。。有它就会错误
#     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#     "Connection": "keep-alive",
#     "Content-Length": len(data),
#     "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#     "Cookie": "YOUDAO_EAD_UUID=c7c1d171-272e-443f-9d07-d9f8c779342e; _ntes_nnid=f691c54e993915b7e783b9985d6cc6aa,1490533835544; __guid=204659719.1198573978453254000.1502548625976.454; OUTFOX_SEARCH_USER_ID_NCOO=937151153.4321815; P_INFO=userlvkaokao@163.com|1523271382|0|other|00&99|bej&1523189875&hzhr#bej&null#10#0#0|157818&0|hzhr|userlvkaokao@163.com; OUTFOX_SEARCH_USER_ID=-2077552359@180.201.180.165; _ga=GA1.2.667209885.1524559124; JSESSIONID=aaaTQDWkaB_7QbzNHL4nw; monitor_count=1; fanyi-ad-id=44547; fanyi-ad-closed=1; ___rl__test__cookies=1526736521106",
#     "Host": "fanyi.youdao.com",
#     "Origin": "http://fanyi.youdao.com",
#     "Referer": "http://fanyi.youdao.com/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
# }

headers = {
    "Accept": "application/json,text/javascript,*/*;q = 0.01",
    # "Accept-Encoding": "gzip,deflate",      #### 啥意思。。查。。有它就会错误
    "Accept-Language": "zh-CN,zh;q = 0.8",
    "Connection": "keep-alive",
    "Content-Length": len(data),
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Cookie": "YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=-903753322@10.169.0.83; JSESSIONID=aaajckhYLgskf-P4elKww; ___rl__test__cookies=1536073311658; OUTFOX_SEARCH_USER_ID_NCOO=259638459.6742181",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
}

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
req = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(req)

html = response.read()
html = html.decode('utf-8')
print(html)
