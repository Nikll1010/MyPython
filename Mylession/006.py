import urllib.request
req = urllib.request.Request('http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule')
data = {}


response = urllib.request.urlopen(req)

html = response.read()
html = html.decode('utf-8')
print(html)
