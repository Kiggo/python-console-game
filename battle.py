# - 전투(공격의 결과값)ex.15~18 random (자동전투)
import threading
import time

class Battle:
    def __init__(self, character, monsters):
        self.character = character
        self.monsters = monsters
        self.threads = []
        self.battle_active = True

    def battle_with_monster(self, monster):
        while self.character.hp > 0 and monster.hp > 0 and self.battle_active:
            self.character.attack(monster)
            if monster.hp <= 0:
                print(f'{monster.type}를 물리쳤습니다!')
                item = monster.drop_item()
                exp = monster.exp
                self.character.exp += exp
                print(f'{monster.type}를 물리치고 {item} 아이템과 {exp} 경험치를 얻었습니다.')
                break
            monster.attack(self.character)
            if self.character.hp <= 0:
                if self.battle_active:  # Ensure the message is printed only once
                    print(f'{self.character.name}가 쓰러졌습니다.')
                    self.battle_active = False
                break

    def start_battle(self):
        for monster in self.monsters:
            thread = threading.Thread(target=self.battle_with_monster, args=(monster,))
            self.threads.append(thread)
            thread.start()

    def start(self):
        self.start_battle() # 전투시작

    def join(self):
        for thread in self.threads:
            thread.join() # 모든 전투 쓰레드가 끝날때까지 기다림
        if self.character.hp > 0:
            print("모든 몬스터를 쓰러트렸습니다!")
        else:
            self.battle_active = False  # Ensure all threads stop if character is down