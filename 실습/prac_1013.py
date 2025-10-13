import pandas as pd
import numpy as np


# # 과제1

# practice_data = pd.DataFrame({
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'age': [25, 30, 35],
#     'city': ['Seoul', 'Busan', 'Daegu']
# })

# practice_data.to_csv('pratice.csv', index = False)
# print('CSV 파일로 저장')

# df = pd.read_csv('pratice.csv')
# print('===CSV 파일 읽기===')
# print(df)
# print()

# # 과제2

# korean_data = pd.DataFrame({
#     '이름': ['김철수', '이영희', '박민수'],
#     '직급': ['사원', '대리', '과장']
# })

# korean_data.to_csv('korean_data.csv', index = False, encoding = 'utf-8-sig')
# print('CSV 파일로 저장')

# df = pd.read_csv('korean_data.csv', encoding = 'utf-8-sig')
# print('===CSV 파일 읽기(한글 포함)===')
# print(df)

# 실습4

data = {

"도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],

"미세먼지": [45, 51, np.nan, 38, 49, np.nan],

"초미세먼지": [20, np.nan, 17, 18, 22, 19],

"강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]

}

df = pd.DataFrame(data)

# 1.'미세먼지' 컬럼의 평균과 중앙값
mean = df['미세먼지'].mean()
print('평균:', mean)
median = df['미세먼지'].median()
print('중앙값:', median)
print()

# 2.'초미세먼지' 컬럼의 최댓값과 최솟값
max_cols = df['초미세먼지'].max()
print('최댓값:', max_cols)
min_cols = df['초미세먼지'].min()
print('최솟값:', min_cols)
print()

# 3.각 컬럼별 결측값 갯수 
print(df.isna().sum())
print()

# 4.결측값이 하나라도 있는 행을 모두 삭제한 뒤, 남은 데이터의 '초미세먼지' 평균
drop_rows = df.dropna()
print('결측값 제거\n', drop_rows)
drop_rows_mean = drop_rows['초미세먼지'].mean()
print('결측값 제거후 평균:', drop_rows_mean)
print()

# 5.결측값을 모두 0으로 채운 뒤, '미세먼지'와 '초미세먼지'의 합계를 각각 구하시오
fill_zero = df.fillna(0)
print(fill_zero)
print('미세먼지 합계:',fill_zero['미세먼지'].sum())
print('초미세먼지 합계:',fill_zero['초미세먼지'].sum())
print()

# 6.'미세먼지'컬럼의 결측값을 평균값으로 채운 뒤, 그 표준편차 구하기
fill_mean = df.copy()
fill_mean['미세먼지'] = fill_mean['미세먼지'].fillna(fill_mean['미세먼지'].mean())
print(fill_mean)
print('표준편차:', fill_mean['미세먼지'].std())