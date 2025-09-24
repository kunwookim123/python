# 실습1
# 문제1. 책 클래스 만들기
class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 0
    def read_page(self, pages):
        '''현재 페이지를 읽음. 촐 페이지 수를 넘지 않도록 처리'''
        if pages < 0:
            return
        
        self.current_page = min(self.total_pages, self.current_page + pages)
    
    def progress(self):
        '''
            전체에서 얼마나 읽었는지 퍼센트로 소수점 1자리 까지 표시
        '''        
        pct = (self.current_page / self.total_pages) * 100
        return round(pct,1)
    
    def __repr__(self):
        return f'<Book {self.title} by {self.author}'
    
# 객체 생성
b = Book('파이썬 클린코드', '홍길동', total_pages = 320)
b.read_page(100)
print(b)
print('책 정보')
print(b)
print()
print(b.progress(), '%')
b.read_page(1000)
print(b.progress(), '%')

# 문제2. Rectangle 클래스 구현
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
        
rectangle = Rectangle(20,40)
print('사각형의 넓이:', rectangle.area())

# 실습2
# 문제1. User 클래스 구현
class User:
    total_users = 0
    def __init__(self,username,points):
        self.username = username
        self.points = points
        User.total_users += 1

    def add_points(self,amount):
        self.points += amount
        print(f'포인트 추가: {amount}점')
        
    @classmethod
    def get_total_users(cls):
        print(f'총 유저 수: {cls.total_users}')
    
    def get_level(self):
        if self.points >= 500:
            return 'gold'
        elif self.points <= 99:
            return 'silver'
        else:
            return 'Silver'

user1 = User('이영희',420)
user2 = User('김철수',655)
user3 = User('홍길동',50)
user1.add_points(100)
print(user1.get_level())
print(user2.get_level())
print(user3.get_level())

User.get_total_users()