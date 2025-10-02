# 실습2

import numpy as np

# 문제1. 다음 배열에서 2,4,6번째 요소를 fancy indexing으로 선택
arr = np.arange(10,30,2)
indices = [1,3,5]
print('2,4,6 요소 선택:', arr[indices]) # 인덱스 [1,3,5] 선택: [12 16 20]

# 문제2. 3x3 배열에서 왼쪽 위 → 오른쪽 아래 대각선의 요소만 인덱싱으로 추출하세요.
arr = np.arange(1, 10).reshape(3, 3)
row_indices = [0,1,2]
col_indices = [0,1,2]
print('대각선 요소:', arr[row_indices,col_indices])

# 문제3. 3x4 배열에서 마지막 열만 선택해 모두 -1로 변경하세요.
arr = np.arange(1, 13).reshape(3, 4)
arr[:,3:] = -1
print('마지막 열 -1:\n', arr)

# 문제4. 4x4 배열에서 행을 역순, 열을 역순으로 각각 슬라이싱해 출력하세요.
arr = np.arange(1, 17).reshape(4, 4)
print('행의 역순:\n', arr[::-1,:])
print('열의 역순:\n',arr[:,::-1])

# 문제5. 4x5 배열에서 가운데 2x3 부분을 슬라이싱한 뒤 copy()를 이용해 독립 배열을 만드세요.
arr = np.arange(1, 21).reshape(4, 5)
print('원본:\n', arr)
copy = arr[1:3,1:4].copy()
print('copy:\n', copy)

# 문제6. 3x4 배열에서 짝수이면서 10 이상인 값만 선택하세요.(&을 활용)
arr = np.array([[ 4,  9, 12,  7], [10, 15, 18,  3], [ 2, 14,  6, 20]])
print('짝수이면서 10 이상인 값:', arr[(arr % 2 ==0) & (arr >= 10)])


# 문제7. 5x5 배열에서 2, 4번째 행을 선택하고, 선택된 행에서 열 순서를 [4, 0, 2]로 재배치하세요.
arr = np.arange(1, 26).reshape(5, 5)
print(arr)
print(arr[[1,3]][:,[4,0,2]])


# 문제8. 5x3 배열에서 각 행의 첫 번째 값이 50 이상인 행만 Boolean Indexing으로 선택하세요.
arr = np.array([[10, 20, 30], [55, 65, 75], [40, 45, 50], [70, 80, 90], [15, 25, 35]])
print('각 행의 첫 번째 값이 50 이상인 행:', arr[arr[:,0] >= 50])

# 문제9. 4x4 배열에서 (0,1), (1,3), (2,0), (3,2) 위치의 요소를 한 번에 선택하세요.
arr = np.arange(1, 17).reshape(4, 4)
print('(0,1), (1,3), (2,0), (3,2) 위치의 요소:', arr[(0,1,2,3),(1,3,0,2)])

# 문제10. 3차원 배열 (2, 3, 4)에서 모든 블록에서 두 번째 열만 추출해 새로운 2차원 배열 (2, 3)을 만드세요.
arr3d = np.arange(24).reshape(2, 3, 4)
print(arr3d)
print('새로운 2차원 배열\n', arr3d[:,:,1].reshape(2,3))

# 실습3
# 문제1. 0부터 24까지 정수를 가진 배열을 만들고, (5, 5) 배열로 변환한 뒤 가운데 행(3번째 행)과 가운데 열(3번째 열)을 각각 1차원 배열로 출력하세요.
arr = np.arange(25).reshape(5, 5)
print(arr)
print('가운데행:', arr[2])
print('가운데열:', arr[:,-3])

# 문제2. 0~99 난수로 이루어진 (10, 10) 배열을 생성하고, 짝수 인덱스의 행만 선택하여 출력하세요.
arr = np.random.randint(0, 100, size = (10,10))
print('전체 배열\n', arr)
row_indices = [1,3,5,7,9]
print('짝수 행들\n', arr[row_indices])

# 문제3. 0부터 49까지 정수를 가진 배열을 (5, 10) 배열로 변환한 후, 2행 3열부터 4행 7열까지의 부분 배열을 추출하세요.
arr = np.arange(50).reshape(5, 10)
print(arr)
print('(2,3) (4,7) 배열\n',arr[1:4,2:7])

# 문제4. 0~9 난수로 이루어진 (4, 4) 배열을 생성하고, 각각 인덱싱으로 추출해 출력하세요.(for 이용)
# 주대각선 요소 (왼쪽 위 → 오른쪽 아래)
# 부대각선 요소 (오른쪽 위 → 왼쪽 아래)
arr = np.random.randint(0, 10, size = (4,4))
print(arr)
for i in range(4):
    print('주대각선:',[arr[i][i]],end='')
print()
for j in range(4):
    print('부대각선:',[arr[j][3-j]],end='')
print()

# 문제5. 0~9 난수로 이루어진 (3, 4, 5) 3차원 배열을 생성하고, 두 번째 층에서 첫 번째 행과 마지막 열의 값을 출력하세요.
arr = np.random.randint(0, 10, size = (3,4,5))
print('원본 배열\n', arr)
print('첫 번째 행, 마지막 값:', arr[1,0,-1])

