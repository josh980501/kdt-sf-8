while True:
    positive_input = input("양수를 입력하세요 ('종료' 입력 시 프로그램 종료): ")

    if positive_input == "종료":
        print("프로그램을 종료합니다")
        break

    try:
        positive_input = int(positive_input)

        if positive_input < 0:
            print("양수만 입력하세여")
            continue
        elif positive_input == 0:
            continue
        else:
            print("로직을 넣으세요")

    except:
        print("양수만 입력하세요")
        continue