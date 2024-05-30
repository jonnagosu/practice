url = input('url을 입력하세요')
url_str = url.replace('http://','')
url_str = url_str[:url_str.index('.')]

password = url_str[:3] + str(len(url_str)) + str(url.count('e')) + '!'
print(password)