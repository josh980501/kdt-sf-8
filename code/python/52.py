import numpy as np
'''
# 1차원
print([1, 2, 3, 4, 5])
a1 = np.array([1, 2, 3, 4, 5]) #컴마가 없음. [1 2 3 4 5]
print(a1)

# 2차원
a2 = np.array([[1, 2, 3], [4, 5, 6]]) # 대괄호가 2개!
print(a2)

# 3차원
a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a3)

print(a2.shape) # 배열 모양, 튜플 형태. (2, 3): 2행 3열
print(a2.ndim) # 차원
print(a2.dtype) # 원소의 자료형 int64(정수 타입, 64bit)
print(a2.itemsize) # 원소의 크기(바이트)
print(a2.size) # 원소의 개수
'''
'''
arr = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
print(arr[0, 1]) # 리스트랑 좀 다른점. arr[0][1]
print(arr[2, 2])
row  = [0, 2]
col  = [2, 2]
print(arr[row, col])

arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 20]) #[30 40 50]
print(arr[arr % 20 == 0]) # [20 40]
arr[arr > 20] = 0
print(arr)  #[10, 20, 0, 0, 0]
lists = [2, 3, 4]
print(arr[lists]) #[0 0 0]
'''

'''
# 배열 생성
zero = np.zeros((3, 3))
print(zero)
ones = np.ones((5, 5))
print(ones)
ranges = np.arange(1, 20, 3) # [ 1  4  7 10 13 16 19] ...range랑 범위 똑같
print(ranges)
linespaces = np.linspace(0, 2, 10) #0부터 2까지 10개를 균등하게생성--> 이러면 소수점이 생김
print(linespaces)
'''

'''
# 1차원 배열을 2x3 배열로 변환
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped = np.reshape(array, (3, 3)) # shape 다시..근데 개수 맞아야됨
print(reshaped)
resized = np.resize(array, (4, 4))
print(resized) # 나머지를 계속 채움
'''

'''
# 연산
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a + b) # [ 6  8 10 12]
print(a * b) # [ 5 12 21 32]

c= np.array([1, 4, 9, 16, 25, 36])
print(np.sqrt(c)) # 제곱근
print(np.exp(c)) # 지수함수
print(np.log(c)) # 자연로그
'''
'''
# 삼각 함수
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
# 0, 30, 45, 60, 90
print(angles)
print(np.sin(angles))
print(np.cos(angles))
'''

'''
'''
# 합치기
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 수평합치기
print(np.hstack((a, b)))

# 수직 합치기
print(np.vstack((a, b)))

# 열 기준 합치기
print(np.column_stack((a, b))) # 열끼리 합침. 3행 2열이 됨 [[1 4] [2 5] [3 6]]


'''
# 분할하기
a = np.array([[1, 2, 3], [4, 5, 6]])
# 수평을 기준으로 분할
h = np.hsplit(a, 3)
print(h)
# 수직을 기준으로 분할
v = np.vsplit(a, 3)
print(v)
'''