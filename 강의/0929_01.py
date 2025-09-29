# Numpy(numerical python)는 파이썬에서 과학계산을 위한 핵심 라이브러리
# 데이터 과학, 머신러닝, 과학 연구 분야에서 가장 중요한 도구중 하나

# 파이썬은 인터프리터 언어로 실행 속도가 느림
# 속도 문제 해결
# Numpy는 C언어로 구현되어 있어 대용량 데이터 연산을 매우 빠르게 처리

# 메모리 효율성
# 파이썬 리스트: 각 요소가 객체로 저장되어 메모리 오버헤드가 큼
# Numpy 배열: 연속된 메모리 공간에 같은 타입의 데이터를 저장

# 벡터화 연산
# 반복문 없이 전체 배열에 대한 연산을 한번에 수행


import numpy as np

print('Numpy 버전:', np.__version__)
print('Numpy 설치 경로:', np.__file__)

# ndarray(N-dimensional array) Numpy의 핵심 자료구조
# 같은 타입의 요소들을 담는 다차원 컨테이너

arr = np.array([1,2,3,4,5])

print('1. 객체타입:', type(arr))    # 1. 객체타입: <class 'numpy.ndarray'>
print('2. 데이터 타입:', arr.dtype) # 2. 데이터 타입: int64
print('3. 배열 모양:', arr.shape)   # 3. 배열 모양: (5,)
print('4. 차원 수:', arr.ndim)      # 4. 차원 수: 1
print('5. 전체 요소 수:', arr.size) # 5. 전체 요소 수: 5

python_list = [1,2.5,'3.',True]
numpy_array = np.array([1,2.5,'3.',True])
print('파이썬 리스트:', python_list)
print('Numpy 배열:', numpy_array)

list1 = [1,2,3]
list2 = [4,5,6]

print('리스트 더하기:', list1 + list2)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print('Numpy 배열 더하기:', arr1 + arr2)


# 정수 배열
int_array = np.array([1,2,3,4,5])
print('정수 배열:', int_array)
print('데이터 타입:', int_array.dtype)

# 실수 배열
float_array = np.array([1.1,2.2,3.3,4.4,5.5])
print('실수 배열:', float_array)
print('데이터 타입:', float_array.dtype)

# 타입을 명시적으로 지정 배열
specified_array = np.array([1,2,3,4,5], dtype = np.float32)
print('명시적 배열:', specified_array)
print('데이터 타입:', specified_array.dtype)

# 타입을 명시적으로 지정 배열
specified_array = np.array([1,2,3,4,5], dtype = np.float32)
print('명시적 배열:', specified_array)
print('데이터 타입:', specified_array.dtype)

# 문자열 배열
string_array = np.array(['apple','banana','cherry'])
print('문자열 배열:', string_array)         # 문자열 배열: ['apple' 'banana' 'cherry']
print('데이터 타입:', string_array.dtype)   # 데이터 타입: <U6 <- 유니코드 문자열, 최대 10자

# 2차원 배열(3x3 행렬)
matrix = np.array([
    [1,2,3],
    [2,3,4],
    [3,4,5]
])

print('2차원 배열:', matrix)
print('모양:', matrix.shape) # 모양 : (3,3)
print('차원:', matrix.ndim) # 차원 : 2
print('크기:', matrix.size) # 크기 : 9

# for i in range(3):
#     for j in range(3):
#         print()


rows = []
for i in range(3):
    row = [i * 3 + j for j in range(4)] # [0,1,2,3]
    rows.append(row)

matrix2 = np.array(rows)
print('동적 생성 행렬:', matrix2)

# 3차원 배열 (2x3x4)
# 2개의 3 x 4 행렬로 구성
tensor = np.array([
    [
        [1,2,3,4],
        [11,21,31,41],
        [12,22,32,42],        
    ],
    [
        [1,2,3,4],
        [11,21,31,41],
        [12,22,32,42], 
    ]
])

