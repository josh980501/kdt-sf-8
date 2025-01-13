# 클래스

"""
# 클래스 정의
class Car:
    # 2개의 속성을 가짐
    model = ""
    cc = 0

    # 메서드 추가
    def info(self):
        print(f"모델명: {self.model}, 배기량: {self.cc}cc")


car1 = Car()  # 인스턴스 생성
car1.model = "아반떼"
car1.cc = 1600

car2 = Car()  # 인스턴스 생성
car2.model = "K5"
car2.cc = 2000

# print(f"모델명: {car1.model}")
# print(f"배기량: {car1.cc}")
# print(f"모델명: {car2.model}")
# print(f"배기량: {car2.cc}")
car1.info()
car2.info()
"""


# 생성자 존재할 때
class Car:
    """
    def __init__(self, 매개변수1, 매개변수2, ...):
        self.속성1 = 매개변수1
        self.속성2 = 매개변수2
        ...
        # 생성자의 매개변수의 값으로 객체의 속성을 초기화(할당)
    """

    # 생성자
    def __init__(self, model, cc): #특수 메서드
        self.model = model # self.model = "싼타페"
        self.cc = cc # self.cc = 2000

    def __str__(self): # 특수 메서드. 얘가 있어야 반환
        return f"**모델명: {self.model}, 배기량: {self.cc}cc"

    def info(self): #일반 메서드
        print(f"모델명: {self.model}, 배기량: {self.cc}cc")


# 인스턴스 생성
car1 = Car("싼타페", 2000)
car2 = Car("BMW", 2200)
car1.info()
car2.info()
print(car1)
print(car2)

print("====== 승용차 리스트 ======")
cars = [Car("소나타", 2000), Car("쏘렌토", 3000), Car("아반떼", 1600)]
"""

snt = Car("소나타", 2000)
srt = Car("쏘렌토", 3000)
avt = Car("아반떼", 1600)
cars2 = [snt, srt, avt]
"""

for car in cars:
    print(car)
    # car.info()

# 클래스 실습

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        if self.num2 == 0:
            return "0으로 나눌 수 없습니다."
    
        return self.num1 / self.num2
    

calc = Calculator(10, 7)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())

calc2 = Calculator