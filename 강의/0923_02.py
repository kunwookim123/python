# 추상 클래스
'''
    직접 객체를 만들 수 없고,
    반드시 상속 받아서 완성해야 사용할 수 있는 미완성 설계도

    동물 - 실제로 '동물'만 있는건 없고, 개,고양이,새 등 구제적인 동물이 있음
    악기 - 추상적 피아노, 기타, 드럼 등 - 구체적
'''

# 추상 클래스의 필요성
# 추상 클래스 x

# class Animal:
#     def make_sound(self):
#         pass # 구현을 깜박할 수 있음


# class Dog(Animal):
#     def __init__(self):
#         print('강아지가 밥을 먹습니다.')

# # 문제 발생
# dog = Dog()
# dog.make_sound() # 아무것도 안 일어남 - 버그

# # 추상 클래스 o

# from abc import ABC, abstractmethod

# class Animal(ABC): # 추상 클래스
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         pass

#     def eat(self):
#         print('강아지가 밥을 먹습니다.')

# dog = Dog()


# # 기본 사용법
# # from abc import ABC, abstractmethod

# class 추상클래스이름(ABC): # ABC 상속 필수!
#     @abstractmethod
#     def 추상메서드이름(self):
#         pass

# # 추상 메서드는 반드시 자식 클래스에서 구현해야함!!


# from abc import ABC, abstractmethod

# class Animal(ABC): # 추상 클래스
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         pass

#     def eat(self):
#         print('강아지가 밥을 먹습니다.')

# # animal = Animal() # 에러 발생 - 추상 클래스는 직접 생성 불가
# dog = Dog() # 추상 메서드를 모두 구현했으므로 가능


# class Shape(ABC):
#     '''추상 클래스'''

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         # super().__init__()
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius
    
# # shape = Shape()
# circle = Circle(5)
# print(circle.area())


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # 일반 메서드 - 모든 동물이 공퉁으로 사용
#     def sleep(self):
#         print(f'{self.name}이(가) 잠을 잡니다.')

#     def eat(self):
#         print(f'{self.name}이(가) 먹이를 먹습니다.')

#     # 추상 메서드 - 각 동물마다 다르게 구현해야 함
#     @abstractmethod
#     def make_sound(self):
#         pass

#     @abstractmethod
#     def move(self):
#         pass


# class Dog(Animal):
#     def make_sound(self):
#         print(f'{self.name}: 멍멍!')

#     def move(self):
#         print(f'{self.name}이(가) 뛰어다닙니다.')

# class Bird(Animal):
#     def make_sound(self):
#         print(f'{self.name}: 짹짹!')

#     def move(self):
#         print(f'{self.name}이(가) 날아다닙니다.')

# dog = Dog('바둑이', 3)
# bird = Bird('참새', 1)

# # 부모 클래스의 일반 메서드
# dog.eat()
# bird.sleep()

# # 부모 클래스의 추상 메서드
# dog.move()
# bird.make_sound()

# 모듈
'''
    파이썬 코드가 저장된 파일
    함수, 변수, 클래스 등을 모아놓은 파일로 다른 프로그램에서 가져다 쓸 수 있음

    예시
    도구 상자 : 여러 도구(함수)를 모아둔 상자(모듈)
    레고 블록 : 필요한 블록(모듈)을 가져와서 조립
    요리 레시피 : 필요한 레시피(모듈)를 참고해서 요리
'''

# 코드 재사용 : 한 번 작성한 코드를 여러 곳에서 사용
# 유지 보수 : 기능별로 분리하여 관리가 쉬움
# 협업 : 팀원들과 코드 공유가 편리
#네임스페이스 : 이름 충돌 방지

# 전체 모듈 가져오기
# import calc

# result = calc.add(10,5)
# print(result)

# 작성되어있는 모듈
# import math
# import random
# import datetime

# 패키지
'''
    패키지는 모듈들을 모아 놓은 디렉토리
    관련된 모듈들을 체계적으로 관리할 수 있음
'''

from my_package import module1
from my_package import module2

module1.greet()
module2.hello()

from my_package.module1 import greet
from my_package.module2 import hello

# 가상 환경이란
# 프로젝트 별로 독립적인 패키지 환경을 만들 수 있음
# python -m venv 이름(쓰고싶은 이름) -> 가상환경 생성
# source myenv/Scripts/activate -> 가상환경 활성화
# deactivate -> 비활성화

# pip
# 파이썬 패키지 관리자
# pip list - 현재 설치된 패키지 확인 가능

