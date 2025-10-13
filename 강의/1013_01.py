import pandas as pd


# CSV 파일
# CSV(Comma-Separated Values) 가장 널리 사용되는 데이터 파일 형식

'''
    특징
    쉼표(,)로 값을 구분
    텍스트 파일이라 어디서나 열람 가능
    가볍고 빠름
    Excel, Google 시트 등과 호환 가능
'''

# CSV 파일 예시 내용
'''
name, age, city, salary
john,  25, Seoul, 50000
jane,  30, Busan, 60000
Park,  35, Daegu, 55000
'''

sample_data = pd.DataFrame({
    'name': ['John','Jane','Park'],
    'age': [25,30,35],
    '도시': ['서울','부산','대구'],
    'salary': [50000,60000,55000]
})
# utf-8로 저장 (기본값, 권장)
sample_data.to_csv('sample_data.csv', index = False,
                   encoding = 'utf-8-sig')
# utf-8-sig : UTF8 + BOM (Excel 호환)

# cp-949로 저장 (window 한글)
# sample_data.to_csv('sample_data.csv', index = False,
#                    encoding = 'cp-949')

df = pd.read_csv('sample_data.csv', encoding = 'utf-8-sig')
# df = pd.read_csv('sample_data.csv', encoding = 'cp-949')
print('===CSV파일 읽기===')
print(df)
print(f'데이터 타입:\n {df.dtypes}')
print(f'데이터 크기:\n {df.shape}')

sample_data = pd.DataFrame({
    'name': ['John','Jane','Park'],
    'age': [25,30,35],
    '도시': ['서울','부산','대구'],
    'salary': [50000,60000,55000]
})

# sep - 구분자 설정
sample_data.to_csv('tab_separated.txt', sep = '\t', index = False)

df_tab = pd.read_csv('tab_separated.txt', sep = '\t')
print('===CSV sep=탭 파일 읽기===')
print(df_tab)
print()
print(df_tab.head()) # 처음 5개 행을 가지고 옴 (기본값)

# Excel
# 엑셀은 마이크로소프트 스프레드시트 프로그램
'''
    특징
    여러 시트(sheet) 지원
    서식, 수식 포함 가능
    비즈니스에서 가장 많이 사용
    확장자(.xlsx) 최신, (.xls) 구버전
    pip install openpyxl
'''

sample_data = pd.DataFrame({
    'name': ['John','Jane','Park'],
    'age': [25,30,35],
    '도시': ['서울','부산','대구'],
    'salary': [50000,60000,55000]
})

sample_data.to_excel('sample_data.xlsx', index = False, sheet_name='Default')
print('샘플 엑셀 파일 생성 완료')

df_excel = pd.read_excel('sample_data.xlsx')
print('===Excel 파일 읽기===')
print(df_excel)

# 여러 시트 다루기
sample_data = pd.DataFrame({
    'name': ['John','Jane','Park'],
    'age': [25,30,35],
    '도시': ['서울','부산','대구'],
    'salary': [50000,60000,55000]
})
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    sample_data.to_excel(writer, sheet_name='Default1', index = False)
    sample_data['name'].to_excel(writer, sheet_name='name', index = False)

print('2개의 시트를 가진 엑셀 파일 생성 완료')

# JSON
# JSON(JavaScript Object Notation)
# 웹에서 많이 사용되는 데이터 형식

sample_data = pd.DataFrame({
    'name': ['John','Jane','Park'],
    'age': [25,30,35],
    '도시': ['서울','부산','대구'],
    'salary': [50000,60000,55000]
})

sample_data.to_json('sample_data.json', orient='records', index = 2)
print('JSON 파일 저장')
print()

df_json = pd.read_json('sample_data.json')
print('===JSON 파일 읽기===')
print(df_json)



data = {
"이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원"],
"나이": [23, 35, 31, 40, 28, 34],
"직업": ["학생", "군인", "장군", "장군", "상인", "왕자"]
}
df = pd.DataFrame(data)

# 인덱싱
print('===인덱싱===')
print(df['이름'])
print(df[['이름','직업']])
print(df[['이름','직업','나이']])
print()

# 슬라이싱
print(df[1:3])
print()
print(df[-2:])
print()

# DataFrame의 슬라이싱은 행(Row)를 기준으로 동작
# 열 단위 슬라이싱은 명시적으로 지정해야 함
print(df[-2:]['이름'])
print()

# iloc
print(df.iloc[0]) # 이름    홍길동
                  # 나이     23
                  # 직업     학생
print()
print(df.iloc[:, 1]) # 전체 행에서 1번째 컬럼인 나이만 출력
print(df.iloc[[0,2,4], [0,2]]) # 0,2,4번째 행만 0,2번째 컬럼 내용만 출력
print()

# loc
print(df.loc[0]) # 0번째 인덱스 행 출력
print(df.loc[:,'나이'])
print(df.loc[:,['이름','나이']])
print(df.loc[1:3,['이름','나이']]) # 3행 포함!! 제외x



