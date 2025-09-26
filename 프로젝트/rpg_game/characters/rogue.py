import random
from .character import Character # character 파일에서 Character 클래스 import

class Rogue(Character): # 도적 기본 설정 - 부모 클래스 상속
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=12) # 부모 클래스에서 생성자 호출

    def attack(self, target):
        print(f"{self.name}이(가) 기본 공격을 합니다!")
        target.take_damage(self.attack_power)

    def special_attack(self, target):
        print(f"{self.name}의 급습!")
        if random.random() < 0.7: # 특수 공격 랜덤 설정 - 70% 확률로 특수 공격 성공, 성공시 기본 공격력의 3배 데미지를 입힘
            damage = self.attack_power * 3
            print("급습 성공!")
            target.take_damage(damage)
        else:
            print("급습 실패!") # 실패시 - 데미지가 들어가지 않음