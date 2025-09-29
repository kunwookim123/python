# 실습1
# 문제1.0으로 채워진 크기 (3,4) 배열을 생성한 후, 모든 값을 5로 채우는 새로운 배열 만들기
import numpy as np

matrix = np.array([
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6]
])

zeros_like = np.zeros_like(matrix)
print('zeros_like:\n', zeros_like)

full_array = np.full((3,4),5)
print('5로 채워진 배열\n', full_array)

# 문제2, 0부터 20까지 2씩 증가하는 1차원 배열 생성하기
arr = np.arange(0, 21, 2)
print('0 ~ 20까지 2씩 증가:', arr)

# 문제3. 0~1 사이의 실수 난수를 가지는 (2,3) 크기 배열 생성하기
random_uniform = np.random.rand(2,3)
print('0~1사이 난수:\n', random_uniform)

# 문제4. 평균이 100, 표준편차가 20인 정규분포 난수 6개 생성하기
# normal(평균,표준편차,사이즈)
arr4 = np.random.normal(100,20,6)
print('표준정규분포:\n', arr4)

# 문제5. 1~20까지의 정수를 포함하는 1차원 배열을 만들고, 이 배열을 (4,5)크기의 2차원 배열로 변환하기
# 모양 변환 - reshape() 사용
arr5 = np.arange(1,21).reshape(4,5)
print('arr5\n', arr5)


# 문제6. 0~1까지 균등 간격으로 나눈 12개의 값을 가지는 배열을 생성하고, 이를 (3,4) 크기로 변환하기
random_uniform = np.linspace(0, 1, 12).reshape(3,4)
print('0과 1 사이 균일 분포:\n', random_uniform)

# 문제7. 0~99 사이의 난수로 이루어진 (10,10) 배열로 생성한 뒤, np.eye()로 만든 단위 행렬을 더하여 대각선 요소가 1씩 증가된 배열 만들기
arr7 = np.random.randint(0, 100, (10,10))
print('arr7\n', arr7)
arr7 = arr7 + np.eye(10)
print('arr7\n', arr7)

# 문제8
arr8 = np.random.randint(0, 10, (2, 3, 4))
print('arr8\n', arr8)