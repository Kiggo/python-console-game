from character import Character
from monster import Monster
from battle import Battle

# 어떤 몬스터를 만나는건 랜덤
# 몬스터 인스턴스 생성 

monster = Monster()
character = Character('momo') 

# 4. 전투
battle = Battle(character, monster)
battle.start()
battle.join()