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

    # 캐릭터가 몬스터를 공격하는 우선순위 -> type 의 index

    type = ['Slime', 'Pig', 'Mushroom', 'Ghost']

    drop_items = ['Helmet', 'Weapon', 'Chestplate', 'Gauntlets', 'Boots']


    def __init__(self):
        self.type = random.choice(self.type)
        self.power = 20
        self.hp = random.randrange(100,200)
        self.mp = 10
        self.physical_defence = 10
        self.magic_defence = 10
        self.exp = random.randrange(10,30)
        print()
        print(f'{self.type} 몬스터가 나타났습니다')

    def drop_item(self):
        return random.choice(self.drop_items)
    
    def attack(self, target):
        damage = random.randrange(self.power/2, self.power) - target.physical_defence  # 몬스터의 고정 데미지
        if damage > 0:
            target.hp -= damage
        print(f'{self.type}가 {target.name}에게 {damage}의 데미지를 입혔습니다. {target.name}의 남은 HP: {target.hp}')