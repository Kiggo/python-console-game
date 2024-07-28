from character import Character
from monster import Monster
from battle import Battle
from account import Account
from location import Location_State
import random
import json

# 로그인 상태
login_state = False

while True:
    # 로그인
    account_question = input('\n로그인할 계정이 있으신가요? ... input (y/n)\n')
    
    if account_question == 'y':
        id = input('\n아이디를 입력하세요\n')
        pw = input('\n비밀번호를 입력하세요\n')

        # json 파일을 읽어서 아이디 비밀번호 확인
        with open('./save.json', 'r') as save_json:
            json_data = json.load(save_json)
            if json_data['account']['id'] == id and json_data['account']['pw'] == pw:
                print()
                print('로그인 성공.')
                login_state = True
                break
            else:
                # 계정 정보 불일치
                print('일치하는 계정 정보가 없습니다 다시 입력해주세요.')
                continue

    elif account_question == 'n':
        # 계정 생성
        print('계정 생성을 시작합니다.')
        id = input('\n새로 등록할 아이디를 입력하세요\n')
        pw = input('\n새로 등록할 비밀번호를 입력하세요\n')
        account = Account(id, pw)
        account.sign_in()
        login_state = True
        break

    else:
        continue


# 로그인한 상태
if login_state:

    select_character = None

    # 계정에 캐릭터가 있는지 확인
    with open('./save.json', 'r') as save_json:
        json_data = json.load(save_json)
        if json_data['character']:
            for character in json_data['character']:
                print(f'{character["name"]}의 캐릭터가 존재합니다.')

            character_name = input('\n접속할 캐릭터명을 입력하세요\n')

            for character in json_data['character']:
                if character['name'] == character_name:
                    # 캐릭터 객체 생성
                    select_character = Character(name=character['name'])
                    select_character.skill = character['skill']
                    select_character.level = character['level']
                    select_character.hp = character['hp']
                    select_character.mp = character['mp']
                    select_character.power = character['power']
                    select_character.physical_defence = character['physical_defence']
                    select_character.magic_defence = character['magic_defence']
                    select_character.exp = character['exp']
                    select_character.max_hp = character['max_hp']
                    select_character.max_mp = character['max_mp']
                    select_character.equipment = character['equipment']
                    select_character.items = character['items']
                    
                    print(f'{character["name"]} 캐릭터 정보를 가져옵니다.')
                    print(f'스킬은 {character["skill"]} 을 부여 받았습니다')
                    print(f'캐릭터 레벨은 {character["level"]} 이며')
                    print(f'hp는 {character["hp"]} mp는 {character["mp"]}, 공격력은 {character["power"]} 물리방어력은 {character["physical_defence"]} 마법방어력은 {character["magic_defence"]} 경험치는 {character["exp"]}입니다')
        else:
            # 계정에 캐릭터가 없으면
            # 1. 신규 캐릭터 생성 - 사용자 입력
            character_name = input('\n저장된 캐릭터가 없습니다 새로 생성할 캐릭터명을 입력하세요\n')
            character = Character(character_name)
            select_character = character

            # 2. 정보 save.json에 저장
            if character:
                file_path = './save.json'
                with open(file_path, "r") as save_json:
                    json_data = json.load(save_json)
                    json_data['character'].append(character.state())
                with open (file_path, 'w', encoding="UTF-8")as json_file:
                    json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    # 3. 마을 또는 사냥터 이동
    while True:
        # 로그인하면 마을에서 시작하고 사냥터로 이동
        location_state = Location_State(select_character)

        move = input('\n던전으로 이동하시려면 y, 장비를 착용하려면 n을 눌러주세요 ... input (y/n)\n')
        if move == 'y':
            location_state.enter_dungeon()

            # 어떤 몬스터를 만나는건 랜덤
            # 몬스터 인스턴스 생성 (2~5마리 랜덤)
            monsters = [Monster() for _ in range(random.randint(2, 5))]

            # 4. 전투
            battle = Battle(select_character, monsters)
            battle.start()

            # 전투 이후 마을 이동
            location_state.enter_town()
            continue

        elif move == 'n':
            print('현재 보유 중인 아이템은:', ', '.join(select_character.items) if select_character.items else '없습니다.')
            equip_item = input('착용할 장비의 이름을 입력하세요 (없으면 그냥 엔터): ')
            if equip_item:
                if equip_item in select_character.items:
                    select_character.equip_item(equip_item)  # 아이템 착용
                    select_character.items.remove(equip_item)  # 보유 중인 아이템에서 제거
                    
                    # save.json에 캐릭터 정보 저장
                    file_path = './save.json'
                    with open(file_path, "r") as save_json:
                        json_data = json.load(save_json)
                        for character in json_data['character']:
                            if character['name'] == select_character.name:
                                character['equipment'] = select_character.equipment  # 착용 중인 장비 업데이트
                                character['items'] = select_character.items  # 보유 중인 아이템 업데이트
                                if 'Weapon' in character['equipment']:
                                    character['power'] += 10
                                else:
                                    character['physical_defence'] += 10
                                break
                    with open(file_path, 'w', encoding="UTF-8") as json_file:
                        json.dump(json_data, json_file, indent=4, ensure_ascii=False)
                    
                    print(f'{equip_item}을 착용하고 저장했습니다.')
                else:
                    print('해당 아이템이 없습니다.')
            else:
                continue