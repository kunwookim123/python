from abc import ABC, abstractmethod # 추상 메서드 

class Character: # 캐릭터 기본 설정
    def __init__(self, name, level = 1, health = 100, attack_power = 10):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    @abstractmethod # 자식 클래스에서 설정 예정
    def attack(self, target):
        pass

    @abstractmethod # 자식 클래스에서 설정 예정
    def special_attack(self,target):
        pass

    def take_damage(self, damage): # 받은 데미지
        self.health = max(0, self.health - damage)
        print(f'{self.name}이(가) {damage}만큼 피해를 입었습니다. 남은 체력: {self.health}')
        

    def is_alive(self): # 생존 여부
        return self.health > 0
    
    def show_status(self): # 캐릭터 상태
        print(f'캐릭터 이름: {self.name}, 레벨: {self.level}, 체력: {self.health} / {self.max_health}, 공격력: {self.attack_power}')

    def reset_health(self): # 체력 초기화
        self.health = self.max_health

    def get_name(self): # 캐릭터 이름을 가져옴
        return self.name
    
