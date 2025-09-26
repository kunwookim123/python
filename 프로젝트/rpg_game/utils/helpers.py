from characters import Warrior, Mage, Rogue        # __init__을 통한 패키지로 묶인 함수 사용

def choose_character(prompt="캐릭터를 선택하세요"):
    while True:                                             # while문 무한 루프
        print(f"{prompt}: 1) 전사 2) 마법사 3) 도적")
        choice = input("번호 입력: ")
        name = input("캐릭터 이름 입력: ")

        if choice == '1':
            return Warrior(name)
        elif choice == '2':
            return Mage(name)
        elif choice == '3':
            return Rogue(name)
        else:
            print("잘못된 선택입니다. 다시 시도하세요.\n")