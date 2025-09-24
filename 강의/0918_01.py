# 중첩 shile문
print('===========이중 for 문==============')
# 이중 for문 구구단
for i in range(2,10):
    print(f'==={i}단===')
    for j in range(1,10):
        print(f'{i} x {j} = {i * j}')
print()

print('===========이중 while 문==============')
# 중첩 while문 구구단
i = 2 #초기값

while i < 10:
    j = 1 #수 초기값
    print(f'==={i}단===')
    while j < 10:
        print(f'{i} x {j} = {i * j}')

        j += 1 # 수 증가
    i += 1 # 단 증가
print()

# 함수(function)

# 함수는 특정 작업을 수행하는 코드의 묶음
# 한 번 정의하면 필요할 때마다 호출하여 재사용 가능

# 함수를 사용하는 이유
# 1. 코드 재사용성: 같은 코드를 반복할 필요가 없음
# 2. 모듈화: 프로그램을 작은 단위로 나누어 관리
# 3. 가독성 향상: 코드의 의도를 명확히 표현
# 4. 유지보수 용이: 수정이 필요할 때 함수만 변경
# 5. 추상화: 복잡한로직을 단순한 인터페이스로 제공

# 함수 사용 전 - 같은 코드 반복
print('=' * 20)
print('첫 번째 섹션')
print('=' * 20)

print('=' * 20)
print('첫 번째 섹션')
print('=' * 20)

# 함수 사용
def print_section(title):
    print('=' * 20)
    print(f'{title} 섹션')
    print('=' * 20)

print_section('첫번째')
print_section('두번째')


# 함수 정의와 호출
# 함수 정의(definition)
# def 함수이름(매개변수):
    # 실행 코드
    # return 반환값

# 함수 호출(call)
# 결과 = 함수이름(인자)

def say_hello():
    print('안녕하세요!')

say_hello()

def greet(name):
    print(f'안녕하세요! {name}님!')

greet('김철수')
greet('이영희')
print("greet('이영희')",greet('이영희'))


def add(a,b):
    result = a + b
    return result

sum_result = add(3,5)
print(sum_result)
print('add(10,5)', add(10,5))

# 사각형 넓이
def calculate_area(width,height):
    # 문자화 문자열 (docstring)
    """직사각형 넓이를 계산합니다.
    parameters:
            width(float): 직사각형의 너비
            height(float): 직사각형의 높이
    return:
        float: 직사각형의 넓이
    """
    return width * height

print(calculate_area(10,20))

# docstring
print(calculate_area.__doc__)
help(calculate_area)

def greet(name, message = '안녕!'):
    print(f'{name} {message}')

greet('ethan')
greet('김철수', '안녕하세요!')


def add_all(*new_tuple):
    return sum(new_tuple)


result = add_all(1,2,3,4,5)
print(result)

def print_info(**new_dic):
    for key, value in new_dic.items():
        print(f'{key}: {value}')

print_info(name = '홍길동', age = 25, city = '서울')

# 매개변수와 인자
"""
    매개변수(parameter): 함수 정의 시 사용하는 변수
    인자(argument): 함수 호출시 전달하는 실제 값
"""

def multiply(x,y): #x, y는 매개변수
    return x * y

result = multiply(3,5) #3,5는 인자


# 위치 인자(positional arguments)
def introduce(name, age, city):
    print(f'{name} {age} {city}')

# name = 김철수, age = 25, city = 서울
introduce('김철수','25','서울')

# 키워드 인자(keyword arguments)
def introduce(name, age, city):
    print(f'{name} {age} {city}')

# 순서와 상관없이 이름을 전달
introduce(city = '서울', age = 25, name = '김철수')

# 위치 인자, 키워드 인자 혼용
introduce('김철수', city = '서울', age = 25)

# 주의 : 위치 인자는 키워드 인자보다 앞에 와야 함

# introduce(20, city = '부산', name = '이영희')

# 반환값(return)
# 단일 값 반환

def square(n):
    return n ** 2

result = square(5)
print(result) #25

# 여러 값 반환
def calculate_stats(number):
    total = sum(number)
    avg = total / len(number)
    max_num = max(number)
    min_num = min(number)

    return total, avg, max_num, min_num

number = [100,140,230,200]
a,b,c,d = calculate_stats(number)
print('total:', a)
print('avg:', b)
print('max_num:', c)
print('min_num:', d)

stats = calculate_stats(number)
print(stats)


# return의 특징

def check_positive(numbers):
    if numbers > 0:
        return '양수'
    elif numbers < 0:
        return '음수'
    else:
        return '0'
    
print('코드가 실행이 될까요?')

# return은 함수를 종료시킴

# 조기 반환(early return)
def divide(a,b):
    # 예외 상황을 먼저 처리
    if b == 0:
        return '0으로 나눌 수 없습니다.'
    
    return a / b
print(divide(10,2))
print(divide(10,0))

# 기본값 매개변수
def greet(name, greeting = '안녕하세요'):
    print(f'{greeting}, {name}님')

greet('김철수')
greet('이영희', '반갑습니다.')

# 여러 기본값
def create_profile(name, age = 25, city = '서울', job = '개발자'):
    return {
        'name': name,
        'age': age,
        'city': city,
        'job': job
    }
print(create_profile('박민수'))
# {'name': '박민수', 'age': 25, 'city': '서울', 'job': '개발자'}
print(create_profile('김철수',30))
# {'name': '김철수', 'age': 30, 'city': '서울', 'job': '개발자'}
print(create_profile('이영희', job = '모델'))
# {'name': '이영희', 'age': 25, 'city': '서울', 'job': '모델'}

# 가변 위치 인자(*args)
def sum_all(*numbers):
    print(type(numbers))
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1,2,3))
print(sum_all(1,2,3,3,4,5,6,7,8,98))
print(sum_all())

# 가변 키워드 인자(**kwargs)
def print_info(**user):
    # 키워드 인자를 딕셔너리로 받음
    print(type(user))
    print('user',user)
    for key, value in user.items():
        print(f'{key}: {value}')

print_info(name = '김철수', age = 22, city = '서울')
    
def create_student(**info):
    '''
        학생 정보를 생성합니다.
    '''
    student = {
        'name': info.get('name', '이름 없음'),
        'age': info.get('age', 20),
        'grade': info.get('grade', 1),
        'subjects': info.get('subjects', [])
    }
    return student

student1 = create_student(name = '김철수', subjects = [])
print(student1)
# {'name': '김철수', 'age': 20, 'grade': 1, 'subjects': []}
student1 = create_student(name = '김철수', subjects = ['python'])
# {'name': '김철수', 'age': 20, 'grade': 1, 'subjects': ['python']}