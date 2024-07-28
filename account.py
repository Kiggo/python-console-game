import json

# [계정]
# - 여러명의 캐릭터
# - 소지품
# save.json 에서 가져온 정보를 토대로 구성됨

class Account:

    def __init__(self, id, pw):
        self.id = id
        self.pw = pw
        pass

    def sign_in(self):
        id = self.id
        pw = self.pw

        new_account_obj = {
            'id': id,
            'pw': pw
        }

        file_path = './save.json'
        with open(file_path, "r") as save_json:
            json_data = json.load(save_json)

            json_data['account'] = new_account_obj
            json_data['character'] = []

        with open (file_path, 'w', encoding="UTF-8")as save_json:
            json.dump(json_data, save_json, indent=4, ensure_ascii=False)


