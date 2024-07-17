from character import Character
from monster import Monster
import json

# 쓰레드를 사용 해야 함

# 1. 캐릭터 생성 - 사용자 입력
character_name = input('\n캐릭터명을 입력하세요\n')
character = Character(character_name)

# 2. 정보 save.json에 저장
file_path = './save.json'
with open (file_path, 'w')as json_file:
    json.dump(character, json_file)

# 3. 마을 또는 사냥터 이동


# 어떤 몬스터를 만나는건 랜덤
monster = Monster()

# 4. 전투
# 몬스터 사망
monster.dead()