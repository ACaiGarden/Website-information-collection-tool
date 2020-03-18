url = 'www.baidu.com'

result = url.split('.')
print(result)
for x in result:
    if x != 'www':
        name = x
        break
else:
    name = 'None_name'

print(name)