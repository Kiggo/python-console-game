from character import Character
from monster import Monster
from account import Account
import json

# 쓰레드를 사용 해야 함

login_state = False

# 로그인
account_question = input('\n로그인할 계정이 있으신가요? ... input (y/n)\n')
while account_question == 'y':
    id = input('\n아이디를 입력하세요\n')
    pw = input('\n비밀번호를 입력하세요\n')

    # json 파일을 읽어서 아이디 비밀번호 확인
    with open('./save.json', 'r') as save_json:
        json_data = json.load(save_json)
        if json_data['account'][0]['id'] == id and json_data['account'][0]['pw'] == pw:
            print()
            print('로그인 성공.')
            login_state = True
            break
        else:
            # 계정 정보 불일치
            print('일치하는 계정 정보가 없습니다 다시 입력해주세요.')
            continue
else:
    # 계정 생성
    print('계정 생성을 시작합니다.')
    id = input('\n새로 등록할 아이디를 입력하세요\n')
    pw = input('\n새로 등록할 비밀번호를 입력하세요\n')
    account = Account(id, pw)
    account.sign_in()
    login_state = True


# 로그인한 상태
if login_state:
    # 계정에 캐릭터가 있는지 확인
    with open('./save.json', 'r') as save_json:
        json_data = json.load(save_json)
        if json_data['character']:
            for character in json_data['character']:
                print(f'{character["name"]}의 캐릭터가 존재합니다.')

            character_name = input('\n접속할 캐릭터명을 입력하세요\n')

            for character in json_data['character']:
                if character['name'] == character_name:
                    print()
                    print(f'{character["name"]} 캐릭터 정보를 가져옵니다.')
                    print(f'스킬은 {character["skill"]} 을 부여 받았습니다')
                    print(f'캐릭터 레벨은 {character["level"]} 이며')
                    print(f'hp는 {character["hp"]} mp는 {character["mp"]}, 공격력은 {character["power"]} 물리방어력은 {character["physical_defence"]} 마법방어력은 {character["magic_defence"]} 경험치는 {character["exp"]}입니다')
        else:
            # 계정에 캐릭터가 없으면
            # 1. 신규 캐릭터 생성 - 사용자 입력
            character_name = input('\n저장된 캐릭터가 없습니다 새로 생성할 캐릭터명을 입력하세요\n')
            character = Character(character_name)

            # 2. 정보 save.json에 저장
            if character:
                file_path = './save.json'
                with open(file_path, "r") as save_json:
                    json_data = json.load(save_json)
                    json_data['character'].append(character.obj())
                with open (file_path, 'w', encoding="UTF-8")as json_file:
                    json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    # 3. 마을 또는 사냥터 이동
    # 로그인하면 마을에서 시작하고 사냥터로 이동
    

    # # 어떤 몬스터를 만나는건 랜덤
    # # 몬스터 인스턴스 생성 
    # monster = Monster()

    # # 4. 전투

    # # 몬스터 사망
    # monster.dead()






