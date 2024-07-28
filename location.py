class Location_State:
    def __init__(self, character):
        self.character = character
        self.state = 'Town'  # 초기 상태는 마을

    def enter_town(self):
        if self.state != 'Town':
            self.state = 'Town'
            self.character.hp = self.character.max_hp
            self.character.mp = self.character.max_mp
            print(f'{self.character.name}가 마을에 도착했습니다. hp 회복 {self.character.hp} mp 회복 {self.character.mp}.')

    def enter_dungeon(self):
        if self.state != 'Dungeon':
            self.state = 'Dungeon'
            print(f'{self.character.name}가 던전에 들어갔습니다.')
            
