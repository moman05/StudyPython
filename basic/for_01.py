# for문 학습
#arr = [1, 2, 3, 4, 5]
'''다중문자열 == 여러줄 주석'''
# 한줄 주석

"""
result = 0

for x in range(1,101):
    result = result + x

print('배열의 합 =', result)

arr2 = ('me', 'my', 'friend', 'jane')  #튜플이든 리스트든 상관X

for i in arr2:
    print(f'{i * 2}') #print(f'{i:>10}')  #총 10글자로 맞춰줌
"""

## 1~10까지 수에서 짝수 구분하기
"""
for num in range(1, 11, 2):
    if (num % 2) == 0:
        print(f'{num}는 짝수입니다.')
    else:
        print(f'{num}는 홀수입니다.')
"""

# for문 내에서 사용하는 confinue, break
values = [1,3,5,7,9,11,13,15,17,19]

num = 0
for item in values:
    num += 1   #num = num+1 이랑 같음
    if (num % 2) == 0:
        #break  #반복문 탈출
        continue #if 조건만 패스 다음값 진행
    else:
        print(f'{num}번 수는 {item}입니다.')
