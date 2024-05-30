
# 슬라이싱 연습

num = str(input('주민등록번호를 입력하세요. \n (-를 넣어서 입력) ->'))
name = input('\n 이름을 입력해주세요 ->')

# ex: 021010-1234567

print("\n")
print(f'출생년도: {num[0:2]}년 {num[2:4]}월 {num[4:6]}일')
if int(num[7]) == 1 or 3: 
    print('성별: 남자')
elif int(num[7]) == 2 or 4:
    print('성별: 여자')
else: print('성별: 기타')
# 기타 성별이란게 있을 수 있나..? 아직 while문을 안 배움..
print(f"이름: {name}")

is_you = (input('본인이 맞으신가요? \n(맞으면 <네>, 틀리면 <아니요> 를 입력해주세요. ->)')) 

if is_you == str('네'):
    print(f'Access, Welcome {name}')
else:
    print('다시 실행해주세요.')
    
# 네 이외의 o 등의 대답이 입력되어도 else값이 나옴. 나민혁 기술력 한계..