import urllib.request

import urllib.parse
import json
import time
import random
import hashlib
import time


while True:
    content = input('请输入需要翻译的句子(请输入q!推出这个程序)：')
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data = {}

    u = 'fanyideskweb'
    d = content
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    c = 'rY0D^0\'nM0}g5Mm1z%1G4'

    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = f
    data['sign'] = sign
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CL1CKBUTTON'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        "Accept": "application/json,text/javascript,*/*;q = 0.01",
        # "Accept-Encoding": "gzip,deflate",      #### 啥意思。。查。。有它就会错误
        "Accept-Language": "zh-CN,zh;q = 0.8",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "YOUDAO_EAD_UUID=c7c1d171-272e-443f-9d07-d9f8c779342e; _ntes_nnid=f691c54e993915b7e783b9985d6cc6aa,1490533835544; __guid=204659719.1198573978453254000.1502548625976.454; OUTFOX_SEARCH_USER_ID_NCOO=937151153.4321815; P_INFO=userlvkaokao@163.com|1523271382|0|other|00&99|bej&1523189875&hzhr#bej&null#10#0#0|157818&0|hzhr|userlvkaokao@163.com; OUTFOX_SEARCH_USER_ID=-2077552359@180.201.180.165; _ga=GA1.2.667209885.1524559124; JSESSIONID=aaaTQDWkaB_7QbzNHL4nw; monitor_count=1; fanyi-ad-id=44547; fanyi-ad-closed=1; ___rl__test__cookies=1526736521106",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }

    # data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    print(html)

    answer = json.loads(html)

    print(type(answer))
    print(answer['translateResult'][0][0]['tgt'])
    time.sleep(5)
