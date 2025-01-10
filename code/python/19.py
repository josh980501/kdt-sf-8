'''
# 재귀함수

def sos(i):
    print(f"{i}번째 도움 요청")

    if i == 1:
        return ""
    else:
        return sos(i - 1)
sos(10)

# 팩토리얼

def factorial(n):
    print("n >>", n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(3))
print(factorial(5))
print(factorial(7))
'''
# 피보나치 수열 만들기

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(6))
    