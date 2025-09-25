import random
import time

class BattleManager:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print('전투 시작!')
        time.sleep(1)

        turn = random.choice([self.player, self.enemy])
        print(f'선공은 {turn.name}입니다.')
        time.sleep(1)

        while self.player.is_alive() and self.enemy.is_alive():
            attacker = turn
            defender = self.enemy if attacker == self.player else self.player

            action_type = random.choices(['attack','special_attack'], weights = [70,30]) [0]

            try:
                if action_type == "attack":
                    attacker.attack(defender)
                else:
                    attacker.special_attack(defender)
            except Exception as e:
                print(e)
                print(f"{attacker.name}의 특수 공격 실패! 기본 공격으로 전환합니다.")
                attacker.attack(defender)

            time.sleep(1)

            if not defender.is_alive():
                print(f"{defender.name}이(가) 쓰러졌습니다!")
                break

            turn = defender

        winner = self.player if self.player.is_alive() else self.enemy
        print(f"\n{winner.name}의 승리!\n")