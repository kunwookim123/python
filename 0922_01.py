# # 클래스
# """
#     클래스는 객체를 만들기 위한 설계도
#     클래스 = 붕어빵 틀
#     객체(인스턴스) = 실제로 만들어진 붕어빵

#     클래스를 사용하면 관련된 데이터와 기능을 하나로 묶어서 관리
# """

# """
#     코드 재사용성: 한 번 작성한 코드를 여러 곳에서 활용
#     유지보수 용이: 수정사항이 있을 때 클래스만 수정하면 됨
#     코드 구조화: 복잡한 프로그램을 체계적으로 구성
#     현실 세계 모델링: 실제 사물이나 개념을 프로그램으로 표현
# """

# class 클래스_이름:
#     def __init__(self):
#         pass

#     def 메서드이름(self):
#         # 메서드 코드
#         pass

# class Car:
#     def __init__(self, brand, model, color):
#         self.brand = brand # 브랜드
#         self.model = model # 모델명
#         self.color = color # 색상
#         self.speed = 0 # 현재 속도

#     def accelerate(self, increase):
#         '''속도를 증가시키는 메서드'''
#         # 최대 속도가 150km/h라면
#         self.speed += min(150,self.speed + increase)
#         print(f'속도가 {increase}km/h 증가 했습니다. 현재 속도: {self.speed}km/h')

#     def brake(self,decrease):
#         '''속도를 증가시키는 메서드'''
#         self.speed += max(0, self.speed - decrease) # 속도는 0 미만이 될 수 없게 설정
#         print(f'속도가 {decrease}km/h 증가 했습니다. 현재 속도: {self.speed}km/h')
  
#     def info(self):
#         '''차량 정보를 출력하는 메서드'''
#         print(f'브랜드: {self.brand}')
#         print(f'모델명: {self.model}')
#         print(f'색상: {self.color}')
#         print(f'현재 속도: {self.speed}km/h')

# # 객체 생성 및 불러오기
# my_car = Car('tesla','model 3','빨간색')
# # my_car 객체(인스턴스)의 정보 출력
# my_car.info()
# print()
# my_car.accelerate(80)
# print()
# my_car.brake(30)

    

# self = 클래스 자기 자신
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f'안녕하세요. 저는 {self.name}, {self.age}살입니다.')

# introduce = Person('김철수', 25)
# print(introduce())

# class Student:
#     def __init__(self, name, age, sturdent_id):
#         '''생성자:학생 객체를 초기화'''
#         self.name = name
#         self.age = age
#         self.studengt_id = sturdent_id
#         self.grades = [] # 성적 리스트 초기화
#         print(f'학생 {name}의 정보가 등록 되었습니다.')

#     def add_grade(self, grade):
#         self.grades.append(grade)
#         print(f'{self.name}의 성적 {grade}점이 추가 되었습니다.')

#     def get_averate(self):
#         '''평균 성적 계산'''
#         if self.grades:
#             return sum(self.grades) / len(self.grades)
#         return 0
#     def __del__(self):
#         '''소멸자'''
#         '''객체가 메모리에서 삭제될 때 호출되는 메서드'''
#         print(f'{self.name}의 정보가 삭제되었습니다.')
# # 객체 인스턴스 생성
# student1 = Student('김철수','20','20250001')
# print()
# student1.add_grade(70)
# print()
# student1.add_grade(60)
# print()
# student2 = Student('이영희','22','20230001')
# print()
# print('평균 점수:', student1.get_averate())
# print()
# del student2

# 인스턴스 변수, 클래스 변수
'''
    인스턴스 변수: 각 객체마다 독립적으로 가지는 변수
    클래스 변수: 모든 객체가 공유하는 변수
'''

# class BankAccount:
#     # 클래스 변수
#     bank_name = '파이썬 은행'
#     total_accounts = 0
#     interest_rate = 0.02 # 이자율

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#         self.account_number = BankAccount.total_accounts + 1
        
#         # 클래스 변수 업데이트
#         BankAccount.total_accounts += 1
#     def deposit(self, amount):
#         '''입금 메서드'''
#         if amount > 0:
#             self.balance += amount
#             print(f'{amount}원이 입금 되었습니다. 잔액 : {self.balance}원')
#         else:
#             print('입금액은 0보다 커야합니다.')

#     def withdraw(self, amount):
#         '''출금 메서드'''
#         if self.balance > amount:
#             self.balance -= amount
#             print(f'{amount}원이 출금되었습니다. 잔액 : {self.balance}원')
#         else:
#             print('잔액이 부족합니다.')

#     def apply_interest(self):
#         '''이자 적용'''
#         interest = self.balance * BankAccount.interest_rate
#         self.balance += interest
#         print(f'이자{ interest}원이 적용되었습니다. 잔액 : {self.balance}원')

#     @classmethod
#     def change_interest_rate(cls, new_rate):
#         '''클래스 메서드: 이자율 변경'''
#         cls.interest_rate = new_rate
#         print(f'이자율 {new_rate * 100}%로 변경되었습니다.')

#     def __del__(self):
#         BankAccount.total_accounts -= 1
#         print(f'{self.owner}님 계좌를 삭제했습니다.')
#         print(f'남은 계좌 수: {BankAccount.total_accounts}')


# # 객체 생성
# account1 = BankAccount('홍길동', 10000)
# account2 = BankAccount('김철수', 15000)

# print(f'은행 이름: {BankAccount.bank_name}')
# print(f'총 계좌 수: {BankAccount.total_accounts}')

# account1.deposit(50000) # 입금
# account2.apply_interest() # 이자 적용

# BankAccount.change_interest_rate(0.03) # 이자 변경
# print()
# account1.apply_interest() # 이자 적용

# del account1

