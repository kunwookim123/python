# 배열 모양 변경, 조작

import numpy as np

arr_1d = np.array([1,2,3,4,5,6])
print('==========1차원==========')
print('shape',arr_1d.shape) # 모양
print('ndim',arr_1d.ndim) # 차원
print('size',arr_1d.size) # 사이즈
print(arr_1d.reshape(3,-1)) # '-'는 자동으로 채워진다

arr_2d = np.array([[1,2,3], [4,5,6]])
print('==========2차원==========')
print('shape',arr_2d.shape) # 모양
print('ndim',arr_2d.ndim) # 차원
print('size',arr_2d.size) # 사이즈

# 기본 산술 연산
a = np.array([1,2,3,4,5])
b = np.array([5,4,3,2,1])

print('배열 a:', a)
print('배열 b:', b)

print('덧셈 (a + b):', a + b)
print('뺄셈 (a - b):', a - b)
print('곱셈 (a * b):', a * b)
print('거듭제곱 (a ** b):', a ** b)
print('나눗셈 (a / b):', a / b)
print('몫 (a // b):', a // b)
print('나머지 (a % b):', a % b)

# 스칼라와의 연산
a = np.array([1,2,3,4,5])
scalar = 10

print('+ 스칼라:', a + scalar)
print('- 스칼라:', a - scalar)
print('* 스칼라:', a * scalar)
print('/ 스칼라:', a / scalar)
print('스칼라 / 배열:', scalar / a)

A = np.array([
    [1,2,3],
    [4,5,6]
])
B = np.array([
    [7,8,9],
    [10,11,12]
])

print('행렬 A\n', A)
print('행렬 B\n', B)

print('행렬 A + B\n', A + B)
print('행렬 A * B\n', A * B)
print('행렬 A / B\n', A / B)

A = np.array([
    [1,2,],
    [3,4]
])
B = np.array([
    [7,8],
    [9,10]
])

print('행렬의 곱셈\n',A @ B)

# 브로드 캐스팅
# 서로 다른 모양의 배열 간 연산을 가능하게 하는 numpy 기능
arr = np.array([1,2,3,4,5])
scalar = 10

# 스칼라가 자동으로 배열 크기로 브로드 캐스트 됨
# [1,2,3,4,5] + [10,10,10,10,10] 가 됨

matrix = np.array([
    [1,2,3,],
    [4,5,6,],
    [7,8,9]
])
vector = np.array([10,20,30])

print(matrix + vector)

# 브로드 캐스팅 규칙
# 규칙1 : 차원 수가 다르면 작은 쪽의 팡에 1을 추가
# (3,3) + (3, ) -> (1,3)
a = np.array([1,2,3]) # (3, ) 1차원
b = np.array([[4],[5],[6]]) # (3,1) 2차원

a + b # (3, ) + (3, 1) -> (1, 3) + (3, 1) = (3, 3)
print(a + b)

# 규칙2 : 각 차원에서 크기가 1이거나 같아야 함
# 호환 가능: (3,1) & (1,4) = (3,4)
# 호환 불가: (3,2) & (4,2) = 에러 발생

a = np.ones((3,2))
b = np.ones((1,2))

print(a + b)

arr = np.array([1,2,3,4,5,6,7,8,9])
# np.sum(arr) # 합
# np.mean(arr) # 평균
# np.median(arr) # 중간값
# np.std() # 표준편차
# np.max() # 최대값
# np.min() # 최솟값
# np.var() # 분산
# np.ptp() # max - min
print('누적 합:', np.cumsum(arr))
print('누적 곱:', np.cumprod(arr))

matrix = np.array([
    [1,2,3,],
    [4,5,6,],
    [7,8,9]
])

print('행별 합 (axis=1)', np.sum(matrix, axis=1))
print('열별 합 (axis=0)', np.sum(matrix, axis=0))

print('행별 평균 (axis=1)', np.mean(matrix, axis=1))
print('열별 평균 (axis=0)', np.mean(matrix, axis=0))

print('행별 누적 합 (axis=1)', np.cumsum(matrix, axis=1))
print('열별 누적 합 (axis=0)', np.cumsum(matrix, axis=0))