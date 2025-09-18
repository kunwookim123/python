# 실습3
# 구구단
for i in range(2, 10):
    print(f'[ {i} 단 ]')
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
    print()


# 중첩 for문 별찍기
n = int(input('몇 줄 ? >'))

print('[왼쪽 정렬]')
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()


print('[가운데 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end='')
    # (i - 1) * 2 + 1 = 2i - 1
    for k in range(2 * i - 1):
        print('*', end='')
    print()

print('[오른쪽 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end='')
    for k in range(i):
        print('*', end='')
    print()

# 실습4
# 문제1
squares = [x ** 2 for x in range(1,11)]
print('각 수 제곱값:', squares)

# 문제2
three = [x for x in range(3,51,3)]
print('3의 배수:', three)

# 문제3
fruits = ['apple', 'fig', 'banana', 'plum', 'cherry', 'pear', 'orange']

new_fruits = [word for word in fruits if len(word) >= 5]
print('글자 수 5 이상인 단어:', new_fruits)

# 실습1
# 문제1. 비밀 코드 맞추기(1)
secret_code = 'codingonre3'
code = input('비밀 코드를 입력하세요.')

while code != secret_code:
    print('비밀 코드가 틀렸습니다. 다시 시도하세요.')
    code = input('비밀 코드를 입력하세요.')
print('입장이 허용되었습니다.')

# 문제2. 업다운 게임
import random

random_value = random.randrange(1,101)

count = 0
n = 0

while random_value != n:
    n = int(input('1부터 100 사이 숫자를 입력해주세요.'))
    count += 1

    if n < random_value:
        print('입력한 숫자보다는 커요.')
    else:
        print('입력한 숫자보다는 작아요.')

print(f'{count}번 만에 정답을 맞췄습니다.')

# 실습2
# 문제1 비밀 코드 맞추기(2)
secret_code = 'codingonre3'

while True:
    code = input('비밀 코드를 입력하세요.')
    if secret_code == code:
        print('입장 완료! 환영합니다.')
        break
    else:
        print('비밀 코드가 틀렸습니다. 다시 시도하세요.')

# 문제2. 유효한 나이만 평균 내기
times = 0
sum_age = 0

while times < 5:
    age = int(input('나이를 입력해주세요.'))

    if 0 < age <= 120:
        sum_age += age
        times += 1
print(f'총 나이의 합계는 {sum_age}, 평균은 {sum_age/5:.0f}입니다.')