print('3차원 배열 모양:', tensor.shape)
print('3차원 배열 모양:', tensor.ndim)

# numpy 내장 함수로 배열 생성
# 연속된 숫자 배열
# 0부터 9까지
arr1 = np.arange(10)
print('0부터 9까지:', arr1) # 0부터 9까지: [0 1 2 3 4 5 6 7 8 9]

arr2 = np.arange(11)
print('0부터 10까지:', arr1) # 0부터 10까지: [ 0  1  2  3  4  5  6  7  8  9 10]

arr3 = np.arange(1, 21, 2)
print('1부터 20까지 홀수만:', arr3) # 1부터 20까지 홀수만: [ 1  3  5  7  9 11 13 15 17 19]

arr4 = np.arange(1, 11, 0.5)
print('1부터 11까지:', arr4) # 1부터 11까지: [ 1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6.   6.5  7.   7.5
                            #   8.   8.5  9.   9.5 10.  10.5]
                            # range는 정수만 가능 .5 안됨
# 균등 간격 배열 Linspace
# 시작, 끝 사이를 균등하게 나눈 숫자들
arr1 = np.linspace(0, 10, 5) # 끝자리 포함
print('0부터 10까지 5개 요소:', arr1) # 0부터 10까지 5개 요소: [ 0.   2.5  5.   7.5 10. ]

arr2 = np.linspace(0, 10, 5, endpoint=False)
print('끝값 제외:', arr2) # 끝값 제외: [0. 2. 4. 6. 8.]

# 로그 간격 배열 Logspace
# Logspace(start, end, num)

# zeros: 0으로 채운 배열
zeros_1d = np.zeros(5)
print('1차원 zeros:', zeros_1d) # 1차원 zeros: [0. 0. 0. 0. 0.]

zeros_2d = np.zeros((3,4))
print('2차원 zeros:', zeros_2d) # 2차원 zeros: [[0. 0. 0. 0.]
                                            #  [0. 0. 0. 0.]
                                            #  [0. 0. 0. 0.]]

zeros_2d_int = np.zeros((3,4), dtype=int)
print('2차원 zeros:', zeros_2d_int) # 2차원 zeros: [[0 0 0 0]
                                                #  [0 0 0 0]
                                                #  [0 0 0 0]]

matrix = np.array([
    [1,2,3],
    [2,3,4],
    [3,4,5]
])
# 기존 배열과 같은 모양의 영 배열
zeros_like = np.zeros_like(matrix)
print('zeros_like:', zeros_like) # zeros_like: [[0 0 0]
                                            #  [0 0 0]
                                            #  [0 0 0]]
# 1차원 일 배열
ones_1d = np.ones(5)
print('1차원 ones:', ones_1d) # 1차원 ones: [1. 1. 1. 1. 1.]

# 2차원 일 배열(3,4)
ones_2d = np.ones((3,4))
print('2차원 ones:', ones_2d) # 2차원 ones: [[1. 1. 1. 1.]
                                        #  [1. 1. 1. 1.]
                                        #  [1. 1. 1. 1.]]

# 2차원 일 배열(3,4) bool 타입
ones_2d_bool = np.ones((3,4), dtype=bool)
print('2차원 ones:', ones_2d_bool) # 2차원 ones: [[ True  True  True  True]
                                              #  [ True  True  True  True]
                                              #  [ True  True  True  True]]

# full 특정 값으로 채운 배열
full_array = np.full((3,4),7)
print('2차원 배열:', full_array) # 2차원 배열: [[7 7 7 7]
                                           #  [7 7 7 7]
                                           #  [7 7 7 7]

matrix = np.array([
    [1,2,3],
    [2,3,4],
    [3,4,5]
])
full_like = np.full_like(matrix, 999)
print('2차원 배열:', full_like) # 2차원 배열: [[999 999 999]
                                        #    [999 999 999]
                                        #    [999 999 999]]

