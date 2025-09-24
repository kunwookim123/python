# # # 실습1
# # # 문제1
# # # 1단계
# # emtpy_dict = dict()
# # print('empty_dict', emtpy_dict)

# # # 2단계
# # person = {
# #     'username': 'skywalker',
# #     'email': 'sky@example.com',
# #     'level': 5
# # }
# # print('person', person)

# # # 3단계
# # email_value = person.get('email')
# # print('email_value:', email_value)

# # # 4단계
# # person['level'] = 6
# # print('person:', person)

# # # 5단계
# # phone = person.get('phone','미입력')
# # print('phone:', phone)

# # # 6단계
# # person.update({'nickname': 'sky'})
# # del person['email']
# # person.setdefault('singup_date', '2025-07-10')
# # print('person:', person)

# # # 문제2
# # student = {}
# # student_name = ['Alice', 'Bob', 'Charlie']
# # student_score = [85,90,95]
# # student1 = dict(zip(student_name, student_score))
# # print('student1', student1)

# # student1.update({
# #     'David': 80
# # })
# # print('student1', student1)

# # student1['Alice'] = 88
# # del student1['Bob']
# # print('student1', student1)

# # # 실습1
# # # 문제1
# # numbers = [3, 6, 1, 8, 4]
# # number = []
# # for i in numbers:
# #     number.append(i*2)
# # print(number)

# # # 문제2
# # words = ['apple', 'banana', 'kiwi', 'grape']
# # len_words = []
# # for i in words:
# #     len_words.append(len(i))
# # print('len_words:',len_words)

# # # 문제3
# # coordinates = [(1,2),(3,4),(5,6),(7,8)]
# # x_values, y_values = [],[]
# # for x, y in coordinates:
# #     x_values.append(x)
# #     y_values.append(y)
# # print('x_values:', x_values)
# # print('y_values:', y_values)

# # 실습2
# # 문제1
# number = int(input('수를 입력하세요.'))
# sum = 0
# for i in range(0,number+1):
#     sum += i
# print(sum)

# # 문제2
# num = int(input('정수를 입력하세요.'))

# for i in range(1,10):
#     print(f'{num}x{i} = {num*i}')

# # 문제3
# sum1 = 0
# for i in range(3,101,3):
#     sum1 += i
# print(sum1)

# # 문제4
# n = int(input('숫자를 입력하세요.'))
# for i in range(1,n+1):
#     if (not i % 2) and (not i % 5):
#         print(i)