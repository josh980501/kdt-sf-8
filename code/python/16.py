'''
# 전역 변수
quantity = 12

def get_price(price):
    #price: 매개변수
    return price * quantity

print(f"{quantity}개의 가격은 {get_price(5000)}입니xi")

# 지역변수
def oneUp():
    x = 0
    x += 1
    return x

print(oneUp())
# print(x) # NameError: name 'x' is not defined
print(quantity)


# 변수의 유효범위
amount = 10

def price_sum(price):
    amount = 7 
    print('#', amount) #7 (지역변수)
    return price * amount # 14000 = 2000 * 7

result = price_sum(2000)
print(result)
print('##', amount) #10(전역변수)
'''

# global 키워드
x = 0
def oneUp():
    global x # 함수 내에서 전역변수 "변경"이 이루어질 예정 힌트
    x += 1
    return x

print(oneUp())
print(oneUp())
print(oneUp())

print(x) # 3 나옴
