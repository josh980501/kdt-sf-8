'''
# 이중 for문

for i in range(5):
    print(f'외부 반복문의 i 값: {i}')

    for j in range(3): # 바깥쪽 변수랑 보통 달라야됨 i, j, k
        print(f'외부 반복문의 i 값: {j}')

    print("---------")
'''
'''
# 이차원 리스트와 이중 for 문
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 요소(elem 변수)의 합계 구하기
total_sum = 0
for row in matrix:
    # print(f"외부반복문의 row: {row}")

    for elem in row:
        # print(f"내부반복문의 elem: {elem}")
        total_sum += elem
    #1번 시점: 내부 반복무이 종료
    print(f"중간 합계: {total_sum}")
#2번 시점: 외부 반복문이 종료
print(f"전체 합계: {total_sum}")

# 짝수만 출력
matrix2 = [
    [4, 2117, 98],
    [60, 17, 98],
    [2, 74, 33]
]
print("짝수만 출력:", end=" ")
for row in matrix2:
    for elem in row:
        if elem % 2 ==0:
            print(elem, end=" ")

#구구단 실습
for num in range(2, 10):
    print(f"[{num}단]")
    for i in range(1, 10):
        print(f"{num} x {i} = {num * i}")
    print()
'''

'''
#별찍기 1

for star_row in range(3):
    for star in range(5):
        print("*", end = "")
    print()

# 별찍기 2
for star_row in range(4):
    for star in range(star_row + 1):
        print("*", end = "")
    print()
#별찍기 3
for star_row in range(5):
    for star in range(5 - star_row, 0, -1):
        print("*", end = "")
    print()
'''

'''
# 별찍기 4
for star_row in range(4):
    for space in range(4 - star_row, 0, -1):
        print(" ", end = "")
        for star in range(1, 8):
            if star % 2 == 1:
                print("*"*star)
        print()
'''

'''
# 별찍기 4
for star_row in range(4):
    
    for space in range(4 - star_row, 0, -1):
        print(" ", end = "")

    for star in range(1, 8):
        if star % 2 != 0:
            print("*"*star)
    print()
'''

# 별찍기 4 Sean님 풀이
# 엑셀에 출력한다고 생각

n = 4 #줄 개수
for i in range(1, n + 1): #1~n 반복
    # 공백 출력
    # i 번째 줄에 대한 내용
    for j in range(n-i): #n - i개의 공백이 출력
        print(" ", end = "")
        # ex. 1번째줄: N - 1/ 2번째 줄: n-2 ....4 번째줄: n-4



    # 별 출력
    for k in range(2*i - 1): #2*i - 1 개의 별 출력
        print("*", end="")
    #내부 포문이 종료되는 시점
    print()


# 별찍기 5 Sean님 풀이
# 삼각형 나눠서 풀기
n = 5 # 줄 개수

# 윗 삼각형


# 아래 삼각형