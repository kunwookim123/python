import pandas as pd
# import numpy as np

# 통계 함수
# 데이터의 특징을 숫자로 요약하는 것


daily_sales = pd.Series([
    332,221,452,577,654,834,
    628,970,351,214,512,662,
    623,678,564,745,232,887,
    508,522,321,433,435,683,
    439,590,503,729,121,120],
    index=pd.date_range('2025-09-01', periods = 30),
    name = 'September Sales'
)
# 평균(mean)
mean_value = daily_sales.mean()
print(f'1. 평균 (mean): {mean_value:.2f}만원')

# 중앙값(median)
median_value = daily_sales.median()
print(f'2. 중앙값 (median): {median_value}만원')

# 최빈값(mode)
mode_value = daily_sales.mode()
print(f'3. 최빈값 (mode): {mode_value}만원')

# 산포도 측정
# 데이터가 얼마나 퍼져있는지 알려주는 통계량

print('======산포도 측정======')
max_value = daily_sales.max()
min_value = daily_sales.min()

print(f'1. 최댓값: {max_value}') # 1. 최댓값: 970
print(f'2. 최솟값: {min_value}') # 2. 최솟값: 120

# 범위 : 최댓값 - 최솟값
range_value = max_value - min_value
print(f'3. 범위: {range_value}') # 3. 범위: 850

# 분산: 평균으로부터 떨어진 정도의 제곱의 평균
variance = daily_sales.var()
print(f'4. 분산: {variance:.2f}') # 4. 분산: 47143.10

# 표준편차: 분산의 제곱근
std_dev = daily_sales.std()
print(f'5. 표준편차: {std_dev:.2f}') # 5. 표준편차: 217.12

# 표준편차 해석
print('표준편차 해석:')
print(f'평균 표준편차: {mean_value - std_dev:.2f} ~ {mean_value + std_dev:.2f}') # 평균 표준편차: 300.88 ~ 735.12
print()
# 한 번에 모든 통계 표시
print(daily_sales.describe())