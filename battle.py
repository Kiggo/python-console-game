# - 전투(공격의 결과값)ex.15~18 random (자동전투)
import threading
import time

class Battle:
    def __init__(self, character, monster):
        self.character = character
        self.monster = monster
        self.thread = threading.Thread(target=self.start_battle)

    def start_battle(self):
        while self.character.hp > 0 and self.monster.hp > 0:
            self.character.attack(self.monster)
            if self.monster.hp <= 0:
                print(f'{self.monster.type["name"]}를 물리쳤습니다!')
                item = self.monster.drop_item()
                exp = self.monster.exp
                self.character.exp += exp
                print(f'{self.monster.type["name"]}를 물리치고 {item} 아이템과 {exp} 경험치를 얻었습니다.')
                break
            self.monster.attack(self.character)
            if self.character.hp <= 0:
                print(f'{self.character.name}가 쓰러졌습니다.')
                break
            time.sleep(1)

    def start(self):
        self.thread.start() # 전투시작

    def join(self):
        self.thread.join() # 전투 쓰레드가 끝날때까지 기다림