# 문제6. 35부터 74까지의 순차적인 수로 이루어진 1차원 배열을 만들고 10x4 행렬로 변환 후 출력해주세요.
arr = np.arange(35,75)
print('원본 배열\n',arr)
arr1 = np.arange(35,75).reshape(10,4)
print('10x4 배열\n',arr1)

# 문제7. 6번에서 만든 배열을 맨 끝의 행부터 역순으로 출력해주세요.
arr1 = np.arange(35,75).reshape(10,4)
print('행 역순\n',arr1[::-1,:])

# 문제8. 6번에서 만든 배열 중 두 번째 행부터 마지막 직전 행까지, 세번째 열부터 마지막 열까지 슬라이싱해서 출력해주세요.
arr1 = np.arange(35,75).reshape(10,4)
print('새로운 배열\n', arr1[1:9,2:])

# 문제9. 1부터 50까지의 난수로 된 5x6 배열을 만들고, 배열에서 짝수만 선택하여 출력하는 코드를 작성하세요.
arr = np.random.randint(1,50, size = (5,6))
print('원본 배열\n', arr)
print('짝수만:',arr[arr % 2 == 0])

# 문제10. 0부터 99까지의 정수로 이루어진 (10, 10) 배열을 생성한 후,[1, 3, 5]번째 행과 [2, 4, 6]번째 열의 교차하는 원소들만 선택하여 출력하세요.
arr = np.arange(100).reshape(10,10)
print('원본 행렬\n', arr)
print('교차 요소들:', arr[[1,3,5],[2,4,6]])

# 문제11. 0~9 난수로 이루어진 1차원 배열(길이 15)을 생성하고,짝수 인덱스 위치에 있는 값들 중에서 5 이상인 값만 선택해 출력하세요.
arr = np.random.randint(0,9,size=(15))
print('원본 배열\n', arr)
print('짝수 인덱스 중 5이상인 값:', arr)

# 실습1
# 문제1. 다음 배열을 생성하고, 모든 요소에 3을 더하세요.
arr = np.array([1, 2, 3, 4])
print('모든 요소에 3 더한 배열:', arr + 3)

# 문제2. 아래 2차원 배열에서 각 요소를 -1로 곱한 새로운 배열을 만드세요.
arr = np.array([[5, 10],[15, 20]])
copy = np.array(arr * -1).copy()
print(copy)

# 문제3. 아래 두 배열의 요소별 곱셈과 나눗셈 결과를 각각 출력하세요.
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])

print('곱셈:', arr1 * arr2)
print('나눗셈:', arr1 / arr2)

# 문제4. 아래 배열에서 모든 요소를 최대값 100으로 만들기 위해 필요한 값을 더한 결과 배열을 브로드캐스팅으로 만드세요.
arr = np.array([[95, 97],[80, 85]])
print('원래 배열:\n', arr)
diff = 100 - arr
print('필요한 값의 배열:\n', diff)
max_arr = arr + diff
print('필요한 값을 더한 배열 결과\n', max_arr)

# 문제5. 아래 2차원 배열에서 각 행에 다른 값을 곱하여 새로운 배열을 만드세요.(브로드캐스팅 이용)
# 첫 번째 행은 10을 곱하고
# 두 번째 행은 100을 곱해야 합니다.
arr = np.array([[1, 2, 3], [4, 5, 6]])
multiply = [10],[100]
print('새로운 배열\n',arr * multiply)


# 문제6. 아래 배열에서 각 행마다 다른 스칼라 값을 더하기 위해
# 1차원 배열을 만들어 브로드캐스팅 연산을 수행하세요.
# 첫 번째 행에 100, 두 번째 행에 200, 세 번째 행에 300을 더하세요.
arr = np.array([[10, 20],[30, 40],[50, 60]])
scalar = [100],[200],[300]
print('각 행 합:\n', arr + scalar)

# 실습2
# 문제1. 아래 배열의 전체 합계와 평균을 각각 구하세요.
arr = np.array([5, 10, 15, 20])
print('전체 합:', np.sum(arr))
print('전체 평균:', np.mean(arr))

# 문제2. 다음 2차원 배열에서 전체 최소값과 최대값을 구하세요.
arr = np.array([[3, 7, 1],[9, 2, 8]])
print('전체 최대값:', np.max(arr))
print('전체 최소값:', np.min(arr))

# 문제3. 아래 배열에서 각 열의 합계와 각 행의 합계를 각각 구하세요.
arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print('행별 합:', np.sum(arr, axis=1))
print('열별 합:', np.sum(arr, axis=0))

# 문제4. 아래 배열에서 행별 평균과 열별 평균을 각각 구하세요.
arr = np.array([[10, 20],[30, 40],[50, 60]])
print('행별 평균:', np.mean(arr, axis=1))
print('열별 평균:', np.mean(arr, axis=0))

# 문제5. 1차원 배열에서 전체 표준편차를 구하고, 각 요소가 평균으로부터 얼마나 떨어져 있는지 편차 배열을 만드세요. (값 - 평균)
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print('표준편차:', np.std(arr))
print('전체 평균:', np.mean(arr))
print('편차 배열:', arr - np.mean(arr))

# 문제6. 아래 2차원 배열에서 행 단위 누적 합과 열 단위 누적 곱을 각각 구하세요.
arr = np.array([[1, 2, 3],[4, 5, 6]])
print('누적 합:\n', np.cumsum(arr, axis=1))
print('누적 곱:\n', np.cumprod(arr, axis=0))