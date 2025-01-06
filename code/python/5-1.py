# 이차원 리스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])

print(matrix[0][0])
print(matrix[1][2])

#요소 추가
matrix[1] = matrix[1] +[99]
print(matrix)

#행 추가
matrix = matrix + [[10, 11, 12]]
print(matrix)

# 요소 수정
matrix[0][0] = 100
matrix[1][1] = 5000
print(matrix)

# 행 삭제
del matrix[2]
print(matrix)

# 행 개수
rows = len(matrix)
rows2 = len(matrix[0])
rows3 = len(matrix[1])
rows4 = len(matrix[2])
print(rows)
print(rows2) #3 . 0번 행 길이(요소 개수)
print(rows3) #4
print(rows4) #3

