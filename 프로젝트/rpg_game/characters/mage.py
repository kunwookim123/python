from .character import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=18)
        self.mana = 100

    def attack(self, target):
        print(f"{self.name}이(가) 기본 공격을 합니다!")
        target.take_damage(self.attack_power)

    def special_attack(self, target):
        if self.mana < 20:
            raise Exception(f"{self.name}의 마나가 부족합니다!")
        self.mana -= 20
        damage = int(self.attack_power * 1.5)
        print(f"{self.name}의 파이어볼!")
        target.take_damage(damage)