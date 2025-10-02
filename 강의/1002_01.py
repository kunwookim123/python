import pandas as pd

print(pd.__version__)

# 데이터 분석
# 과정
# 데이터 수집 -> 데이터 정제
# 데이터 탐색 -> 데이터 분석 -> 시각화
# 인사이트 도출

'''
    1. 데이터 수집
        분석할 자료를 모으는 단계
    2. 데이터 정제
        분석 가능한 형태로 만드는 단계
    3. 데이터 탐색
        데이터의 특성을 파악하는 단계
    4. 데이터 분석
        가설을 검증하고 패턴을 찾는 단계
    5. 시각화
        결과를 이해하기 쉽게 표현하는 단계
    6. 인사이트 도출
        분석 결과를 의사결정에 활용하는 단계
'''

'''
    편의점 사장님의 고민
    문제 : 어떤 제품을 더 많이 주문해야할까?
    데이터 : 지난 3개월 판매 기록
    분석 : 요일별, 시간대별 판매 패턴 파악
    인사이트 : 금요일 저녁에 맥주가 가장 많이 팔린다.
    행동 : 금요일 전에 맥주 재고 확충
'''

# Excel, Pandas 비교

'''
    엑셀로 100만개 데이터를 처리한다면?
    2019 버전 기준 100만행 까지만 제한이 됨
    파일 열기만 해도 5분 이상 소요
    수식 계산 시 프로그램 멈춤
    반복 작업을 수동으로 해야함
'''


# Series
# Pandas의 가장 기본이 되는 1차원 데이터 구조
'''
    1. 1차원 배열 : 데이터가 일렬로 나열
    2. 레이블(인덱스) 보유 : 각 데이터에 이름표를 붙일 수 있음
    3. 동일 타입 : 하나의 Series 안의 모든 데이터는 같은 타입
'''
simple_series = pd.Series([10,20,30,40,50])
print(simple_series)

'''
    Series = Value(값) + Index(인덱스) + Name(이름)
'''
data_series = pd.Series(
    data= [10,20,30,40,50], # 실제 데이터 값
    index = ['Alice','Bob','Charlie','David','Eve'], # 인덱스 : 각 값의 레이블
    name = 'Test_Score' # 이름 : Series 전체의 이름
)
'''
    pd.Series(data=None, index=None, name=None)

    매개변수 설명
    data=None 실제 데이터(필수)
        - 리스트, 딕셔너리, 스칼라값, Numpy 배열
    index=None 인덱스 레이블(선택)
        - 기본값 0,1,2...
    name=None 이름
'''
'''
    각 구성요소의 역할:
    Value(값)
        실제 데이터가 저장되는 부분
        Numpy 배열로 저장됨
        빠른 수치 연산 가능
    Index(인덱스)
        각 값을 식별하는 레이블
        기본값 : 0,1,2,3,...(정수)
        사용자 정의 가능(문자열, 날짜 등)
    Name(이름)
        Series 전체를 설명하는 이름
        선택사항(없어도 됨)
        DataFrame 결합 시 컬럼명이 됨
'''

int_series = pd.Series([1,2,3,4,5])
print(f'Integer Series dtype: {int_series}') # int 64

float_series = pd.Series([1.1,2.2,3.3,4.4,5.5])
print(f'Integer Series dtype: {float_series}') # float 64

str_series = pd.Series(['apple','banana','cherry'])
print(f'Integer Series dtype: {str_series}') # object

bool_series = pd.Series([True, False, True])
print(f'Boolean Series dtype: {bool_series}')

mixed_series = pd.Series([1, 2.5, 3])
print(f'Mixed Series dtype: {mixed_series}')

temp_list = [15.5, 17.2, 18.9, 19.1, 20.1]
temp = pd.Series(temp_list, name = '4월_기온')
print(temp)
# 0    15.5
# 1    17.2
# 2    18.9
# 3    19.1
# 4    20.1
# Name: 4월_기온, dtype: float64

date = pd.date_range('2025-04-01', periods = 5)
print(date)
temp_date = pd.Series(temp_list, index=date, name='4월_기온')
print(temp_date)
# 2025-04-01    15.5
# 2025-04-02    17.2
# 2025-04-03    18.9
# 2025-04-04    19.1
# 2025-04-05    20.1
# Freq: D, Name: 4월_기온, dtype: float64

product = {
    '노트북': 15,
    '마우스': 40,
    '키보드': 20
}

product_series = pd.Series(product, name = '현재재고')
print(product_series)

scalar_series = pd.Series(0, index=['월','화','수','목'], name='판매량')
print(scalar_series)

