# stack 문제

def solution(s):
    stack = 0
    for ch in s:
        if ch == '(':
            stack += 1
        else: # ch == ')'
            if stack == 0: # 닫는게 없는데 ')'가 나오면 잘못되었다 판단
                return False
            stack -= 1

    return stack == 0 # 남아있는 '('가 있으면 안됨. 모두 짝이 맞아야 올바른 괄호