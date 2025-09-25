import random
from .character import Character

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=12)

    def attack(self, target):
        print(f"{self.name}이(가) 기본 공격을 합니다!")
        target.take_damage(self.attack_power)

    def special_attack(self, target):
        print(f"{self.name}의 급습!")
        if random.random() < 0.7:
            damage = self.attack_power * 3
            print("급습 성공!")
            target.take_damage(damage)
        else:
            print("급습 실패!")