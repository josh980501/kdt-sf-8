import matplotlib.pyplot as plt

'''
# 히스토그램----------------------데이터 분포 나타낼 때
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6]

plt.hist(data, bins= 6, color="green", histtype= "step") # bins(기본값 10)로 구간 경계 구할 수 있음 10이면 1~6을 10개 구간으로 나눔


plt.title("hist")
plt.xlabel("value")
plt.ylabel("bins")

plt.show()
# bins=10 [1,1.5],[1.5, 2], [2,2.5], [2.5, 3], [3, 3.5], [3.5, 4], [4, 4.5], [4.5, 5], [5, 5.5], [5.5, 6] : 구간을 10개로 나눠
'''

'''
# 여러개 data
data1= [1, 2, 2, 3, 3, 3, 4]
data2= [2, 3, 3, 4, 4, 5, 6]

plt.hist([data1, data2], bins=6, color=["green", "purple"], label=["data1", "data2"])
plt.title("hist")
plt.xlabel("value")
plt.ylabel("bins")
plt.legend()
plt.show()
'''
'''
#----------------------------------------------------------
# 산점도: 관계의 방도를 파악할때

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [20, 50, 80, 100, 200]
colors = [10, 20, 30, 40, 50]

plt.scatter(x, y, s=sizes, c=colors, cmap="plasma") #cmap: 색상 배열 컬러매
plt.colorbar(label="color bar") # 없어도 무관.

plt.show()
'''

'''
# 산점도 예시
import numpy as np

n = 50
x = np.random.rand(n) # 0과 1의 난수
y = np.random.rand(n)

area = (30 * np.random.rand(n)) ** 2 # 0~30 사이의 난수 생성 후 제곱
colors = np.random.rand(n)

plt.scatter(x, y, s=area, c=colors, cmap="Spectral", alpha=0.5)
plt.colorbar(label="color bar") # 없어도 무관.
plt.show()
'''

#-------------------------------------------
# 파이 차트
# sizes = [25, 25, 20, 20]
# labels = ["A", "B","C", "D"]

'''
sizes = [15, 30, 34, 10]
labels = ["apple", "banana", "grape", "cherry"]
explode = [0, 0.1, 0, 0]
colors = ["gold", "lightblue", "lightgreen", "pink"]

plt.pie(sizes, labels=labels, explode=explode, autopct="%1.1f%%", shadow=True, 
        # startangle=180, 
        colors=colors,
        textprops={"fontsize": 20, "color": "darkblue"},
        wedgeprops={"edgecolor": "black", "width": 0.7}
        )
plt.show()
'''


# 도넛
sizes = [40, 30, 20, 10]
labels = ["X", "Y", "Z", "W"]
plt.pie(sizes, labels=labels, wedgeprops={"width":0.4}) # 얇게
plt.show()