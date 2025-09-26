from utils.helpers import choose_character         # __init__을 통한 패키지로 묶인 함수 사용
from battle.battle_manager import BattleManager

def main():
    print("=== RPG 전투 게임 ===")
    player = choose_character("당신의 캐릭터를 선택하세요")

    while True:                                             # 전투 반복 실행
        enemy = choose_character("상대 캐릭터를 선택하세요")
        player.reset_health()
        enemy.reset_health()

        battle = BattleManager(player, enemy)               # battle_manager 파일에서 BattleManager 클래스 import
        battle.start_battle()

        if not player.is_alive():                           # 플레이어 사망
            print("게임 오버! 당신은 패배했습니다.")
            break                                           # 반복문 탈출

        again = input("계속 전투를 하시겠습니까? (y/n): ")     # 전투 완료후 플레이어 승리시 실행
        if again.lower() != 'y':
            print("게임을 종료합니다.")                       # 'n' 입력시 실행
            break                                           # 반복문 탈출

if __name__ == "__main__": # 'main'함수 호출
    main()