# 메모리만 할당함, 값은 쓰레기값
empty_array = np.empty((2,3))
print('2차원 배열(주의: 쓰레기값)', empty_array)

# 3x3 항등 행렬
identity = np.eye(3)
print('3x3 항등 행렬:\n', identity) # 3x3 항등 행렬:
                                    #  [[1. 0. 0.]
                                    #  [0. 1. 0.]
                                    #  [0. 0. 1.]

# 4x5 행렬에서 대각선이 1이 나오게끔
matrix = np.eye(4,5)
print('4x5 대각 1:\n', matrix) # 4x5 대각 1:
                            #  [[1. 0. 0. 0. 0.]
                            #  [0. 1. 0. 0. 0.]
                            #  [0. 0. 1. 0. 0.]
                            #  [0. 0. 0. 1. 0.]]

# 대각선 위치 조정 (k 매개변수)
matrix = np.eye(4, k = 1) # -면 아래쪽 대각선으로 이동
print('위쪽 대각선:\n', matrix) # 위쪽 대각선:
                            #  [[0. 1. 0. 0.]
                            #  [0. 0. 1. 0.]
                            #  [0. 0. 0. 1.]
                            #  [0. 0. 0. 0.]]

# 정방 항등 행렬
identity = np.identity(4)
print('4x4 항등 행렬:\n', identity) # 4x4 항등 행렬:
                                #  [[1. 0. 0. 0.]
                                #  [0. 1. 0. 0.]
                                #  [0. 0. 1. 0.]
                                #  [0. 0. 0. 1.]]


# 0과 1 사이의 균일 분포
random_uniform = np.random.rand(3,4)
print('0과 1 사이 균일 분포:\n', random_uniform)
rounded = np.round(random_uniform,2)
print('0~1 균일 분포 (소수점 2자리):\n', rounded)

# 특정 범위의 균일 분포
low, high, = 10, 20
random_range = low + (high - low) * np.random.rand(3,3)
print(f'{low}부터 {high}사이 균일 분포:\n', random_range)

uniform = np.random.uniform(low = 0, high = 100, size = (2,3))
print(f'0부터 100까지 균일 분포\n', uniform)

# 정규 분포 난수
# 표준 정규 분포 (평균0 표준편차1)
random_normal1 = np.random.randn(3,3)
print('표준 정규 분포\n', random_normal1) # 표준 정규 분포
                                        #  [[ 1.47880777 -1.41987722 -0.9592587 ]
                                        #  [ 0.32379318  0.61998989 -1.09447201]
                                        #  [-0.72324123 -2.07031379 -0.00446553]]

# 평균 100, 표준편차 15인 정규 분포
mean, std = 100, 15
scores = mean + std * np.random.randn(3)
print('표준 정규 분포\n', scores) # 표준 정규 분포
                                # [ 82.04476701  87.33857598 108.93883191]

mean, std = 100, 15
scores = mean + std * np.random.randn(1000)
print('표준 정규 분포\n', scores[:10])
print('실제 평균\n', scores.mean()) # 실제 평균
                                   # 100.15330899501505
print('실제 표준 편차\n', scores.std()) # 실제 표준 편차
                                      # 14.995293300675318

# 정수 난수
# 0~9 사이의 정수 난수
random_int = np.random.randint(0, 10, size = (3,4))
print('0~9까지 정수 난수:', random_int)

# 주사위 시뮬레이션
dice = np.random.randint(1, 7, size = 10)
print('주사위 10번 굴리기:', dice)

# 시드 설정 (재현 가능한 난수)
np.random.seed(42)
random1 = np.random.rand(5)
print('첫 번째 난수:', random1)

np.random.seed(42)
random2 = np.random.rand(5)
print('두 번째 난수:', random2)
print('같은가?', np.array_equal(random1,random2)) # 같은가? True

# 새로운 방식(권장)
rng = np.random.default_rng(seed=42)
random3 = rng.random((2,3))
print('새로운 방식 난수:', random3)