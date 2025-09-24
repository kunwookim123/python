# # 실습1
# nums = [10,20,30,40,50]
# print(nums[::4])

# # 실습2
# nums = [100,200,300,400,500,600,700]
# print(nums[2:5])

# # 실습3
# nums = [1,2,3,4,5]
# for i in range(5):
#     nums[i] *=2
# print(nums)

# # 실습4
# items = ['a','b','c','d','e']
# print(items[::-1])

# # 실습5
# data = ['zero','one','two','three','four','five']
# print(data[::2])

# # 실습6
# movies = ['인셉션','인터스텔라','어벤져스','라라랜드','기생충']
# movies[2:4] = ['매트릭스','타이타닉']
# print(movies)

# # 실습7
# subjects = ['국어','수학','영어','물리','화학','생물','역사','지구과학','윤리']
# print(subjects[3::2])

# # 실습8
# data = ['A','B','C','D','E','F','G','H','I']
# data1 = data[:3]
# data2 = data[3:6]
# data3 = data[6:]
# print(data1[::-1], data2[::-1], data3[::-1])

# 리스트 연산

# 실습1
# fruits = ['apple', 'banana', 'cherry', 'grape', 'watermelon', 'strawberry']
# del fruits[1:4]
# print(fruits)

# 실습2
# letters = ['A','B']
# letters1 = letters*3
# del letters1[2]
# print(letters1)

# 실습3-1
# passengers = ['철수', '영희']
# passengers.extend(['민수', '지훈'])
# passengers.remove('영희')
# passengers.insert(0,'수진')
# passengers.remove('민수')
# passengers.reverse()
# print(passengers)

# 실습3-2
list = [5,3,7]
list.extend([4,9])
print('max_list:', max(list))
print('min_list:', min(list))
print('sum_list:', sum(list))
list.sort()
list.pop()
print(list)