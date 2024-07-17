# [캐릭터]
# - 이름
# - 스킬 - DoubleAttack, Freeze 
# - 장비(착용부위) Weapon, Helmet, Chestplate, Gauntlets, Boots  
# - 레벨
# - hp 
# - mp 
# - 공격력
# - 물리방어력
# - 마법방어력
# - 우선순위(같으면랜덤)

import random

class Character:

    skill = ['DoubleAttack', 'Freeze']

    def __init__ (self, name):
        self.name = name
        self.skill = random.choice(self.skill)
        self.weapon = ''
        self.armor = []
        self.exp = 0
        self.level = 1
        self.hp = 10
        self.mp = 10
        self.power = 10
        self.physical_defence = 10
        self.magic_defence = 10
        print()
        print(f'{name} 캐릭터가 생성되었습니다')
        print(f'스킬은 {self.skill} 을 부여 받았습니다')
        print(f'캐릭터 레벨은 {self.level} 이며')
        print(f'기본 hp는 {self.hp} mp는 {self.mp}, 공격력은 {self.power} 물리방어력은 {self.physical_defence} 마법방어력은 {self.magic_defence} 입니다')

    # 무기착용
    # 방어구 착용
    # hp 변화
    # mp 변화
    # 경험치 변화
    # 공격력 변화
    # 물리 방어력 변화
    # 마법 방어력 변화