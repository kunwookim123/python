from characters import Warrior, Mage, Rogue  # characters 파일에서 직업 클래스 import

def choose_character(prompt="캐릭터를 선택하세요"):
    while True:                                             # while문 무한 루프 - 잘못 입력시 재선택을 하기 위해서 설정
        print(f"{prompt}: 1) 전사 2) 마법사 3) 도적")
        choice = input("번호 입력: ")
        name = input("캐릭터 이름 입력: ")

        if choice == '1':
            return Warrior(name) # 1번 입력시 전사 선택을 하게 됨
        elif choice == '2':
            return Mage(name) # 2번 입력시 마법사 선택을 하게 됨
        elif choice == '3':
            return Rogue(name) # 3번 입력시 도적 선택을 하게 됨
        else:
            print("잘못된 선택입니다. 다시 시도하세요.\n") # 1,2,3 외 다른 것을 입력시 무한 루프 실행