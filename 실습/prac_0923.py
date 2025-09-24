# 실습1
# 문제1
# class UserAccount:
#     def __init__(self, username, password):
#         self.username = username # public
#         self.__password = password # private

#     def change_password(self, old_pw, new_pw):
#         if self.__password == old_pw:
#             self.__password = new_pw
#             print('비밀번호가 변경되었습니다.', self.__password)
#         else:
#             print('비밀번호 불일치')

#     def check_password(self, password):
#         return self.__password == password # 비밀번호 일치 여부 반환
    
# user1 = UserAccount('김철수', 'python')
# print('비밀번호 일치 여부:', user1.check_password('python1'))
# print('비밀번호 일치 여부:', user1.check_password('python'))

# user1.change_password('python3', 'python3')
# user1.change_password('python', 'python3')

# 문제2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.__score = 0

#     @property
#     def score(self):
#         return self.__score
    
#     @score.setter
#     def score(self, value):
#         if 0 <= value <= 100:
#             self.__score = value
#         else:
#             raise ValueError('범위를 넘었습니다.')
        
# s = Student('홍길동')
# s.score = 90
# print(f'{s.name}님의 점수: {s.score}점')
# s.score = 110
# print(s.score)



# # 프로그래머스
# # 컨트롤 제트 문제
# def solution(s):
#     # 스택 생성
#     stack = []
#     # 리스트로 만듦
#     s_list = s.split()

#     for word in s_list:
#         if word == 'Z':
#             if stack:
#                 stack.pop() # 마지막 요소 제거
#         else:
#             stack.append(int(word))
#     return sum(stack)

# print(solution('1 2 Z 3'))
# print(solution('Z -1 -2 -3 Z'))

# 실습4
# 문제1 Shape 클래스 오버라이딩
# class Shape:
#     def __init__(self, sides, base):
#         self.sides = sides
#         self.base = base

#     def printinfo(self):
#         print(f'변의 개수: {self.sides}')
#         print(f'밑변의 길이: {self.base}')

#     def area(self):
#         print(f'넓이 계산이 정의되지 않았습니다.')

# class Rectangle(Shape):
#     def __init__(self, sides, base, height):
#         super().__init__(sides, base)
#         self.height = height
    
#     def area(self):
#         print(f'사각형의 넓이: {self.base * self.height}')
    
# class Triangle(Shape):
#     def __init__(self,sides, base, height):
#         super().__init__(sides, base)
#         self.height = height

#     def area(self):
#         print(f'삼각형의 넓이: {self.base * self.height / 2}')

# shapes = [Rectangle(4,5,10), Triangle(3,4,9)]
# for shape in shapes:
#     shape.printinfo()
#     shape.area()

# # 실습5
# # 문제. 추상 클래스 Payment 구현

# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass

# class CardPayment(Payment):
#     def __init__(self, amount):
#         super().__init__()
#         self.amount = amount
    
#     def pay(self):
#         print(f'카드로 {self.amount}원을 결제합니다.')
    

# class CashPayment(Payment):
#     def __init__(self, amount):
#         super().__init__()
#         self.amount = amount
#     def pay(self):
#         print(f'현금으로 {self.amount}원을 결제합니다.')

# card = CardPayment(100000)
# cash = CashPayment(4000)

# card.pay()
# cash.pay()

# 실습1
# 계산기 모듈 만들기

# import calc

# result1 = calc.add(10,6)
# result2 = calc.subtract(5,3)
# result3 = calc.multiply(20,7)
# result4 = calc.divide(10,5)
# result5 = calc.divide(10,0)

# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)

# 실습2
# 문제1. 실제 거리 계산: 좌표 두 점 사이 거리 구하기
import math

x1, y1 = input('(x1, y1) 좌표를 입력하세요.').split(',')
x2, y2 = input('(x2, y2) 좌표를 입력하세요.').split(',')

distance = math.sqrt(math.pow(math.fabs(int(x2)-int(x1)),2) + math.pow(math.fabs(int(y2)-int(y1)),2))
print('두 점 사이의 거리:', round(distance, 2))

# 문제2. 상품 나누기: 최소 공배수와 최대 공약수
import math

student = 18
teacher = 24
gcd = math.gcd(student, teacher)
lcm = math.lcm(student, teacher)
print('최대 간식 개수:', gcd)
print('최소 간식 개수:', lcm)

# 실습3
import random

numbers = range(1,46)
lotto = random.sample(numbers,6)
sorted_lotto = sorted(lotto)
print('당첨번호:', sorted_lotto)

# 실습4
import random

user = input('가위,바위,보 중 하나를 입력하세요.')
srp = ['가위','바위','보']
c_srp = random.choice(srp)
print(f'사용자: {user} 컴퓨터: {c_srp}')

if user == c_srp:
    print('무')
elif (user == '가위' and c_srp == '바위') or (user == '바위' and c_srp == '보') or (user == '보' and c_srp == '가위'):
    print('사용자 패')
else:
    print('사용자 승')

# 실습5
import datetime

birthday = input('생일을 입력하세요').split('-')
birth_month, birth_day = map(int, birthday)

today = datetime.date.today()

current_year_birthday = datetime.date(today.year, birth_month, birth_day)

if current_year_birthday >= today:
    left_day = (current_year_birthday - today).days
else:
    next_year_birthday = datetime.date(today.year + 1, birth_month, birth_day)
    left_day = (next_year_birthday - today).days

print(f'남은 날짜: {left_day}일')

# 실습6
import time
import random

word = ['sky','moon','sun','one','two','three','four','five','six','seven']
print('[타자 게임] 준비되면 엔터!')
input()
start = time.time()
num = 1
question = random.choice(word)
while num <= 10:
    print('문제',num)
    print(question)
    user_input = input()
    if question == user_input:
        print('통과!!')
        num += 1
        question = random.choice(word)
    else:
        print('오타! 다시 도전!')

end = time.time()
print('타자 시간: ' + str(end - start) + '초')

# sys
import sys

x = input('수 입력: ')
n = int(x)

if n == 0:
    print('0으로 나눌 수 없습니다.')
    sys.exit(0)

result = 10 / n

print(result)

# os
import os

# 1.현재 작업 디렉터리 확인
print('현재 작업 디렉터리:', os.getcwd())

# 2. 새 폴더 생성 (이미 있으면 예외 발생 가능)
folder_name = 'sample_folder'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f'{folder_name} 폴더를 생성했습니다.')
else:
    print(f'{folder_name} 폴더가 이미 존재합니다.')

# 3. 현재 디렉터리 내 파일/폴더 목록 출력
print('현재 디렉터리 내 파일 및 폴더 목록:')
print(os.listdir())