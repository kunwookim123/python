from .character import Character # character 파일에서 Character 클래스 import

class Mage(Character): # 마법사 기본 설정 - 부모 클래스 상속
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=18) # 부모 클래스에서 생성자 호출
        self.mana = 100
    # 기본 공격 설정
    def attack(self, target):
        print(f"{self.name}이(가) 기본 공격을 합니다!")
        target.take_damage(self.attack_power)
    # 특수 공격 설정
    def special_attack(self, target):
        if self.mana < 20:
            raise Exception(f"{self.name}의 마나가 부족합니다!") # 예외 설정 - 마나 20 미만일 경우 예외에 해당
        self.mana -= 20 # 기본 마나 소비량 20
        damage = int(self.attack_power * 1.5)
        print(f"{self.name}의 파이어볼!")
        target.take_damage(damage)