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
    cnt = [1, 2, 3, 4, 5]
    drop_item = ['Helmet', 'Weapon', 'Chestplate', 'Gauntlets', 'Boots']

    def __init__(self):
        self.type = random.choice(self.type)
        self.cnt = random.choice(self.cnt)
        self.hp = self.type['hp']
        self.mp = 10
        self.physical_defence = 10
        self.magic_defence = 10
        self.exp = self.type['exp']
        print()
        print(f'{self.type["name"]} 몬스터 {self.cnt} 마리가 나타났습니다')


    def dead(self):
        drop_item = random.choice(self.drop_item)
        exp = self.exp * self.cnt
        return print(f'몬스터를 잡고 {drop_item} 아이템과 {exp} 경험치를 얻었습니다')