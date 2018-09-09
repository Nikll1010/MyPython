import re

g = re.search(r'FishC', 'I love FishC.com!')

print(g)

g = 'I love FishC.com!'.find('FishC')
print(g)
# 正则表达式通配符  .点号能匹配除换行外的任何字符
g = re.search(r'.', 'I love FishC.com!')
print(g)
g = re.search(r'Fish.', 'I love FishC.com!')  # 匹配Fish+一个字符
print(g)
g = re.search(r'', 'I love FishC.com!')

# 用\消除.的匹配功能
g = re.search(r'\.', 'I love FishC.com!')
print(g)
g = re.search(r'\d', 'I love 123FishC.com!')
print(g)

g = re.search(r'\d\d', 'I love 123FishC.com!')
print(g)

# 匹配IP地址
g = re.search(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d', '192.168.000.001')
print(g)

g = re.search(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d', '192.168.1.1')
print(g)

# []创建字符类
g = re.search(r'[aeiou]', 'I love FishC.com!')  # 有大小写敏感模式
print(g)

g = re.search(r'[aeiouAEIOU]', 'I love FishC.com!')  # 有大小写敏感模式
print(g)
g = re.search(r'[a-z]', 'I love FishC.com!')  # 有大小写敏感模式
print(g)
# g.group(1)
g = re.search(r'[1-9]', 'I love 123FishC.com!')  # 有大小写敏感模式
print(g)

# 限定匹配的次数,用{}限定

g = re.search(r'ab{3}c', 'abbbc')  # 有大小写敏感模式
print(g)
g = re.search(r'ab{4}c', 'abbbc')  # 有大小写敏感模式
print(g)
# 3到10次
g = re.search(r'ab{3,10}c', 'abbbbbbbbbbbbbbbbbbbbbbbc')  # 有大小写敏感模式
print(g)

g = re.search(r'ab{3,10}c', 'abbbbbbbbbc')  # 有大小写敏感模式
print(g)
# g.group(1)
g = re.search(r'[0-255]', '355')  # 有大小写敏感模式，正则表达式将数字作为字符匹配
print(g)


#自定义匹配规则
g = re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '188')  # 有大小写敏感模式
print(g)
#匹配IP规则
g = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', '192.168.0.1')  # 有大小写敏感模式
print(g)

g = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])', '192.168.0.1')  # 有大小写敏感模式
print(g)

g = re.search(r'\w','我爱鱼C工作室')
print(g)


g = re.findall(r'\w','我爱鱼C工作室')
print(g)
