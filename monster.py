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

    type = ['Slime', 'Pig', 'Mushroom', 'Ghost']
    cnt = [1, 2, 3, 4, 5]
    drop_item = ['Helmet', 'Weapon', 'Chestplate', 'Gauntlets', 'Boots']
    exp = [10, 20, 30]

    def __init__(self):
        self.type = random.choice(self.type)
        self.cnt = random.choice(self.cnt)
        self.hp = 10
        self.mp = 10
        self.physical_defence = 10
        self.magic_defence = 10
        self.exp = random.choice(self.exp)
        print(f'{self.type} 몬스터 {self.cnt} 마리가 나타났다')


    def dead(self):
        drop_item = random.choice(self.drop_item)
        exp = self.exp
        return print(f'몬스터를 잡고 {drop_item} 아이템과 {exp} 경험치를 얻었다')