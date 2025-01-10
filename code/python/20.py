'''
# 람다식

def add(x, y): # 일반 함수
    return x + y

print(add(3, 4))

add2 = lambda x, y: x + y # 람다식
print(add2(4, 5))

# 매개 변수가 1개인 람다식

square = lambda x: x**2 # 변수에 할당
print(square(5))
print((lambda x: x**2)(5)) #할당 안하고 바로 실행

# 매개변수가 2개인 람다식
mul = lambda x, y: x*y
print(mul(3, 7))
print((lambda x, y: x*y)(3, 7))

# 람다 변수를 매개변수로 전달

# call(): 함수를 인수로 받아서 그 함수를 10번 호출하는 함수
def call(func):
    for _ in range(10):
        func() # 전달받은 함수를 호출


# hello(): 일반함수로, "안녕" 문자 출력
def hello():
    print("안녕")

# 람다식으로 정의된 함수 hello2
hello2 = lambda: print("하이")

call(hello) # call 함수에 hello 함수를 전달해서 10번 실행
call(hello2) # call 함수에 hello2 람다식을 전달해서 10번 실행

# 고차함수(map, filter 등) 와 함께 쓰는 람다식
# 고차함수: 함수를 인수로 받을 수 있고, 함수를 반환할 수도 있음
#1. 람다식 with map()
def square(x):
    return x**3


# 리스트
numbers = [2, 4, 6, 8, 10]

print(list(map(square, numbers))) # 일반 함수
print(list(map(lambda x: x**3, numbers))) # 람다식

# 2. 람다식 with filter()
def even_number(x):
    return x % 2 == 0

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(even_number, numbers2))) #[2, 4, 6, 8, 10]
print(list(filter(lambda x: x% 2 == 0, numbers2))) #[2, 4, 6, 8, 10]


#3. map, filter 두개를 람다식과 함께 사용
#3-1. 짝수만 남겨서 -> filter
    # filter(lambda x: x % 2 == 0, numbers2)
#3-2. 그 제곱을 계산 -> map

even_squared_nums = list(map(lambda x: x **2, filter(lambda x: x % 2 == 0, numbers2)))
print(even_squared_nums)
'''


# 실습 6. 함수 종합 프로그래밍

# 함수 정의부
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]

# 평균 기온 계산 함수
def avg():
    city = input("도시 이름을 입력하세요: ")
    a = filter(lambda x: x[1] == city, weather_data)
    number = map(lambda x: x[2], a)
    list_number = list(number)
    sum = 0
    for n in list_number:
        sum += n
    mean = sum / len(list_number)
    print(f"{city}의 평균 기온: {mean:.2f}°C")

# 최고/최저 출력 함수
def max_min():
    city = input("도시 이름을 입력하세요: ")
    a = filter(lambda x: x[1] == city, weather_data)
    number = map(lambda x: x[2], a)
    list_number = list(number)

    print(f"{city}의 최고 기온: {max(list_number)}°C, 최저 기온: {min(list_number)}°C" )

# 강수량 분석 함수
def rain():
    city = input("도시 이름을 입력하세요: ")
    a = filter(lambda x: x[1] == city, weather_data)
    number = map(lambda x: x[3], a)
    list_number = list(number)
    all_rain = sum(list_number)

    print(f"{city}의 총 강수량: {all_rain}\n{city}의 강수량이 있었던 날: {len(list_number)}일")

# 데이터 추가 함수
def data_add():
    day = input("날짜를 입력하세요 (YYYY-MM-DD):" )
    city = input("도시 이름을 입력하세요: ")
    temp = float(input("평균 기온을 입력하세요 (°C): "))
    rain = float(input("강수량을 입력하세요 (mm): "))
    weather_data.append([day, city, temp, rain])
    print(f"{city}의 데이터가 추가되었습니다.")

# 전체 데이터 출력 함수
def all():
    for i in range(len(weather_data)):
        print(f"날짜: {weather_data[i][0]}, 도시: {weather_data[i][1]}, 평균 기온: {weather_data[i][2]}, 강수량: {weather_data[i][3]}")

# 출력부
while True:

    print("[날씨 데이터 분석 프로그램]")
    option = input("1. 평균 기온 계산\n"
                "2. 최고/최저 기온 찾기\n"
                "3. 강수량 분석\n"
                "4. 날씨 데이터 추가\n"
                "5. 전체 데이터 출력\n"
                "6. 종료\n"
                "원하는 기능의 번호를 입력하세요: "
                )

    if option == "1":
        avg()

    if option == "2":
        max_min()

    if option == "3":
        rain()

    if option == "4":
        data_add()

    if option == "5":
        all()

    if option == "6":
        print("프로그램을 종료합니다")
        break
    print()