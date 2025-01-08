'''
# 함수

# 1. 매개변수x, 리턴값x

def say_hello(): # 함수 정의 #식별자 규칙 맞춰서 써줘야됨 say_print 이딴거 안돼
    print("Hello, World")

say_hello() #함수호출

# 2. 매개벼수o, 리턴값 x

#2-1. 매개변수 1개
def print_greetting(name):
    print(f"Hello, {name}")


print_greetting("Allie") # 함수 호출
print_greetting("Martin")

#2-2. 매개변수 2개
def gugudan(dan, end): # 1~end-1
    print(f"{dan}단")

    for i in range(1, end+1):
        print(f"{dan} x {i} = {dan * i}")

gugudan(7, 15) #함수 호출
gugudan(4,20)

# 3. 매개변수x, 리턴값 o

def mul_numbers():
    print("곱셈을 시작합니다.")
    return 10 * 5

result = mul_numbers()
print(result)

#매개변수 o, 리턴값 o
def add_numbers(x, y):
    print("덧셈을 시작합니다.")
    return x + y

result2 = add_numbers(40, 50)
print(result2)
print(add_numbers(10, 50))


#다양한 타입을 return하는 함수
# 1. list 타입을 반환하는 함수
# ex. 제한값(limit) 이전까지의 짝수를 출력하는 함수
def print_even_numbers(limit):
    return [i for i in range(0, limit) if i % 2 == 0]

print(print_even_numbers(10))

# Dictionary 타입을 반환하는 함수
def print_user_info(name, grade):
    return {"user_name": name, "user_grade": grade}

print(print_user_info("철수", 2))
print(print_user_info("영희", 5))
'''

'''
#set 타입을 반환하는 함수
# print(set("Hello"))
#문자열을 set 타입으로 변환=> 고유한 문자들만 남김

def print_unique_char(word):
    return set(word)

print(print_unique_char("Hi, My name is Sean"))

# Tuple 타입을 반환하는 함수
#ex. 두 숫자의 합과 곱을 동시 반환=>합, 곱

def calculate_sum_and_product(a, b):
    return(a + b, a*b)

print(calculate_sum_and_product(3,6))
print(calculate_sum_and_product(5,6))

# Collection (컬렉션)
# 혼합 컬렉션
# ex. 딕셔너리 안에 리스트가 있는 예시
def split_numbers(numbers):
    even_nums = [n for n in numbers if n % 2 == 0]
    odd_nums = [n for n in numbers if n % 2 != 0]
    #반환값 (딕셔너리)
    return {"odd": odd_nums, "even": even_nums}


print(split_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#{"odd": 홀수 리스트, "even": 짝수 리스트}

# 매개변수로 리스트를 받는 함수
# ex. 각 요소를 2배로 만드는함수
def double(nums):
    return [i * 2 for i in nums]

print(double([1, 2, 3, 4]))

#ex. 각 요소를 문자열로 변환하는 함수
def to_string(nums):
    return [str(i) for i in nums]

print(to_string([8, 46, 24]))
'''

'''
# 실습 1
def sum_or_product(num1, num2):
    if num1 == num2:
        print(f"결과(곱): {num1 * num2}")
    else:
        print(f"결과(합): {num1 + num2}")
        
sum_or_product(2, 2)

# 실습 2



def delivery(name, price):
    
    if price < 20000:
        return f"{name} 가격: {price + 2500}"
    else:
        return f"{name} 가격: {price}"

print(delivery("상품1", 30000))
print(delivery("상품2", 15000))
'''

# 