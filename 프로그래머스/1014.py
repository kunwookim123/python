# 시저암호

def solution(s, n):
    answer = ''
    for ch in s:
        if ch.isupper(): # 대문자 처리
            answer += chr(((ord(ch) - ord('A')) + n) % 26 + ord('A')) # n만큼 이동
        elif ch.islower(): # 소문자 처리
            answer += chr(((ord(ch) - ord('a')) + n) % 26 + ord('a')) # n만큼 이동
        else:
            answer += ch # 공백은 그대로
    return answer

# 이상한 문자 만들기

def solution(s):
    words=s.split(" ")
    result = []
    
    for word in words:
        new_word = ""
        for i in range(len(word)):
            if i%2==0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        result.append(new_word)
    return ' '.join(result)

# 가장 가까운 같은 문자

def solution(s):
    char_index = {}                              # 문자의 마지막 위치 저장
    answer = []
    
    for i, char in enumerate(s):
        if char in char_index:
            answer.append(i - char_index[char])  # 거리 계산
        else:
            answer.append(-1)                    # 처음 나온 문자
        char_index[char] = i                     # 현재 위치 저장
    
    return answer