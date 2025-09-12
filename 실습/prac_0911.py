# # 실습2
# # intro = "두둠칫"
# # drop = '둠칫'

# # print(intro + drop * 2 + intro)

# # 실습3
# # name, age = input('이름과 나이를 입력하세요.').split()
# # print(f'안녕하세요. 저는 {name} 이고, {age}살입니다.')

# # 실습4
# # 4-1
# # width = int(input('가로 길이:'))
# # height = int(input('세로 길이:'))
# # print(f'넓이: {width*height}')
# # print(f'둘레: {(height+width)*2}')

# # 4-2
# # num = int(input("네자리 정수 입력"))
# # thousand = num // 1000
# # hundred = (num % 1000) // 100
# # ten = (num % 100) // 10
# # one = num % 10
# # print("천의 자리:", thousand)
# # print("백의 자리:", hundred)
# # print("십의 자리:", ten)
# # print("일의 자리:", one)

# # 실습5
# # name1, name2, name3 = input().split()
# # topic1, topic2, topic3 = input().split()
# # print(f'1조 발표자: {name1} - 주제: {topic1}')
# # print(f'2조 발표자: {name2} - 주제: {topic2}')
# # print(f'3조 발표자: {name3} - 주제: {topic3}')

# # 실습6
# # year, month, day = input().split('.')
# # hour, minute, second = input().split(':')
# # print(f'RE4의 개강일은 {year}년 {month}월 {day}일')
# # print(f'시작 시간은 {hour}시 {minute}분 {second}초 입니다.')

# # 실습1

# weather = input('오늘 날씨를 입력하세요')
# if weather == '비':
#     print('우산을 챙기세요.')
# if weather == '맑음':
#     print('선크림을 챙기세요.')

# 실습2
# num = int(input('정수를 입력해주세요.'))
# if num % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# 실습3
# age = int(input('나이를 입력하세요.'))
# if age >= 19:
#     print('청소년 관람불가 가능')
# elif age >= 16:
#     print('15세 이상 관람가')
# elif age >= 13:
#     print('12세 이상 관람가')
# else:
#     print('전체 관람가')

# 실습4
# second = int(input('초를 입력해주세요.'))

# if second >= 3600:
#     print(f'{second // 3600}시간', end=" ")

# second %= 3600

# if second >= 60:
#     print(f'{second // 60}분', end=" ")

# second %= 60

# print(f'{second}초')

# 실습5
# 김밥 = 2500
# 삼각김밥 = 1500
# 도시락 = 4000
# money = int(input('금액을 입력하세요.'))
# food = input('식품명을 입력하세요.')
# if food == '도시락':
#     if money >=4000:
#         print('구매 성공')
#     else:
#         print('금액이 부족합니다.')
# elif food == '김밥':
#     if money >=2500:
#         print('구매 성공')
#     else:
#         print('금액이 부족합니다.')
# else:
#     if food == '삼각김밥':
#         if money >= 1500:
#             print('구매 성공')
#         else:
#             print('금액이 부족합니다.')

