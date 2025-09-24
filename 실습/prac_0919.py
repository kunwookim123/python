# # 실습3
# # 로그인/로그아웃 전역 상태 관리
# current_user = '' # 로그아웃 상태

# def login(name):
#     global current_user
#     if current_user == '':
#         current_user = name
#         print(f'{name}님 로그인 성공')
#     else:
#         print('이미 로그인되어 있습니다.')

# def logout():
#     global current_user
#     current_user = ''
#     print('로그아웃되었습니다.')

# login('Ian')
# login('Ian')
# logout()
# login('codingowl')
# print(current_user)

# # 실습4
# # 거듭제곱
# def square(a,b):
#     if b == 0:
#         return 1

#     return a * square(a,b-1)

# print(square(2,5))
# print(square(3,2))

# 문제1. 1부터 n까지의 합(재귀함수를 이용해서)
def sum_to_n(n):
    if n <= 1:
        return 1
    return n + sum_to_n(n-1)


print(sum_to_n(5))

# sum(range(1,n+1))

# 문제2. 문자열 뒤집기 (재귀함수를 이용해서)


def reverse_string(s):
    if len(s) == 1:
        return ''
    return s(-1) + reverse_string(s[:-1])


print('hello')
# [::-1]
