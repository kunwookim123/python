from .character import Character # character 파일에서 Character 클래스 import

class Warrior(Character): # 도적 기본 설정 - 부모 클래스 상속
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15) # 부모 클래스에서 생성자 호출

    def attack(self, target): # 기본 공격 설정
        print(f"{self.name}이(가) {target.name}을(를) 공격합니다!")
        target.take_damage(self.attack_power)

    def special_attack(self, target): # 특수 공격 설정
        print(f"{self.name}의 강력한 일격!")
        damage = self.attack_power * 2 # 특수 공격 성공시 2배 데미지를 입힘
        target.take_damage(damage)
        self.take_damage(5) # 특수 공격 부작용 - 체력 5 감소