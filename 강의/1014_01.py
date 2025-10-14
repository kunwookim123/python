import pandas as pd
import numpy as np
# 그룹화와 집계

# groupby
'''
    그룹화는 데이터를 특정 기준에 따라 묶에서 분석하는 것

    전체 평균만으로는 부족한 경우 많음
    카테고리별, 기간별로 나누어 보면 숨겨진 패턴 발견
    segment별 비교 분석 가능
'''

employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})

print('전체 직원 데이터')
print(employee_data)

# 전체 분석 vs 그룹별 분석
print('전체 분석')
overall_avg = employee_data['salary'].mean()
print('전체 평균 연봉:', overall_avg)


print('그룹별 분석')
dept_avg = employee_data.groupby('department')['salary'].mean()
print(dept_avg)
print()

# gruopby의 핵심
'''
    split - apply - combine
    3단계 프로세스

    1. split(분할) - 데이터를 그룹으로 나누기
    2. apply(적용) - 각 그룹에 함수 적용하기
    3. combine(결합) - 결과를 하나로 합치기
'''

print('===split - apply - combine===')
simple_data = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [10, 20, 15, 25, 12, 22]
})
print('원본 데이터')
print(simple_data)
print()

# 1단계 split(분할)
for category, group in simple_data.groupby('category'):
    print(f'{category} 그룹')
    print(group)
print()
# 2단계 apply(적용)
for category, group in simple_data.groupby('category'):
    avg = group['value'].mean()
    print(f'{category} 그룹 평균 {avg}')
print()
# 3단계 combine(결합)
result = simple_data.groupby('category')['value'].mean()
print(result)
print()

# groupby(by = None, axis = 0, level = None, as_index = True, sort = True....)
'''
    by : 그룹화 기준 (컬럼명 또는 컬럼명 리스트)
    as_index : 그룹 키를 인덱스로 사용 여부 (기본값 = True)
    sort : 그룹 키를 정렬할지 여부 (기본값 = True)
     
'''

employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})
# 방법 1 - 컬럼명 문자열
result = employee_data.groupby('department')['salary'].mean()
print(result)
print()
# 방법 2 - 컬럼 접근 후 집계
result1 = employee_data.groupby('department').salary.mean()
print(result1)
print()

# 여러 컬럼 선택
result2 = employee_data.groupby('department')[['salary','years']].mean()
print(result2)
print()

# as_index 매개변수
result_indexed = employee_data.groupby('department', as_index=True)['salary'].mean()
print(result_indexed)
print(f'타입: {type(result_indexed)}')
print()

result_no_indexed = employee_data.groupby('department', as_index=False)['salary'].mean()
print(result_no_indexed)
print(f'타입: {type(result_no_indexed)}')
print()

# sort 매개변수
result_sorted = employee_data.groupby('department', sort=True)['salary'].mean() # 알파벳 순으로 정렬
print(result_sorted)
print()

result_no_sorted = employee_data.groupby('department', sort=False)['salary'].mean() # False 사용시 약간의 성능 향상 있음
print(result_no_sorted)
print()

'''
    count() - 개수
    var() - 분산
    std() - 표준편차
    mean() - 평균
    median() - 중앙값
    등등
'''

result = employee_data.groupby('department')['salary'].describe()
print(result)
print()

employee_detail = pd.DataFrame({
    'department': ['Dev', 'Dev', 'Dev', 'Sales', 'Sales', 'Sales', 'HR', 'HR'],
    'position': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Mid', 'Senior'],
    'gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'F'],
    'salary': [4000, 4500, 5500, 3800, 4300, 5200, 4500, 5300]
})

multy_group = employee_detail.groupby(['department', 'position'])['salary'].mean()
print(multy_group)
print()

# agg() 다양한 사용법

monthly_sales = pd.DataFrame({
    'month': [1, 1, 2, 2, 3, 3, 1, 2, 3],
    'store': ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'C'],
    'sales': [100, 80, 120, 90, 150, 100, 110, 95, 130],
    'customers': [50, 40, 60, 45, 75, 50, 55, 48, 65]
})

# 1. 함수 이름 리스트
result1 = employee_detail.groupby('department')['salary'].agg(['mean', 'sum', 'std'])
print(result1)
print()

# 2. 함수 객체 사용 (경고 뜸, 권장 x)
# result2 = employee_detail.groupby('department')['salary'].agg([np.mean, np.sum, np.std])
# print(result2)

# 3. 딕셔너리로 컬럼명 다른 함수

result2 = monthly_sales.groupby('store').agg({'sales' : ['mean', 'sum'], 'customers': ['mean', 'max']})
print(result2)