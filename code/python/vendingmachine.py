# 자판기 실습 아이고님 풀이
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

def check_machine():
    print("남은 음료수: ", vending_machine)

def is_drink(drink):
    return drink in vending_machine

def add_drink(drink):
    vending_machine.append(drink)
    print(f"{drink}추가완료")

def remove_drink(drink):
    if is_drink(drink):
        vending_machine.remove(drink)
        print(f"{drink} 드릴게요")
    else:
        print("음료가 없습니다.")
# def void():
#     pass      # none이 나옴

# print(is_drink("게토레이"))


while True:
    user_type = input("사용자 유형을 선택하세요.\n"
                     "1. 소비자\n"
                     "2. 주인\n"
                     "0. 종료\n:")
    
    if user_type == "1" or "소비자":
        drink = input("마시고 싶은 음료? ")
        remove_drink(drink)
        check_machine()

    elif user_type == "2" or "주인":
        action = input("할 일 선택:\n1. 추가\n2. 삭제\n:")
        if action == "1":
            drink = input("추가할 음료수? ")
            add_drink(drink)

        elif action == "2":
            drink = input("삭제할 음료수? ")
            vending_machine.remove(drink)
            print(f"{drink} 삭제 완료")
        
        else:
            print("잘못된 값입니다")
        check_machine()

    elif user_type == "0":
        print("프로그램을 종료합니다")
        break

    else:
        print("다시 입력하세요")