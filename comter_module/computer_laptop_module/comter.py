# 상업적 이용 빼고 가능ㅎ
# 이 주석 꼭 남기세요ㅋ
# MADE BY 이딥#9708


import datetime as dt

def andoem(안돼는거: str):
    return 안돼는거 + " 이/가 안돼잖아!! X발!!"

def ban(밴대상: str, 사유: str):
    if not 밴대상[-5] == "#":
        print("디스코드 닉네임이 아닙니다.")
    else:
        print("!ban @" + 밴대상)
        print()
        print("=========================")
        print("밴 대상 : " + 밴대상)
        print("사유 : " + 사유)
        print("=========================")

def Qage(A: int):
    while True:
        now_year = dt.datetime.now().year
        comter_age = (now_year - 2007) + 1

        try:
            if A == comter_age:
                print(f"{comter_age}살 맞음 ㅇㅇ")
            elif A < comter_age:
                print(f"ㄴㄴ {comter_age}살임")
            break
        except TypeError:
            print("나이를 맟추는 칸안에 공백 또는 문자열, 특수문자가 들어갈수 없습니다.")
            break

if __name__ == "__main__":
    pass
