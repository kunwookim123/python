# # 실습1
# # step1
# user = ('minji', 25, 'seoul')
# user1 = list(user)
# user1[0] = 'eunji'
# restored_user = tuple(user1)
# print('restored_user:', restored_user)

# # step2
# restored_user = ('eunji', 25, 'seoul')
# name, age, city = restored_user
# print(f'name: {name}, age: {age}, city: {city}')

# # step3
# if city == 'seoul':
#     print('*서울 지역 보안 정책 적용 대상입니다.')
# else:
#     print('*일반 지역 보안 정책 적용 대상입니다.')

# # step4
# users = ('minji', 'eunji', 'soojin', 'minji', 'minji')
# count_minji = users.count('minji')
# print(f'minji 등장 횟수:', count_minji)
# index_soojin = users.index('soojin')
# print(f'soojin이 처음 등장하는 인덱스:', index_soojin)

# # step5
# sorted_users = sorted(users)
# print('고객 이름 가나다순:', sorted_users)

# 실습2
# 문제1
# submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
# set_submissinos = {'kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee'}
# print('제출한 학생 수: ',len(set_submissinos))
# print('제출자 명단:',set_submissinos)


# 문제2
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}
print(f'공통 관심 장르: {user1 & user2} \n서로 다른 장르: {user1 ^ user2} \n전체 장르: {user1|user2}')

# 문제3
my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}
print('지원 자격 충족 여부:', my_certificates >= job_required)