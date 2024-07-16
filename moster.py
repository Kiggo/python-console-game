# [몬스터] 
# - 종류
# - hp
# - mp
# - 물리방어력
# - 마법방어력
# - 드랍아이템
# - 경험치
# - 여러마리

class Monster:

    종류 = ['몬스터1', '몬스터2', '몬스터3', '몬스터4']
    마리수 = [1, 2, 3, 4, 5]
    드랍아이템 = ['모자', '무기', '갑옷', '장갑', '신발']
    경험치 = [10, 20, 30]

    def __init__(self):
        self.hp = 10
        self.mp = 10
        self.physical_defence = 10
        self.magic_defence = 10