import matplotlib.pyplot as plt
from matplotlib import font_manager


'''
# 실습1. 그래프 그리기
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2019 = [100, 120, 140, 110, 130, 150, 160, 170, 180, 200, 190, 210]
sales_2020 = [90, 110, 130, 120, 140, 160, 170, 160, 150, 180, 200, 190]

line1 = plt.plot(months, sales_2019, color="blue", label = "2019")
line2 = plt.plot(months, sales_2020, color="orange", label = "2020")

plt.legend(loc="upper left", fontsize=10, frameon=True)
plt.title("Monthly Sales Comparison (2019-2020)")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
'''

'''
# 실습2. 막대그래프

categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5',]
data = [20, 35, 15, 27, 45]

plt.bar(categories, data, color="blue", alpha = 0.7, label="Bar Chart")
plt.xticks(categories, rotation=45) # 바꿔놓을 수 있음 #rotation: 글자 각도 바뀜
plt.ylim([0, 50])
plt.grid(True, axis="both", color="gray",alpha=0.5) # 그리드. axis는 x,y 또는 both(both가 기본값), alpha는 조도?
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart")

plt.gcf().subplots_adjust(bottom=0.2) # 바닥에 있는 글자 잘리는 문제 해결
plt.show()
'''

'''
# 파이 차트
sizes = [34, 32, 16, 18]
labels = ["Apple", "Banana", "Melon", "Grapes"]
explode = [0, 0.1, 0, 0.1]
colors = ["red", "yellow", "darkgreen", "purple"]

plt.pie(sizes, labels=labels, explode=explode, autopct="%1.1f%%", shadow=False, 
        # startangle=180, 
        colors=colors,
        textprops={"fontsize": 10, "color": "black"},
        wedgeprops={"edgecolor": "black", "width": 0.8}
        )
plt.show()
'''



# Martin 풀이

'''
# 실습1. 그래프 그리기
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2019 = [100, 120, 140, 110, 130, 150, 160, 170, 180, 200, 190, 210]
sales_2020 = [90, 110, 130, 120, 140, 160, 170, 160, 150, 180, 200, 190]

plt.plot(months, sales_2019, color="blue", label = "2019")
plt.plot(months, sales_2020, color="orange", label = "2020")

plt.title("Monthly Sales Comparison (2019-2020)", fontsize=15, pad=10)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend() ##########upper left가 기본###############################3
plt.show()
'''

'''
# 실습 2
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5',]
data = [20, 35, 15, 27, 45]

plt.figure(figsize=(8,8)) # 그래프 사이즈 설정 --------------------------#####################################################
plt.bar(categories, data, color="blue", alpha=0.7)

plt.title("Bar Chart", fontsize= 20, pad=10)
plt.xlabel("Category")
plt.ylabel("Value")
plt.grid(True, axis="both", color="gray",linestyle="--", alpha=0.6)
plt.xticks(categories, rotation=45)
plt.show()
'''

# 실습 3.
sizes = [34, 32, 16, 18]
labels = ["Apple", "Banana", "Melon", "Grapes"]
explode = [0, 0.1, 0, 0.1]
colors = ["red", "yellow", "darkgreen", "purple"]

plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct="%1.1f%%", wedgeprops={"edgecolor": "black", "width": 0.8})

plt.show()