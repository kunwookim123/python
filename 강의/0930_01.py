# 배열 인덱싱, 슬라이싱

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90])
print('원본 배열:', arr)

# 팬시 인덱싱
indices = [1,4,7]
print('인덱스 [1,4,7] 선택:', arr[indices]) # 인덱스 [1,4,7] 선택: [20 50 80]
indices = [1,3,1,7,4,7]
print('인덱스 [1,3,1,7,4,7] 선택:', arr[indices]) # 인덱스 [1,3,1,7,4,7] 선택: [20 40 20 80 50 80]

# 양수 인덱스 (0부터 시작)
print('첫번째 요소 (인덱스0)', arr[0])
print('2번째 요소 (인덱스2)', arr[2])
print('8번째 요소 (인덱스8)', arr[8])
# print('10번째 요소 (인덱스 10)', arr[10]) - 오류 발생

arr[0] = 100

# 음수 인덱스 (뒤에서부터 시작)
print('마지막 요소 (인덱스-1)', arr[-1])
print('-2번째 요소 (인덱스-2)', arr[-2])
print('-8번째 요소 (인덱스-8)', arr[-8])

arr[-3] = 400
print('수정 후 배열', arr)

# 배열 슬라이싱
arr = np.array([10,20,30,40,50,60,70,80,90])
print('원본 배열:', arr)

print('인덱스 2부터 5까지 (5제외):', arr[2:5])
print('인덱스 처음부터 4까지 (4제외):', arr[:4])
print('인덱스 3부터 끝까지:', arr[3:])
print('짝수 인덱스만:', arr[::2])
print('홀수 인덱스만:', arr[1::2])

# 슬라이싱으로 값 수정
arr[2:5] = 100
print('수정 후 배열', arr) # 수정 후 배열 [ 10  20 100 100 100  60  70  80  90]

arr[2:5] = [10,20,30]
print('수정 후 배열', arr) # 수정 후 배열 [10 20 10 20 30 60 70 80 90]

# arr[2:5] = [10,20,] # 오류 발생 - 요소의 개수를 맞춰야함
# print('수정 후 배열', arr)

original = np.array([1,2,3,4,5])
view = original[1:4]
print('original', original) # original [1 2 3 4 5]
print('view', view) # view [2 3 4]

view[0] = 10
print('original', original) # original [ 1 10  3  4  5]
print('view', view) # view [10  3  4]
view[1:] = 20
print('original', original) # original [ 1 10 20 20  5]
print('view', view) # view [10 20 20]

# new_list = [1,2,3,4,5] # 리스트이기 때문에 불가
# new_list[2:4] = 40
# print(new_list)

# 독립적인 복사본이 필요한 경우
original = np.array([1,2,3,4,5])
copy = original[1:4].copy()

copy[0] = 100
print('original', original) # original [1 2 3 4 5]
print('copy', copy) # copy [100   3   4]


# 2차원 배열
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print('2차원 배열\n', matrix)

print('0,0의 요소', matrix[0,0]) # 0,0의 요소 1
print('2,2의 요소', matrix[2,2]) # 2,2의 요소 9
print('1,2의 요소', matrix[1,2]) # 1,2의 요소 6
# print('3,0의 요소', matrix[3,0]) # error - 없는 요소를 찾기 때문

print('-1,-2의 요소', matrix[-1,-2]) # -1,-2의 요소 8
print('-1,-2의 요소', matrix[-1][-2]) # -1,-2의 요소 8

print('첫번째 행', matrix[0]) # 첫번째 행 [1 2 3]
print('여러 행', matrix[:2]) # 여러 행 [[1 2 3] # 2차원으로 생성
                                   #  [4 5 6]]

print('matrix[:2, :]', matrix[:2, :]) # matrix[:2, :] [[1 2 3]
                                                    #  [4 5 6]]

print('matrix[:2, 1:]', matrix[:2, 1:]) # matrix[:2, 1:] [[2 3]
                                                       #  [5 6]]

# 부분 행렬
matrix = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

print('matrix[:2, 1:]', matrix[:2, 1:]) # matrix[:2, 1:] [[ 2  3  4  5]
                                                       #  [ 7  8  9 10]]
print('matrix[1:3, 1:4]', matrix[1:3, 1:4]) # matrix[1:3, 1:4] [[ 7  8  9]
                                                             #  [12 13 14]]
print('matrix[::2, ::2]', matrix[::2, ::2]) # matrix[::2, ::2] [[ 1  3  5]
                                                             #  [11 13 15]]

# 특정 행들 선택
row_indices = [0,2,3]
print('[0,2,3]행 선택:', matrix[row_indices]) # [0,2,3]행 선택: [[ 1  2  3  4  5]
                                                            #  [11 12 13 14 15]
                                                            #  [16 17 18 19 20]]

# 특정 요소들 선택 (행, 열 인덱스)
row_indices = [0,2,2]
col_indices = [3,2,3]
print('특정 요소들 선택:', matrix[row_indices, col_indices]) # 특정 요소들 선택: [ 4 13 14]

# bool
arr = np.array([1,5,4,7,2,3])
print('4 이상', arr[arr >= 4]) # 4 이상 [5 4 7]
print('2 미만, 4 이상', arr[(arr >= 4) | (arr < 2)]) # 2 미만, 4 이상 [1 5 4 7]
# print('2 이상, 4 이하', arr[(2 <= arr <= 4)]) # 안됨
print('2 이상, 4 이하', arr[(2 <= arr) & (arr <= 4)]) # 2 이상, 4 이하 [4 2 3]

matrix = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])
print('원본 행렬', matrix)
print('9보다 큰 요소들',matrix[matrix > 9]) # 9보다 큰 요소들 [10 11 12 13 14 15 16 17 18 19 20]
print('첫번째 열이 4 이상인 행들',matrix[matrix[:,0]>=4]) # 첫번째 열이 4 이상인 행들 [[ 6  7  8  9 10]
                                                                              #  [11 12 13 14 15]
                                                                              #  [16 17 18 19 20]]
matrix[matrix > 9] = 10
print('원본 행렬', matrix) # 원본 행렬 [[ 1  2  3  4  5]
                                   #  [ 6  7  8  9 10]
                                   #  [10 10 10 10 10]
                                   #  [10 10 10 10 10]]

