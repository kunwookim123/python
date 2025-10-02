import numpy as np
# # 실습1
# # 문제1. 1차원 배열 [5, 12, 18, 7, 30, 25]에서 10보다 크고 20보다 작은 값만 필터링하세요.
# arr = np.array([5, 12, 18, 7, 30, 25])
# print('10보다 크고 20보다 작은 값:', arr[(arr > 10) & (arr < 20)])
# # 문제2. 배열 [10, 15, 20, 25, 30, 35]에서 15 이하이거나 30 이상인 값만 선택하세요.
# arr = np.array([10, 15, 20, 25, 30, 35])
# print('15 이하이거나 30 이상인 값:', arr[(arr <= 15) | (arr >= 30)])
# # 문제3. 배열 [3, 8, 15, 6, 2, 20]에서 10 이상인 값을 모두 0으로 변경하세요.
# arr = np.array([3, 8, 15, 6, 2, 20])
# arr[arr >= 10] = 0
# print('10 이상인 값을 0으로 만든 배열:', arr)
# # 문제4. 배열 [7, 14, 21, 28, 35]에서 20 이상인 값은 "High", 나머지는 "Low"로 표시하는 새로운 배열을 생성하세요.
# arr = np.array([7, 14, 21, 28, 35])
# result = np.where(arr >= 20, 'High', 'Low')
# print('20 이상인 값은 "High", 나머지는 "Low"로 표시하는 새로운 배열:', result)
# # 삼항 연산자
# # 참일때 값 if 조건 else 거짓일때 값

# # 문제5. 0~9 범위의 배열에서 짝수는 그대로 두고, 홀수는 홀수 값 × 10으로 변환한 배열을 만드세요
# arr = np.arange(10)
# arr[arr[1::2]] *= 10
# print('짝수는 그대로 두고, 홀수는 홀수 값 x 10으로 변환한 배열:', arr)
# # 문제6. 아래 2차원 배열 에서 20 이상 40 이하인 값만 선택하세요.
# arr = np.array([
#     [10, 25, 30],
#     [40, 5, 15],
#     [20, 35, 50]
#     ])
# print('20 이상 40 이하인 값:', arr[(arr >= 20) & (arr <= 40)])
# # 문제7. 배열 [1, 2, 3, 4, 5, 6]에서 3의 배수가 아닌 값만 선택하세요.
# arr = np.array([1, 2, 3, 4, 5, 6])
# print('3의 배수가 아닌 값:', arr[~(arr % 3 == 0)])
# # 문제8. 랜덤 정수(0~100) 10개 배열에서 아래와 같이 새로운 배열을 만드세요.
# # 50 이상인 값은 그대로
# # 50 미만인 값은 50으로 변경
# arr = np.random.randint(0,101, size = (10))
# print('원본 배열:', arr)
# arr[arr < 50] = 50
# print('50 이상인 값은 그대로, 50 미만인 값은 50으로 변경:', arr)
# # 문제9. 2차원 배열에서 아래와 같이 분류된 문자열 배열을 생성하세요.
# # 70 이상 → "A"
# # 30 이상 70 미만 → "B"
# # 30 미만 → "C“
# arr = np.array(
#     [[5, 50, 95],
#     [20, 75, 10],
#     [60, 30, 85]]
#     )
# rank = np.where(arr >= 70,'A',np.where(arr < 30, 'C', 'B'))
# print(rank)

# 실습1
# 1. 아래의 배열을 사용해서 ravel과 flatten을 각각 사용해 1차원 배열로 변환하고, arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과에 어떤 변화가 있는지 확인하세요.
arr= np.array([[10, 20], [30, 40], [50, 60]])
raveled =arr.ravel()
flattened =arr.flatten()
print('ravel 결과:', raveled)
print('flatten 결과:', flattened)

arr[0,0] = 999
print('원본 변경 후 ravel:', raveled)
print('원본 변경 후 flatten:', flattened)
print()

# 2. 크기가 32x32인 이미지 데이터를 가정하고, 이 배열에 대해 expand_dims를 사용하여 shape (1, 32, 32)로 바꾸는 코드를 작성하세요.
img= np.random.rand(32, 32)
img_expanded = np.expand_dims(img, axis=0)
print('shape:',img_expanded.shape)
print()

