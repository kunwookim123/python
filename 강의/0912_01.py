# 리스트
# list1 = list()
# list2 = list('hello')


#  H  E  L  L  O
#  0  1  2  3  4
# -5 -4 -2 -2 -1
# print(list1)
# print(list2)

# print('인덱스0: ', list2[0])
# print('인덱스3: ', list2[3])
# print('인덱스4: ', list2[4])

# list2[4] = 'a'
# print(list2)

# text = 'python'
# text[1] = 'a' # list가 아니기때문에 문자열 변환 불가
# print('text', text)

# list3 = list('python')
# text3 = 'hello'
# print('list3[:]', list3[:])
# print('text3[:3]',text3[:3])
# print('text3[2:4]',text3[2:4])
# print('text3[-3:-1]',text3[-3:-1])

# print('text3[::-1]', text3[::-1]) # 문자열 뒤집기
# print('text3[::-2]', text3[::-2])
# print('text3[:-4:-2]', text3[:-4:-2])

# [10,20,30,40]
#    0  1  2  3

# numbers = [10,20,30,40]
# print('numbers[1:3]', numbers[1:3])
# print('numbers[:3:2]', numbers[:3:2])
# print('numbers 뒤집기', numbers[::-1])

# # [10,40,20,40]
# print('numbers[1:3]', numbers[1:3])
# print('1. numbers', numbers)

# del
# list1 = [10,20,30,40,50]

# # 3 index 요소를 삭제
# del list1[3]
# print(list1)

# del list1[1:3]
# print(list1)

# del list1
# print(list1)

# list1 = [1,2,3,4,5]
# list2 = [2,3,4,5]

# result = list1 + list2
# print(result)

# result = list1 * 3
# print(result)

# print('1' in list1) # false

#요소 추가 메서드
# numbers = [10,20,30,40,50]

# numbers.append(20)
# print(numbers)

# numbers.append(12)
# print(numbers)

# numbers.append([1,2,3])
# print(numbers)

# numbers.extend([19])
# print(numbers)

# numbers.extend([5, 29])
# print(numbers)

# numbers.insert(2, 22)
# print(numbers)

# list2 = [6,7,8]
# numbers.extend(list2)
# print(numbers)

# append, extend 차이점
# append - 리스트 자체가 추가됨
# extend - 요소들이 추가됨

# 요소 삭제 메서드
# fruits = ['사과', '바나나', '오렌지', '바나나', '포도']
# fruits.remove('바나나')
# print(fruits)

# removed = fruits.pop()
# print(removed)

# removed = fruits.pop(1)
# print(removed)
# print(fruits)

# fruits.clear() # 모든 요소 제거
# print(fruits)

# 요소 검색, 정렬 메서드
numbers = [1,2,6,9,5,3,2,4,7]

idx = numbers.index(6) #자리찾기
print('idx: ', idx)

idx = numbers.index(9)
print('idx: ', idx)

count = numbers.count(2)
print('count: ', count)

numbers.sort() #오름차순
print('numbers:', numbers)

numbers.sort(reverse = True) #내림차순
print('numbers:', numbers)

# sorted
original = [3,2,5,7,1]
sorted_list = sorted(original)


print('original:', original)
print('sorted_list:', sorted_list)


# 연산 메서드
numbers = [5,2,7,3,11,45]
max_num = max(numbers)
min_num = min(numbers)

print('max_num:', max(numbers))
print('min_num:', min(numbers))