'''
    특징
    1. 양방향 연산
        앞쪽 뒤쪽 모두에서 요소의 추가, 제거가 가능
    2. 시간 복잡도
        양쪽 끝에서의 모든 연산이 상수 시간에 수행
    3. 동적 크기
        필요에 따라 크기가 자동으로 조절
    4. 스택과 큐 동시 구현
        하나의 자료구조로 스택과 큐를 모두 구현
    5. 회전 연산 지원
        요소들을 좌우로 회전시킬 수 있음 
'''

'''
    주요 연산
    append(x)               오른쪽 끝에 요소 추가
    appendleft(x)           왼쪽 끝에 요소 추가

    pop()                   오른쪽 끝 요소 제거 및 반환
    popleft()               왼쪽 끝 요소 제거 및 반환

    extend(iterable)        오른쪽에 여러 요소 추가
    extendleft(iterable)    왼쪽에 여러 요소 추가

    rotate(n)               n만큼 회전
    clear()                 모든 요소 제거
'''
from collections import deque
'''
    회문 검사
    level - > 앞 뒤가 똑같은 것: 회문
'''
def is_palindrome(s):
    '''
        덱을 이용한 회문 검사
    '''
    dq = deque(s)

    while len(dq) > 1:
        left_ch = dq.popleft()
        right_ch = dq.pop()
        if left_ch != right_ch:
            return False
    return True
        
print(is_palindrome('level')) # True
print(is_palindrome('tomato')) # False


