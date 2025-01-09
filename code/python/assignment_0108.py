# 자판기 프로그램 1
while True:
    vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

    print()
    user = input("사용자 종류를 입력하세요:\n1. 소비자\n2. 주인\n")

    if user == "1" or "소비자":
        drink = input("마시고 싶은 음료? ")
        if drink in vending_machine:
            vending_machine.remove(drink)
            print(f"남은 음료수: {vending_machine}")
    
        else: print("없음")

    elif user == "2" or "주인":
        option = input("할 일 선택:\n1. 추가\n2. 삭제\n")
        if option =="1" or "추가":
            print(f"남은 음료수: {vending_machine}")
            add = input("추가할 음료수: ")
            vending_machine.append(add)
            print("추가완료")
        elif option == "2" or "삭제":
            print(f"남은 음료수: {vending_machine}")
            delete = input("삭제할 음료수?: ")
            if delete in vending_machine:
                vending_machine.remove(delete)
                print("삭제 완료")
            else:
                print(f"{delete}는 지금 없네요.")
    print()