# 3. 아래 배열에서 불필요한 1차원을 모두 제거하여 shape이 (28, 28)이 되도록 만드세요.
img= np.random.randint(0, 255, (1, 28, 28, 1))
img_squeezed = np.squeeze(img)
print('불필요한 1차원을 모두 제거한 shape:',img_squeezed.shape)
print()

# 4. 아래 2차원 배열을 1) 1차원 배열로 만든 후 2) 중복값을 제거한 뒤 shape (1, n)으로 재구성하세요.
arr= np.array([
    [3, 1, 2, 2],
    [1, 2, 3, 1],
    [2, 2, 1, 4]])

arr_flattened = arr.flatten()
print('1차원 배열:',arr_flattened)
uniq_arr = np.unique(arr)
print('중복값 제거후 배열:', uniq_arr)
uniq_arr_expanded = np.expand_dims(uniq_arr, axis=0)
print('중복값 제거후 shape(1,n)으로 재구성한 배열:',uniq_arr_expanded)
print('shape:',uniq_arr_expanded.shape)
print()

# 1. 다음 두 배열을 행 방향으로 이어붙이세요.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
concated = np.concatenate((a,b), axis=0)
print('행 방향 결합 \n', concated)
print()

# 2. 아래 배열을 3개로 같은 크기로 분할하세요.
a = np.arange(12)
split_equal = np.split(a, 3)
for idx, sub in enumerate(split_equal):
    print(idx + 1, sub)
print()

# 3. 다음 배열들을 새로운 축에 쌓아 shape이 (3, 2)인 배열을 만드세요.
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])

stacked_arr = np.stack((a,b,c), axis=0)
print('새로운 배열\n',stacked_arr)
print('shape:', stacked_arr.shape)
print()

# 4. shape가 (2, 3)인 아래 두 배열을 shape (2, 2, 3)인 3차원 배열을 만드세요.
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
stack_arr = np.stack((a,b), axis=1)
print('shape:', stack_arr.shape)
print()
# 5. 아래의 1차원 배열을 2:3:3 비율(총 3개)로 분할하세요.
arr= np.arange(8)
split_arr = np.split(arr,[2,5])
print('2:3:3 비율 배열:',split_arr)
print()
# 6. 아래 두 배열을 axis=0, axis=1로 각각 stack하여 두 경우의 결과 shape을 모두 구하세요
a = np.ones((2, 3))
b = np.zeros((2, 3))
concat_id = np.concatenate([a,b], axis=0)
print('axis=0 shape:',concat_id.shape)
concat_id1 = np.concatenate([a,b], axis=1)
print('axis=1 shape:',concat_id1.shape)
print()

# 1. 아래의 1차원 배열을 오름차순과 내림차순으로 각각 정렬하는 코드를 작성하세요.
arr= np.array([7, 2, 9, 4, 5])
sort_arr = np.sort(arr)
print('오름차순:',sort_arr)
sort_arr = np.sort(arr)[::-1]
print('내림차순:',sort_arr)
print()
# 2. 아래의 2차원 배열에서 각 행(row) 별로 오름차순 정렬된 배열을 구하세요.
arr= np.array([[9, 2, 5],[3, 8, 1]])
sort_axis1 = np.sort(arr, axis=1)
print('행 별 오름차순 정렬\n',sort_axis1)
print()
# 3. 아래의 1차원 배열에서 정렬 결과(오름차순)가 되는 인덱스 배열을 구하고, 그 인덱스를 이용해 원본 배열을 직접 재정렬하는 코드를 작성하세요.
arr= np.array([10, 3, 7, 1, 9])
sorted_idx = np.argsort(arr)
print('인덱스 배열:',sorted_idx)
sorted_arr = arr[sorted_idx]
print('원본 배열 재정렬:',sorted_arr)
print()
# 4. 아래 2차원 배열을 열(column) 기준(axis=0)으로 오름차순 정렬된 배열을 구하세요.
arr= np.array([[4, 7, 2],[9, 1, 5],[6, 8, 3]])
sorted_col = np.sort(arr, axis=0)
print('열 기준 오름차순 배열\n',sorted_col)