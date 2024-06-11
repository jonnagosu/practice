sum = 0

for n in range(500,1000+1):
    if n%7==0:
        sum = sum + n

print(f'500 부터 1000 사이의 7의 배수들의 합은 {sum}입니다.')