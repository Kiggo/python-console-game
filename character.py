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
import time

class Character:

    skill = ['double_attack', 'fireball', 'power_slash']

    def __init__ (self, name):
        self.name = name
        self.skill = random.choice(self.skill)
        self.equipment = []
        self.items = []
        self.exp = 0
        self.level = 1
        self.hp = 300
        self.mp = 50
        self.max_hp = self.hp
        self.max_mp = self.mp
        self.power = 20
        self.physical_defence = 10
        self.magic_defence = 10
        
    def state(self):
        obj =  {
            'name': self.name,
            'skill': self.skill,
            'equipment': [],
            'items': [],
            'level': self.level,
            'hp': self.hp,
            'mp': self.mp,
            'max_hp': self.hp,
            'max_mp' : self.mp,
            'power': self.power,
            'physical_defence': self.physical_defence,
            'magic_defence': self.magic_defence,
            'exp': self.exp
            }
        return obj
    
    def attack(self, target):
        damage = random.randrange(self.power / 2, self.power) - target.physical_defence
        if damage > 0 and self.mp >= 20:
            print(f'스킬공격 {self.skill}')
            self.mp -= 20
            target.hp -= damage * 2
        else:
            target.hp -= damage
        print(f'{self.name}가 {target.type}에게 {damage}의 데미지를 입혔습니다. {target.type}의 남은 HP: {target.hp}\n')

    def level_up(self):
        self.level += 1
        self.max_hp += 100
        self.max_mp += 100
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.power += 10
        self.physical_defence += 5
        self.magic_defence += 5
        if self.exp >= 100:
            self.exp = 0
        print(f'{self.name}가 레벨업 했습니다!!!')

    def equip_item(self, item):
        self.equipment.append(item)
        print(f'{self.name}가 {item}을 착용했습니다.')

    def recover_mp(self, amount):
        for _ in range(amount):  # 회복할 양만큼 반복
            self.mp = min(self.max_mp, self.mp + 1)  # 1씩 회복
            print(f'{self.name}의 MP가 회복되었습니다. 현재 MP: {self.mp}')
            time.sleep(1)  # 1초 대기

    # 무기착용
    # 방어구 착용
    # hp 변화
    # mp 변화
    # 경험치 변화
    # 공격력 변화
    # 물리 방어력 변화
    # 마법 방어력 변화