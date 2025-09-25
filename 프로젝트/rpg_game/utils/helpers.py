from rpg_game.characters import Warrior, Mage, Rogue

def choose_character(prompt="캐릭터를 선택하세요"):
    while True:
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