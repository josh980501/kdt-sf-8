'''
# 내장 함수

# abs(정수): 절댓값 구하는 내장함수

print(abs(-77))
print(abs(0))
print(abs(10))

# 만약에, abs() 내장 함수가 없었다먄?
def my_abs(n):
    if n < 0:
        return - n # 음수라면 양수로 변환
    else:
        return n # 양수는 그대로
print(my_abs(-77))
print(my_abs(0))
print(my_abs(10))
    

# pow(x, y): x^y 구하는 내장함수
print(pow(10, 2))
print(pow(2, 10))
print(pow(3, 4))

# 만약에 pow() 내장 함수가 없었다면?
def my_pow(x, y): #X: 밑, y: 지수
    num = 1 # 초기값

    for _ in range(0, y): #y번 곱하는 행위를 반복
        num *= x

    return num
print(my_pow(10, 2))
print(my_pow(2, 10))
print(my_pow(3, 4))

#map()


# 각 요소마다 적용하고 싶은 함수
def square(x):
    return x**3


# 리스트
numbers = [2, 4, 6, 8, 10]

print(map(square, numbers)) #<map object at 0x000001B71091FB20> 이 주소상에 map이라는 object가 있다는 것을 알려줌.값을 보려면 list 써야.개발자들이 세팅해놓은것임
print(list(map(square, numbers)))

# filter()
def even_number(x):
    return x % 2 == 0

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter(even_number, numbers2)) #<filter object at 0x000002BED6E18AF0>
print(list(filter(even_number, numbers2))) #[2, 4, 6, 8, 10]
'''

'''
# 배수 함수 실습
def baesoo(x):
    baesoo_list = [i for i in range(1, 31) if i % x == 0]
    for n in baesoo_list:
        print(n, end = " ")
        
    print()
    print(f"{x}의 배수의 개수: {len(baesoo_list)}")

baesoo(3)

#Sean 님 풀이
def count(num):
    lists = [i for i in range (1, 31) if i % num == 0]
    counts = len(lists)

    return (lists, counts) #리스트 반환할 수 있는 것처럼 튜플 형식으로 반환할 수 있음-->중요

n = 4 #배수
my_lists, my_counts = count(n)
print(f"{n}의 배수 목록: {my_lists}")
print(f"{n}의 개수: {my_counts}")
print(count(n))
'''
#풀이 2(Sean)


def count(num):
    # 중첩함수 - 해당 함수 안에서만 호출 가능
    def check(x):  # num의 배수인지를 검사하는 함수
        return x % num == 0

    lists = list(filter(check, range(1, 31)))

    return (lists, len(lists))


n = 6
my_lists, my_counts = count(n)  # (리스트, 개수)
print(f"{n}의 배수 목록: {my_lists}")
print(f"{n}의 개수: {my_counts}")