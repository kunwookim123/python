# 변수(Variable) - 데이터를 담는 상자
'''
변수란
게임 -> 플레이어의 점수를 기억
쇼핑몰 -> 상품의 가격을 저장
SNS -> 사용자의 이름을 기억

데이터를 저장하는 공간을 변수라고 합니다.
'''

'''
상자(변수)에 물건(데이터)를 넣습니다.
이름표(변수명)로 상자를 구분합니다.
필요할 때 상자에서 물건을 꺼내 사용합니다.
'''

# 변수선언
# 변수이름 = 값
age = 20
name = "김철수"
height = 175.5

# = -> 할당 연산자 (넣는다는 의미, 수학의 등호와는 다름)

# 변수의 값은 바꿀 수 있다.
# 재할당
age = 30
print(age)

# 스네이크 케이스(Snake_case)
student_name = "김철수"
user_age = 25
total_score = 100

x = 10
y = 20
# 값의 교환, 여러 변수 할당
x, y = y, x
# x, y = 20, 10 과 같음

X, Y = 30, "a"
# sep = 여러값 구분자, end = '줄바꿈 구분자'
print('X', X, sep='   ', end='   ')
print('Y', Y)
# 자료형
# 정수,실수


# 문자열 => "aaa", "hello"

print('"파이썬"은 가장 널리 사용되는 프로그래밍 언어 입니다.')
print("'파이썬'은 가장 널리 사용되는 프로그래밍 언어 입니다.")


true = True
false = False

print('true', type(true))
print('false', type(false))

a = "1"
b = '1'
# a1 = int(a)
# b1 = float(b)
# print('a1 type:', type(a1))
# print('b1 type:', type(b1), b1)

c = 2
d = 2.1
# 문자열 포매팅 : f-string
print(f'c의 숫자는 {c}, {d} 입니다')

# 실습1
title = 'Inception'
director = 'Christopher Nolan'
year = 2010
genre = 'Sci-fi'
print(f'Title: {title} Director: {director} Year: {year} Genre: {genre}')

# 실습2
name = '김건우'
age = '34'
mbti = 'ISFP'
print(f'안녕하세요. \n제 이름은 {name}이고, \n{age}살입니다. \n제 MBTI는 {mbti}에요')
print(f"""안녕하세요
제 이름은 {name}
{age}살이고
제 mbti는 {mbti}에요""")
