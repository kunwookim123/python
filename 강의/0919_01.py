# # def add(a,b):
# #     a += 1
# #     return a + b
# # print(a)

# new_list = [1,2,3]

# count = 10
# def count_print():
#     global count #전역 변수임을 표시
#     count = count + 1
#     print(count)
#     return count

# count_print()
# print(count)

# a = 10

# def count_print(b):
#     b += 1
#     print('def count:', b)
#     return b


# a = count_print(b=a)

# def outer():
#     a = 10
#     def inner():
#         nonlocal a
#         a += 5
#         print(f'[inner] a: {a}') # 15
#     inner()
#     print(f'[outer] a: {a}') # 15

# outer()

# 함수의 범위(scope)
'''
    변수의 범위란?
    변수가 살아있는(접근 가능한)영역을 범위(scope)라고 합니다.
    비유:
    집 = 전역범위
    방 = 지역범위
    방 안의 물건은 그 방에서만 사용 가능
    거실의 물건은 모든 방에서 사용 가능
'''


# # 전역 변수(global variable)
# global_var = '전역 변수'

# def my_fun():
#     # 지역 변수(local variable)
#     local_var = '지역 변수'

#     print(global_var) # 전역 변수 접근 가능
#     print(local_var) # 지역 변수 접근 가능

# my_fun()
# print(global_var) # 전역 변수 접근 가능
# # print(local_var) # 에러! 함수 밖에서 지역 변수 접근 불가


# # global 키워드
# # 함수 안에서 전역 변수를 수정하려면 global 키워드를 사용해야함

# count = 0 # 전역 변수

# # def increment_wrong():
# #     count = count + 1 # 에러! 지역 변수로 취급됨

# def increment_right():
#     global count
#     count = count + 1

# # increment_wrong()

# print('초기값:', count) # 0
# increment_right()
# increment_right()
# print('최종값:',count) # 2


# score = 0

# def add_score(points):
#     global score
#     score += points
#     print(f'점수 획득! 현재 점수:, {score}')

# def reset_score():
#     global score
#     score = 0
#     print('점수 초기화!')

# add_score(100)
# add_score(200)

# print(score)

# reset_score()

# print(score)

# # 전역 변수 사용 주의
# # 전역 변수는 편리하지만 과도하게 사용하면 코드가 복잡해짐

# # 안좋은 예
# total = 0
# count = 0

# def add_number(num):
#     global total, count
#     total += num
#     count += 1


# def get_average():
#     global total, count # 남용 예시
#     return total / count if count > 0 else 0


# # 좋은 예
# def calculate_average(numbers):
#     if not numbers:
#         return 0
#     return sum(numbers) / len(numbers)


# numbers = [53,56,34,64]
# avg = calculate_average(numbers = numbers)


# def num_append(numbers):
#     numbers.append(6)


# numbers = [1,2,3,4,5]

# print('함수 호출전,numbers:', numbers) # [1,2,3,4,5]
# num_append(numbers)
# print('함수 호출후,numbers:', numbers) # [1,2,3,4,5,6]

# # 복사본이 넘어감
# def increment_num(num_copy):
#     num_copy += 1

# # 원본이 넘어옴
# def num_append(numbers):
#     numbers.append(6)
#     numbers[0] += 1

# # 불변 타입
# # 정수, 실수, 문자열, 튜플
# num = 10
# print('함수 호출전,numbers:',numbers)
# # increment_num(num_copy,num)

# # 가변 타입
# # 리스트, 딕셔너리, set
# numbers = [1,2,3,4,5]

# print('함수 호출전,numbers:', numbers) # [1,2,3,4,5]
# num_append(numbers)
# print('함수 호출후,numbers:', numbers) # [1,2,3,4,5,6]

# info_dic = {'name': '김철수','age': 20}

# def change_info(info):
#     info['name'] = '이영희'
#     info['age'] = 25

# # 1. {'name': '김철수','age': 20}
# print('함수 호출전,info_dic:', info_dic)
# change_info(info_dic)
# # 2  {'name': '이영희','age': 25}
# print('함수 호출후,info_dic:', info_dic)


# 재귀 함수 (recursive function)
'''
    자기 자신을 호출하는 함수
'''

# 팩토리얼 계산
def factofial(n):
    if n <= 1:
        return 1
    
    return n * factofial(n-1)


# result = factofial(5)
# print(result)
# 5 * factorial(4) -> 1번 시행
# 5 * 4 * factorial(3) -> 2번 시행
# 5 * 4 * 3 * factorial(2) -> 3번 시행
# 5 * 4 * 3 * 2 * 1

# 피보나치 수열
# 0 1 1 2 3 5 8 13 21 34 ...

def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(2))
fibonacci(1) + fibonacci(0)
1 + 0
1

for i in range(10):
    print(fibonacci(i))
print()

# 람다 함수(lambda function)
'''
    람다 함수는 이름 없는 한 줄까지 간단한 함수
'''
# 일반 함수

def square(x):
    return x ** 2

# 람다 함수
square_lambda = lambda x: x ** 2


print('square(5):', square(5))
print('square_lambda(5):', square_lambda(5))

# 여러 매개변수
add = lambda x, y: x + y
print(add(5,3))

# map(): 모든 요소에 함수 적용
numbers = [1,2,3,4,5]

squared = list(map(lambda x: x ** 2, numbers))
# [1,4,9,16,25]

def increment_fun(x):
    return x + 1


incre_numbers = list(map(increment_fun, numbers))
print(incre_numbers)

# filter

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# sorted() 정렬 기준 지정

student = [
    {'name': '홍길동', 'score': 80},
    {'name': '김철수', 'score': 92},
    {'name': '이영희', 'score': 70},
]

student.sort(key = lambda x: x['score'], reverse = True)
for student in student:
    print(f'{student ['name']}: {student['score']}점')