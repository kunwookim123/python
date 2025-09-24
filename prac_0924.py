# 문제1
def get_age_group():
    try:
        age = int(input('나이를 입력하세요.'))
    except ValueError:
        print('숫자로 입력해주세요.')
        age = int(input('나이를  입력해주세요.'))
    if 0 <= age < 20:
        print('미성년자')
    elif 20<= age <40:
        print('청년')
    elif 40<= age < 60:
        print('중년')
    elif 60<= age < 150:
        print('노년')
    else:
        print('에러')


get_age_group()
