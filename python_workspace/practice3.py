print('사이트 별로 비밀번호를 만들어 드립니다.')
url = input('\n 비밀번호를 만들 웹사이트 주소를 입력해주세요. \n (http://를 입력, www는 제외) ->')

print(' 생성된 비밀번호는 :end=' '')
print(url[7:10] + str(len(url[7:url.index('.')])) + str(url.count('e')) + '!')