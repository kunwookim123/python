import random # 랜덤 설정과 타임 설정을 위한 import 사용
import time

class BattleManager:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print('전투 시작!')
        time.sleep(1) # 일시정지 1초

        turn = random.choice([self.player, self.enemy]) # 랜덤으로 선공 결정
        print(f'선공은 {turn.name}입니다.')
        time.sleep(1) # 일시정지 1초

        while self.player.is_alive() and self.enemy.is_alive(): # 둘 중 죽을때까지 싸우도록 while문 실행
            attacker = turn # 위에서 결정된 선공자가 attacker
            defender = self.enemy if attacker == self.player else self.player

            action_type = random.choices(['attack','special_attack'], weights = [70,30]) [0] # 기본공격/특수공격 70:30 확률로 랜덤 설정

            try:
                if action_type == "attack":
                    attacker.attack(defender)
                else:
                    attacker.special_attack(defender)
            except Exception as e: # 예외 설정 - 특수 공격 실패시 기본 공격으로 전환되게끔
                print(e)
                print(f"{attacker.name}의 특수 공격 실패! 기본 공격으로 전환합니다.")
                attacker.attack(defender)

            time.sleep(1)

            if not defender.is_alive():
                print(f"{defender.name}이(가) 쓰러졌습니다!")
                break # 반복문 탈출

            turn = defender # while문을 defender 선공일 때도 적용

        winner = self.player if self.player.is_alive() else self.enemy
        print(f"\n{winner.name}의 승리!\n")