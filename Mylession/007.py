import urllib.request

response = urllib.request.urlopen('http://shared.ydstatic.com/api/fanyi-web/assets/index.min.js')
html = response.read()
html = html.decode('utf-8')
print(html)
