# 정수 내림차순으로 만들기
# def solution(n):
#     return int(''.join(sorted(str(n), reverse = True)))

def solution(s):
    cnt_p = 0
    cnt_y = 0
    lower_s = s.lower()
    for i in lower_s:
        if i == 'p':
            cnt_p += 1
        elif i == 'y':
            cnt_y += 1
            if cnt_p == cnt_y:
                return True
            else:
                return False

print("pPoooyY")
print("Pyy")