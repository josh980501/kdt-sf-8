
'''
number = int(input("몇단을 출력할까요?: "))
for i in range(1, 10):
    result = number * i
    print(f"{number} X {i} = {result}")

#정수 합 계산
num = int(input("어디까지 계산할까요?: "))
total = 0
for i in range(1, num + 1, 2):
    total += i
print(f"1부터 {num}까지의 홀수의 합: {total}")
'''

# 평균값 구하기 실습
student = {
    "st1": [83, 92, 88],
    "st2": [90, 79, 86],
    "st3": [88, 86, 94]
}
korean = 0
english = 0
math = 0
for i in student.values():
    korean += i[0]