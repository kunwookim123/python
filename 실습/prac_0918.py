# # 실습3
# # 문제1. 로그인 시스템 구현
saved_id = 'admin'
saved_pw = 'admin123'

input_id = ''
input_pw = ''

while True:
    input_id = input('ID를 입력하세요.')

    if saved_id == input_id:
        while True:
            input_pw = input('PW를 입력하세요.')
            if saved_pw == input_pw:
                print('로그인 성공!')
                break #pw while문 탈출
            else:
                print('비밀번호가 틀렸습니다.')
        break #id while문 탈출
    else:
        print('ID가 존재하지 않습니다.')

# 실습1
# 문제1. 사칙연산 계산기 함수 만들기
def calculate(a,b,operator):
    result = ''

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = float(a / b)
    else:
        print('지원하지 않는 연산입니다.')

    return result
    
print(calculate(3,6,'+'))
print(calculate(3,6,'-'))
print(calculate(3,6,'*'))
print(calculate(3,6,'/'))
print(calculate(3,6,'='))

# 실습2
# 문제1. 숫자 여러개의 평균 구하기
def average(*num):
    sum_num = sum(num)
    avg_num = sum_num / len(num)
    return avg_num

result = average(1,3,4,5,6)
print(result)

# 문제2. 가장 긴 문자열 찾기(max 함수에 대해 찾아보고 풀기)
def max_len_word(*args):
    return max(args, key = len)

print(max_len_word('hello','banana','apple'))

# 문제3. 사용자 정보 출력 함수
def user_info(**info):
    for key, value in info.items():
        print(f'{key}: {value}')
       

user_info(name = '김철수', age = 22, email = 'cs11@gmail.com')
user_info(name = '김철수', age = 22, email = 'cs11@gmail.com', city = '서울')

# 문제4. 할인 계산기
def product(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value*0.9}')

product(radio = 20000, television = 1000000)
product(radio = 20000, television = 1000000, computer = 2500000)