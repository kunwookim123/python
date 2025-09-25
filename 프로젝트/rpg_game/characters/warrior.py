from .character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격합니다!")
        target.take_damage(self.attack_power)

    def special_attack(self, target):
        print(f"{self.name}의 강력한 일격!")
        damage = self.attack_power * 2
        target.take_damage(damage)
        self.take_damage(5)