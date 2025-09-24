# 상속
'''
    기존 클래스의 속성과 메서드를 물려받아 새로운 클래스를 만드는 것

    동물 : 포유류 -> 개, 고양이(공통 특징: 자기, 먹기)
    자동차 : 차량 -> 승용차, 트럭
    가족 : 부모 -> 자식
'''

# 상속 없이 - 코드 중복이 심각
# class Dog(Animal): # Animal 상속
#     def bark(self):
#         print(f'{self.name}이(가) 멍멍 짖습니다.')

# class Cat(Animal): # Animal 상속
#     def meow(self):
#         print(f'{self.name}이(가) 야옹 웁니다.')

# class Bird(Animal): # Animal 상속
#     def fly(self):
#         print(f'{self.name}이(가)  날아갑니다.')

# class Animal: # 부모 클래스, 기본 클래스
#     def __init__(self, name, eat):
#         self.name = name
#         self.eat = eat
    
#     def d(self):
#         print(f'{self.name}이(가)')


# 기본 문법과 용이
# class 부모클래스:
#     # 부모 클래스 내용
#     pass


# class 자식클래스(부모클래스): # 괄호 안에 부모클래스
#     # 자식 클래스 내용
#     pass

# # 자식은 부모의 모든 것을 물려 받습니다.
# # 부모의 모든 속성과 메서드를 자동으로 사용 가능
# # 추가된 자신만의 속성과 메서드 정의 가능

# # 부모 클래스
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f'안녕하세요. {self.name} 입니다.')

# class Student(Person):
#     def study(self):
#         print(f'{self.name}이(가) 공부합니다.')

# class Teacher(Person):
#     def teach(self):
#         print(f'{self.name}이(가) 수업힙니다.')

# student = Student('김학생', 20)
# teacher = Teacher('박선생', 35)

# # 부모 클래스 메서드 호출
# student.greet()
# teacher.greet()

# # 자식 클래스 만의 메서드 호출
# student.study()
# teacher.teach()


# # super()와 생성자 상속
# # super()
# # super()는 자식 클래스에서 부모 클래스로 접근할 때 사용

# # super() 미사용시 - 문제 발생
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f'Person 생성: {name} {age}')

#     def greet(self):
#         print(f'안녕하세요. {self.name}입니다.')

# class Student(Person):
#     def __init__(self, name, age, student_id): # 부모 클래스에서 넘겨 받아야할 변수도 반드시 써줘야함
#         # 부모 클래스의 __init__을 호출하지 않음
#         super().__init__(name, age) # 부모 클래스에서 __init__ 호출
#         self.student_id = student_id
#         print(f'Student 생성: 학번 {student_id}')

#     def greet(self):
#         super().greet() # 부모의 greet() 먼저 호출
#         print(f'학생입니다.')

# student = Student('김철수', 20, '20250001')
# print(student.name)
# student.greet()


# # 메서드 오버라이딩
# # 오버라이딩 - 부모 클래스의 메서드를 자식 클래스에서 다시 정의 하는것

# class Animal:
#     def make_sound(self):
#         print(f'동물이 소리를 냅니다.')

# class Dog(Animal):
#     def make_sound(self):
#         print(f'멍멍')

# class Cat(Animal):
#     def make_sound(self):
#         print(f'야옹')

# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.make_sound() # 각자 다른 소리

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         return 0
    
#     def info(self):
#         print (f'{self.name}의 넓이: {self.area()}')

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__('직사각형')
#         self.width = width
#         self.height = height

#     def area(self): # 오버라이딩
#         return self.width * self.height
    
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__('원')
#         self.radius = radius
        
#     def area(self): # 오버라이딩
#         return 3.14 * self.radius * self.radius
    

# shapes = [Rectangle(5,3), Circle(4)]
# for shape in shapes:
#     shape.info() # 각자 다른 넓이 계산