# class Calculator:
#     # 클래스 변수
#     calculation_count = 0

#     def __init__(self, name):
#         self.name = name
#         self.history = []

#     # 인스턴스 메서드
#     def add_to_history(self, operation, result):
#         '''계산 기록 저장'''
#         self.history.append(f'{operation} = {result}')
#         Calculator.calculation_count += 1
#     # 클래스 메서드
#     @classmethod
#     def get_total_calculations(cls):
#         '''전체 계산 횟수 반환'''
#         return cls.calculation_count
    
#     @classmethod
#     def add(a,b):
#         '''두 수의 합'''
#         return a + b
#     @staticmethod
#     def multiply(a,b):
#         '''두 수의 곱'''
#         return a * b
#     @staticmethod
#     def is_even(number):
#         '''짝수 판별'''
#         return number % 2 == 0
    
#     def calculate_and_save(self, a, b, operation):
#         '''계산 하고 기록 저장'''
#         if operation == 'add':
#             result = self.add(a, b)
#             self.add_to_history(f'{a} + {b}', result)
#         if operation == 'multiply':
#             result = self.multiply(a, b)
#             self.add_to_history(f'{a} x {b}', result)  
#         return result
    
# # 객체 생성
# calc1 = Calculator('계산기1')
# calc2 = Calculator('계산기2')

# # 정적 메서드 사용 (인스턴스 없이도 호출 가능)
# print(Calculator.add(5, 3))
# print(Calculator.is_even(5))

# # 인스턴스 메서드
# result = calc1.calculate_and_save(10,20,'add')
# print(f'결과 : {result}')
# result = calc2.calculate_and_save(10,20,'multiply')
# print()

# # 클래스 메서드 사용
# print(f'총 계산 횟수: {Calculator.get_total_calculations()}')

# 접근 제어자
'''
    객체 지향 프로그래밍에서 클래스의 멤버(속성,메서드)에
    대한 접근 권한을 제어하는 매커니즘
'''

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand # public 속성
#         self.model = model # public 속성
#         self.speed = 0 # public 속성

#     def accelerate(self, amount): # public 메서드
#         '''외부에서 자유롭게 호출 가능'''
#         self.speed += amount
#         return f'속도가 {self.speed}km/h가 되었습니다.'
    
#     def get_info(self):
#         return f'{self.brand} {self.model}'
    
# print()
# # 객체 생성
# car = Car('tesla','model 3')
# print(car.model) # 정상 접근
# print(car.brand) # 정상 접근
# print(car.get_info()) # 정상 호출
# car.speed = 200 # 직접 수정 가능

# Private 속성/메서드(언더바 2개)
# class SecuritySysyem:
#     def __init__(self, password): 
#         self.__password = password # private 속성
#         self.__security_level = 'HIGH' # private 속성
#         self.__failed_attempts = 0 # private 속성

#     def __encrypt_password(self, pwd): # private 메서드
#         '''내부적으로만 사용되는 메서드'''
#         return pwd[::1] + 'encrypted'
    
#     def __check_security(self): # private 메서드
#         '''내부 보안 체크'''
#         return self.__failed_attempts < 3
    
#     def authenticate(self, password): # public 메서드
#         if not self.__check_security():
#             return '계정이 잠겼습니다.'
        
#         # 인자로 받은 password를 암호화
#         encrypted = self.__encrypt_password(password) # private 메서드 호출
#         # 이미 설정한 password를 암호화 하고 비교
#         if encrypted == self.__encrypt_password(self.__password):
#             self.__failed_attempts = 0
#             return '인증 성공'
#         else:
#             self.__failed_attempts += 1
#             return f'인증 실패 {self.__failed_attempts}/3'
        
# security = SecuritySysyem('secret123')
# # print(security.__password)
# # security.__check_security()

# print(security.authenticate('wrong')) # 인증 실패 (1/3)
# print(security.authenticate('secret123'))

# # 절대 권장하지 않음
# # print(security._SecuritySystem__password)

# # property를 사용하지 않는 경우

# class Circle1:
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self): # 메서드로 접근
#         return 3.14 * self.radius ** 2

# # property를 사용하는 경우

# class Circle2:
#     def __init__(self, radius):
#         self.__radius = radius

#     @property
#     def area(self): # 메서드로 접근
#         return 3.14 * self.__radius ** 2
    
#     @property
#     def radius(self):
#         return self.__radius
    
#     @radius.setter
#     def radius(self,radius):
#         self.__radius = radius
    
#     def set_radius(self, radius):
#         self.__radius = radius


# c1 = Circle1(5)
# print('c1',c1.get_area()) # 메서드 호출 : 괄호 필요
# print()
# c2 = Circle2(4)
# print('c2',c2.area) # 속성 접근 : 괄호 없음
# c2 = Circle2(10)
# print('c2',c2.area) # 속성 접근 : 괄호 없음

class Vector:
    def __init__(self,x,y):
        '''생성자 : 속성 초기화'''
        self.x = x
        self.y = y

    def __str__(self):
        '''print() 함수 호출 시'''
        return f'Vector {self.x} {self.y}'
    
    def __repr__(self):
        '''개발자를 위한 문자열 표현'''
        return f'Vector (x = {self.x} y = {self.y})'
    
    # 연산자 오버로딩
    def __add__(self, other):
        '''+ 연산 오버로딩'''
        return Vector(self.x + other.x, self.y + other.y)
    '''__sub__,__mul__,__eq__'''

    def __len__(self):
        '''len() 함수 호출 시 '''
        return int(self.x ** 2 + self.y ** 2) ** 0.5

v1 = Vector(3,4)
v2 = Vector(1,2)
print(v1)
print(repr(v1))

v3 = v1 + v2
print(v3)
