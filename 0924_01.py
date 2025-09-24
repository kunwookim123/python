# # 파일 입출력

# '''
#     파일 입출력(File I/O)은 프로그램이 파일을 읽고(input) 쓰는(output) 작업
#     프로그램이 종료되어도 데이터를 보관할 수 있는 유일한 방법
#     프로그램의 데이터는 메모리에 저장되는데 프로그램이 종료되면 메모리의 데이터는 사라짐
#     파일로 저장하면 하드디스크에 영구 보관됨
# '''


# # 파일 입출력이 필요한 상황
# '''
#     1. 설정 파일 저장 : 게임 설정, 프로그램 옵션
#     2. 데이터 백업 : 중요한 정보 보관
#     3. 로그 기록 : 프로그램 실행 기록, 에러 추적
#     4. 데이터 교화 : 엑셀, csv 파일로 다른 프로그램과 데이터 공유
#     5. 대용량 처리 : 메모리에 다 못 담는 빅데이터 처리
# '''

# # 위험한 방법 why? 파일을 안닫을 수 있기 때문
# # 1단계 - 파일 열기(open) : 파일과 연결 통로 생성
# file = open('data.txt', 'r', encoding = 'utf-8')

# # 2단계 - 파일 작업(Read/Write) : 데이터 읽기/쓰기
# content = file.read()
# print(content)

# # 3단계 - 파일 닫기(Close) : 연결 종료 (중요!!)
# file.close()

# # 안전한 방법 - with 문
# with open('data.txt', 'r', encoding = 'utf-8') as f:
#     content = f.read()
#     print(content)

# # with를 쓰는 이유 - 자동으로 close()를 수행하기 때문

# # 새 파일 생성 또는 덮어쓰기
# with open('output.txt', 'w', encoding = 'utf - 8') as f:
#     f.write('hello, world\n')
#     f.write('파이썬 파일 입출력\n')

# with open('output.txt', 'a', encoding = 'utf - 8') as f:
#     f.write('추가된 내용\n')
    
# # 1. read() - 파일 전체를 하나의 문자열로
# # 메모리 비효율적
# with open('data.txt', 'r', encoding = 'utf - 8') as f:
#     content = f.read()
#     print(content) # 메모리가 10GB라면 그대로 10GB 다 사용

# # read(크기) - 저장한 크기만큼만
# with open('data.txt', 'r', encoding = 'utf-8') as f:
#     print(f'처음 위치: {f.tell()}') # 일반적으로 0이 나옴
#     content = f.read(3) # 3(크기)만큼만
#     print(content)
#     print(f'3바이트를 읽은 후 위치: {f.tell()}') # 일반적으로 0이 나옴

# print()

# # 2. readline() - 한 줄씩 읽기
# # 메모리 효율적 - 한 줄씩 처리
# print('2. readline() - 한 줄씩 읽기')
# with open('data.txt', 'r', encoding = 'utf-8') as f:
#     print(f'처음 위치: {f.tell()}')
#     line1 = f.readline()
#     print(line1.strip()) # 공백, 탭(\t), 줄바꿈(\n) 양쪽 제거
#     print(f'첫번째 줄 읽은 후 위치: {f.tell()}')
#     line2 = f.readline()
#     print(line2.strip())
#     print(f'두번째 줄 읽은 후 위치: {f.tell()}')
#     f.seek(0) # 포인터를 처음으로
#     line3 = f.readline()
#     print(line3.strip())
#     print(f'세번째 줄 읽은 후 위치: {f.tell()}')

# # readline() - for문
# with open('data.txt', 'r', encoding = 'utf-8') as f:
#     for line in f: # 한 줄씩만 메모리에 사용
#         print(line.strip())
# print()

# # 3. readlines()
# print('3. readline()')

# with open('data.txt', 'r', encoding = 'utf-8') as f:
#     lines = f.readlines() # ['첫줄\n','둘째줄\n','셋째줄\n']

#     for line in lines:
#         print(line.strip())

# print()

# 바이너리
# with open('airplane.jpg', 'rb') as f1:
#     img = f1.read()

# with open('./airplane_copy.jpg', 'wb') as f2:
#     f2.write(img)

