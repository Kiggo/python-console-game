from character import Character
from monster import Monster
from battle import Battle
import random

# 몬스터 인스턴스 생성 (2~5마리 랜덤)
monsters = [Monster() for _ in range(random.randint(2, 5))]
character = Character('dodo') 

# 전투
battle = Battle(character, monsters)
battle.start()