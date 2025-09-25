from rpg_game.utils.helpers import choose_character
from rpg_game.battle.battle_manager import BattleManager

def main():
    print("=== RPG 전투 게임 ===")
    player = choose_character("당신의 캐릭터를 선택하세요")

    while True:
        enemy = choose_character("상대 캐릭터를 선택하세요")
        player.reset_health()
        enemy.reset_health()

        battle = BattleManager(player, enemy)
        battle.start_battle()

        if not player.is_alive():
            print("게임 오버! 당신은 패배했습니다.")
            break

        again = input("계속 전투를 하시겠습니까? (y/n): ")
        if again.lower() != 'y':
            print("게임을 종료합니다.")
            break

if __name__ == "__main__":
    main()