# 예외 처리

# try:
#     x = int(input("숫자를 입력하세요: "))
#     result = 10 / x


# except ZeroDivisionError as e: # as e: 별칭
#     print("예외메시지 :", e)
# except ValueError as e:
#     print("예외메시지", e)

# else:
#     print(f"result는 {result}")

# finally:
#     print("예외처리를 종료합니다")

# # 예외가 없을 시
# # x = int(input("숫자를 입력하세요: "))
# # result = 10 / x


# # 하나로 쓰는 방법
# try:
#     x = int(input("숫자를 입력하세요: "))
#     result = 10 / x


# except (ZeroDivisionError, ValueError) as e: # as e: 별칭
#     print("예외메시지 :", e)

# else:
#     print(f"result는 {result}")

# finally:
#     print("예외처리를 종료합니다")


# raise
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.") # 예외처리 멘트 명시적으로
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("예외발생", e)
else:
    print(result)