test_scores = pd.Series(data=[10,20,30,40,50], index = ['Alice','Bob','Charlie','David','Eve'], name = 'Exam')
print('==========Series 속성 전체============')
# 1.value - 실제 데이터 (numpy 배열)
print('1. values (값들)')
print(test_scores.values) # [10 20 30 40 50]
print()
print('2. index (인덱스)')
print(test_scores.index) # Index(['Alice', 'Bob', 'Charlie', 'David', 'Eve'], dtype='object')
print()
print('3. name (이름))')
print(test_scores.name) # Exam
print()
print('4. dtype (타입)')
print(test_scores.dtype) # int64
print()
print('5. shape (모양)')
print(test_scores.shape) # (5,)
print()
print('6. size (크기)')
print(test_scores.size) # 5
print()
print('7. ndim (차원)')
print(test_scores.ndim) # 1
print()

# 인덱싱과 슬라이싱

# 인덱싱
# Series에서 특정 데이터를 선택하는 방법
# 위치 기반 0,1,2...
# 레이블 기반 : 인덱스 이름으로 접근

sales = pd.Series(data=[100,200,300,400], index = ['mon','tue','wed','thur'], name='Daily sale')
wed_sales = sales['wed']
print('수요일 매출:', wed_sales)
print()
# wed_sales2 = sales[2]
# print('수요일 매출:', wed_sales2) # 현재 안됨
print('수요일 매출:', sales.iloc[2]) # 인덱스 접근이 이 방식으로 해야함
print('수요일 매출:', sales.loc['wed'])
print()
selected_days = sales[['mon','wed','thur']]
print(selected_days)
print()

# 슬라이싱
print('처음부터 수요일까지:')
print(sales.loc[:'wed'])
print()
print('수요일부터 끝까지:')
print(sales.loc['wed':])
print()
print('처음부터 끝까지:')
print(sales.iloc[:])
print()
print('역순:')
print(sales.iloc[::-1])
print()

# Boolean 인덱싱
sales = pd.Series(data=[100,200,300,400,250], index = ['mon','tue','wed','thur','fri'], name='Daily sale')
condition = sales >= 200
print(condition) # mon     False
                 # tue      True
                 # wed      True
                 # thur     True

result = sales[condition] # tue     200
                          # wed     300
                          # thur    400
print(result)

# 비교 연산자
print(sales[sales == 200]) # tue    200
print(sales[(sales >= 150) & (sales <= 350)]) # tue    200
                                              # wed    300
print(sales[(sales < 150) | (sales >= 300)])  # mon     100
                                              # wed     300
                                              # thur    400

print(sales[sales != 200]) # mon     100
                           # wed     300
                           # thur    400
                           # fri     250
weekday_high = sales[(sales >= 200) & (sales.index != 'fri')]
print(weekday_high) # tue     200
                    # wed     300
                    # thur    400
weeked_or_low = sales[(sales < 200) | sales.index.isin(['mon','fri'])]
print(weeked_or_low) # mon    100
                     # fri    250

# 벡터화 연산
prices = pd.Series(
    [3000, 1500, 4000, 2000],
    index = ['apple','banana','orange','grape'],
    name = 'price'
)

print('1. 500원 추가:')
print(prices + 500)
print()
print('2. 1000원 할인:')
print(prices - 1000)
print()
print('3. 곱셈:')
print(prices * 0.8)
print()
print('4. 나누기:')
print(prices / 2)
print()

store_a = pd.Series(
    [1000,2000,1500],
    index = ['Apple', 'Pear', 'Orange']
)
store_b = pd.Series(
    [900,2200,1400,2500],
    index = ['Apple', 'Pear', 'Orange','Grape']
)
print(store_a + store_b) # Apple     1900.0
                         # Grape        NaN
                         # Orange    2900.0
                         # Pear      4200.0
price_diff = store_a - store_b
# 결측값(Nan) 처리하며 연산하기
# 1. fill value 사용
price_diff_filled = store_b.sub(store_a, fill_value=0)
print(price_diff_filled) # Apple     -100.0
                         # Grape     2500.0 2500 - 0을 뜻함
                         # Orange    -100.0
                         # Pear       200.0
# 2. reindex로 먼저 맞추기
store_a_reindexed = store_a.reindex(store_b.index, fill_value=0)
print(store_a_reindexed)
price_diff_reindexed = store_b - store_a_reindexed
print(price_diff_reindexed) # Apple     -100
                            # Pear       200
                            # Orange    -100
                            # Grape     2500
# 3. dropna로 결측값 제거 후 연산
price_diff_cleaned = price_diff.dropna()
print(price_diff_cleaned) # Apple     100.0
                          # Orange    100.0
                          # Pear     -200.0
print()

# 비교 연산
store_a = pd.Series(
    [1000,2000,1500],
    index = ['Apple', 'Pear', 'Orange']
)
store_b = pd.Series(
    [900,2200,1400],
    index = ['Apple', 'Pear', 'Orange']
)

is_b_cheaper = store_a > store_b
print('b상점이 더 싼 제품:')
print(is_b_cheaper) # Apple      True
                    # Pear      False
                    # Orange     True

# 저렴한 상점의 가격만 선택
best_prices = store_a.where(is_b_cheaper, store_b)
print(best_prices) # Apple     1000
                   # Pear      2200
                   # Orange    1500
