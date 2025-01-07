'''
# 조건문

age = 25

#if 문
if age < 20: #20 < 20 -> false
    print("안녕하세요")
    print("미성년자 입니다") #문장 여러개 출력 가능

if age >= 20:
    print("성인입니다")
print(f"나이는 {age}(세) 입니다")
'''
'''
#else 문
if age < 20: #20 < 20 -> false # 1~19
    print("안녕하세요")
    print("미성년자 입니다") #문장 여러개 출력 가능

else: # 20~ 값이 나뉘는걸 분기처리한다고 함
    print("안녕하세요")
    print("성인입니다")

'''

'''
# elif 문(else if)
age = int(input("나이를 입력하세요: "))

if age < 20:
    print("10대입니다")
elif age < 30:
    print("20대입니다")
elif age < 40:
    print("30대입니다")
elif age < 50:
    print("40대입니다")
else:
    print("50대 이상입니다")
'''

'''
# 비밀번호

password = input("비밀번호를 입력하세요: ")

if password == "abc123":
    print("비밀번호가 맞습니다")
else:
    print("비밀번호가 틀렸습니다")

# 짝수
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0 :
    print("짝수입니다")
else:
    print("홀수입니다")
'''

'''
# 학점
grade = int(input("점수를 입력하세요: "))

if grade >= 90:
    print("학점: A")
elif grade >= 80:
    print("학점: B")
elif grade >= 70:
    print("학점: C")
elif grade >= 60:
    print("학점: D")

else:
    print("학점: F")

'''

# 중첩 조건문
# 불리언(Boolean): 참과 거짓을 나타내는 데이터 타입 (True랑 False 밖에 없음)
# 참: True (맨앞에 무조건 대문자)
# 거짓: False (맨앞에 무조건 대문자)

'''
is_login = True
role = "admin"

if is_login: # is_login == True 와 같음. 근데 이렇게 할 필요 없음
    print("로그인 상태입니다")
    if role == "admin":  #개발자가 보기 간편하게 조건문 간단하게 쓸것
        print("권리자 권한을 갖습니다")
    elif role == "editor":
        print("편집자 권한을 갖습니다")
    else:
        print("일반 사용자입니다")

else:
    print("로그인이 필요합니다")

#삼항 연산자
age = 12
status = "성인" if age >= 20 else "미성년자"
print(status)

number = 7
result = "짝수" if number % 2 ==0 else "홀수"
print(result)

a, b = 5, 8
max_value = a if a > b else b
print(max_value)

# 중첩 삼항 연산자
score = 81
grade = "A" if score >= 90 else ("B" if score >= 80 else "C") # 가독성 너무 떨어져서 굳이 쓰지마셈
'''

'''
# 조건문에서 in 연산자 활용
users = ["Sean", "Linda", "Allie", "Martin"]

username = input("Name >> ")

if username in users:
    print(f"환영합니다잇 {username}님ㅎㅎ")
else:
    print("등록되지 않은 사용자입니데이. 회원가입 진행하라우")
'''


# 중첩 조건문 실습
age = int(input("나이를 숫자로 입력해주세요: "))
pay = input("결제방법을 입력해주세요 (현금 또는 카드): ")

if age > 0:
    if age < 8:
        price = 0
    elif age <14:
        price = 450
    elif age < 20:
        if pay == "card":
            price = 720
        else:
            price = 1000
    elif age < 75:
        if pay == "card":
            price = 1200
        else:
            price = 1300
    else:
        price = 0
            
    print(f"{age}세의 {pay}요금은 {price}원입니다.")

else:
    print("나이는 음수값이 될 수 없습니다")


'''
# in 연산자 실습
fruit_kcal_dict = {
    "apple": 95,
    "banana": 105,
    "cherry": 50
}
fruit = input("과일을 영문으로 입력하세요. : ")

if fruit in fruit_kcal_dict:
    print(f"{fruit}의 칼로리는 {fruit_kcal_dict[fruit]}kcal입니다.")

else:
    print("해당 과일이 포함되지 않았습니다.")
    
'''