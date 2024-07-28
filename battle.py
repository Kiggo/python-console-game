import threading
import time
import json

class Battle:
    def __init__(self, character, monsters):
        self.character = character
        self.monsters = monsters
        self.threads = []
        self.character_alive = True
        self.lock = threading.Lock()  # Add a lock to synchronize access

    def save_character(self):
        with open('./save.json', 'r') as save_json:
            json_data = json.load(save_json)

        for character in json_data['character']:
            if self.character.name == character['name']:
                character['hp'] = self.character.max_hp
                character['mp'] = self.character.max_mp
                character['max_hp'] = self.character.max_hp
                character['max_mp'] = self.character.max_mp
                character['power'] = self.character.power
                character['exp'] = self.character.exp
                character['level'] = self.character.level
                character['items'] = self.character.items
                break

        with open('./save.json', 'w') as save_json:
            json.dump(json_data, save_json, indent=4)
        print(f'{self.character.name}의 정보가 저장되었습니다.')

    def battle_with_monster(self, monster):
        while self.character.hp > 0 and monster.hp > 0 and self.character_alive:
            self.character.attack(monster)
            if monster.hp <= 0:
                print(f'{monster.type}를 물리쳤습니다!')
                item = monster.drop_item()
                exp = monster.exp
                self.character.exp += exp
                if self.character.exp >= 100:
                    self.character.level_up()
                if item not in self.character.items:
                    self.character.items.append(item)
                print(f'{monster.type}를 물리치고 {item} 아이템과 {exp} 경험치를 얻었습니다. 현재 경험치는 {self.character.exp} 입니다.')
                self.save_character()  # 캐릭터 정보를 저장
                break
            
            time.sleep(0.5)  # 캐릭터의 공격 텀

    def monster_attack(self, monster):
        while self.character.hp > 0 and monster.hp > 0 and self.character_alive:
            monster.attack(self.character)
            if self.character.hp <= 0:
                with self.lock:
                    if self.character_alive:
                        print(f'{self.character.name}가 쓰러졌습니다.')
                        self.character_alive = False
                break
            
            time.sleep(0.5)  # 몬스터의 공격 텀

    def start_battle(self):
        for monster in self.monsters:
            thread = threading.Thread(target=self.monster_attack, args=(monster,))
            self.threads.append(thread)
            thread.start()

        for monster in self.monsters:
            self.battle_with_monster(monster)
            if not self.character_alive:
                break

        for thread in self.threads:
            thread.join()


    def start(self):
        self.start_battle()  # 전투시작
        