'''
# while 문
i = 5
while i > 0:
    print("반복문 연습", i)
    i -= 1

print("종료")

# 합계 구하기
num = 1 # 더하는 숫자
total = 0 # 총합
while num <= 10:
    total += num
    print("현재 total 값 >", total)
    num += 1

print(f"1부터 10까지의 합은 {total}입니다.")

# 입력값 받기
user_input = ""
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. '종료' 입력시 종료됩니다. ")
    print(f"입력한 값: {user_input}")

print("프로그램이 종료되었습니다.")
'''

'''
# break문
# 예시. 숫자를 입력받아서 0이 입력되면 반복문 종료
while True:
    num = int(input("숫자 입력(0 입력시 종료): "))

    if num == 0:
        print("프로그램 종료")
        break

    print(f"입력한 숫자는 {num}입니다")
'''

'''
# continue 문
# 예시. 숫자 입력받고 짝수만 출력하고 홀수는 건너뛰기
while True:
    num = int(input("숫자 입력(음수 입력시 종료): "))

    if num < 0:
        print("프로그램 종료")
        break # 음수 입력 시 프로그램 종료

    if num % 2 != 0:
        continue # 홀수는 건너뛰고, 다시 입력받기

    print(f"입력한 짝수는 {num}입니다")
'''

# while 문 사용 실습
while True:
    num = input("숫자를 입력하세요.(양수만 입력 가능. '종료' 입력시 프로그램 종료): " )

    if num == "종료":
        print("프로그램 종료")
        break

    if num.isdigit() == True:
        num_int = int(num)
    

        if num_int < 0:
            print("양수만 입력해라")
            continue

        if num_int == 0:
            continue

        if num_int > 0:
            i = 1
            total = 0
            while i <= num_int:
                total += i
                i += 1

            print(f"1부터 {num_int}까지의 합은 {total}입니다.")

    else:
        print("양수만 입력해라")
        continue
        










