# 매개변수

# 기본 매개변수
# 주의. 기본값이 있는 매개변수는 맨 뒤에 와야 함 (하나만 넣었을 때 컴퓨터가 어디에 넣을지 모름)

def pr_str(txt = "안녕하시오", count = 1):
    # print(txt, count)
    for _ in range(count):
        print(txt)
     # 반복문에서 "_": 반복변수를 사용하지 않을 때 사용하는 관례적인 이름

pr_str("하이", 3)
pr_str("방가방가", 6)
pr_str() # 기본값 출력
pr_str("바이") # 두번째거 기본값 1


# 함수 호출 키워드
def intro(name, age, city):
    print(f"이름은 {name}이고 나이는 {age}이고, 사는 곳은 {city}입니다.")

intro("Allie", 23, "Seoul") #원래 우리가 하던 방식
intro(city = "Seoul", age = 23, name = "Allie")
#intro("Seoul", name = "Allie", age = 23)/
#위치 매개변수가 가장 먼저 와야함
#Allie만 할수 있나???

# 가변 매개변수
def calc_avg(*args):
    print(args) #tuple 형식

    total = 0
    for i in args:
        total += i
    avg = total / len(args) 

    return avg

print(calc_avg(1,2,3,4,5,6,7,8))
print(calc_avg(10,20,30))

# 다른 예시
def text_def(a, b, *args): # 일반 매개변수 같이 쓸 수 있음. 근데 늘 마지막에 와야됨. 구분하기 어려움
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")

text_def("Hi",100,9,7,5,3,1)

# 가변 키워드 매개변수
def print_info(**kwargs):
    print(kwargs) #dictionary

print_info(name = "홍길동", city = "서울", gender = "남자")
print_info(name = "춘향")
