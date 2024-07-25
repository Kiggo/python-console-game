# [몬스터] 
# - 종류
# - hp
# - mp
# - 물리방어력
# - 마법방어력
# - 드랍아이템
# - 경험치
# - 여러마리

import random

class Monster:

    type = [
        {'name':'Slime', 'hp':100, 'exp':10}, 
        {'name':'Pig', 'hp':200, 'exp':20}, 
        {'name':'Mushroom', 'hp':300, 'exp':30}, 
        {'name':'Ghost', 'hp':400, 'exp':40}
    ]
    drop_items = ['Helmet', 'Weapon', 'Chestplate', 'Gauntlets', 'Boots']

    def __init__(self):
        self.type = random.choice(self.type)
        # self.cnt = random.choice(self.cnt)
        self.power = 20
        self.hp = self.type['hp']
        self.mp = 10
        self.physical_defence = 10
        self.magic_defence = 10
        self.exp = self.type['exp']
        print()
        # print(f'{self.type["name"]} 몬스터 {self.cnt} 마리가 나타났습니다')


    def drop_item(self):
        return random.choice(self.drop_items)
    
    def attack(self, target):
        damage = random.randrange(self.power/2, self.power) - target.physical_defence  # 몬스터의 고정 데미지
        if damage > 0:
            target.hp -= damage
        print(f'{self.type["name"]}가 {target.name}에게 {damage}의 데미지를 입혔습니다. {target.name}의 남은 HP: {target.hp}')