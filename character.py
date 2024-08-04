import random
import time

class Character:

    skill_set = {'double_attack': 20, 'fireball': 25, 'power_slash': 30}

    def __init__ (self, name):
        self.name = name
        self.skill = random.choice(list(self.skill_set.keys()))
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
        self.location = 'Town'
        self.skill_cooldown = 0
        self.last_skill_time = 0
        
    def character_state(self):
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
            'exp': self.exp,
            'location': self.location,
            }
        return obj
    
    def attack(self, target):
        damage = random.randrange(self.power / 2, self.power) - target.physical_defence
        current_time = time.time()
        if current_time - self.last_skill_time < self.skill_cooldown:
            remaining_cooldown = self.skill_cooldown - (current_time - self.last_skill_time)
            print(f'{self.name}의 스킬이 쿨타임 중입니다. 남은 쿨타임: {remaining_cooldown:.2f}초')
            # 일반공격
            target.hp -= damage
            print(f'{self.name}가 {target.type}에게 {damage}의 데미지를 입혔습니다. {target.type}의 남은 HP: {target.hp}\n')
            return  # 쿨타임 중이면 스킬 사용 불가
        
        if damage > 0 and self.mp >= self.skill_set[self.skill]:
            print(f'스킬공격 {self.skill}')
            self.mp -= self.skill_set[self.skill]
            target.hp -= (damage + self.skill_set[self.skill])
            self.last_skill_time  = current_time
            self.skill_cooldown = 5
            print(f'{self.name}가 {target.type}에게 {self.skill} 스킬을 이용하여 {(damage + self.skill_set[self.skill])}의 데미지를 입혔습니다. {target.type}의 남은 HP: {target.hp}\n')
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
        self.physical_defence += 1
        self.magic_defence += 1
        if self.exp >= 100:
            self.exp = 0
        print(f'{self.name}가 레벨업 했습니다!!!')

    def equip_item(self, item):
        self.equipment.append(item)
        print(f'{self.name}가 {item}을 착용했습니다.')

    def recover_mp(self):
        while self.hp > 0 and self.location == 'Dungeon':  
            self.mp = min(self.max_mp, self.mp + 1) 
            print(f'전투중 {self.name} 의 MP가 회복되었습니다. 현재 MP: {self.mp}')
            print()
            time.sleep(1)
    
    def enter_town(self):
        if self.location != 'Town':
            self.location = 'Town'
            self.hp = self.max_hp
            self.mp = self.max_mp
            print(f'{self.name}가 마을에 도착했습니다. hp 회복 {self.hp} mp 회복 {self.mp}.')

    def enter_dungeon(self):
        if self.location != 'Dungeon':
            self.location = 'Dungeon'
            print(f'{self.name}가 던전에 들어갔습니다.')

