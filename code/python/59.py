import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# # 데이터셋
# print(sns.get_dataset_names())

# 예제데이터
# tips = sns.load_dataset('tips')
# print(tips.head())
# print(tips.info())

# sns.scatterplot(x="total_bill", y="tip", data=tips, hue="size", palette="deep", style="size",) # 산점도

# sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, hue="size", dodge=True)

# sns.swarmplot(x="day", y="total_bill", data=tips, hue="size", dodge=True) # stripplot과 유사하지만 처음부터 겹치지 않게 출력. 그게 jitter가 필요 없는 이유

# sns.relplot(x="total_bill", y="tip", data=tips, style="time", hue="day")

# sns.catplot(x="day", y="total_bill", data=tips, kind="boxen", hue="sex")
# sns.displot(tips["total_bill"], kind="kde")
# sns.pairplot(data=tips, hue="time",)# 서로 관계 전부 드러냄
# sns.regplot(data=tips, x="total_bill", y="tip",)

# data= np.random.rand(10,10)
# sns.heatmap(data, annot=True,fmt=".2f", cmap="crest") #, cmap="crest": 색깔 퍼렇게
# plt.show()
# # plt.show()

# 옵션값은 너무 많음

'''
# 데이터셋
# print(sns.get_dataset_names())
penguins = sns.load_dataset('penguins')
penguins.columns = penguins.columns.str.strip() 
# print(penguins.head())
# print(penguins.info())


mean_penguins = penguins.groupby("species")["body_mass_g"].mean().round(2).reset_index()
# print(mean_penguins.head())
# print(mean_penguins.columns)
# print(type(mean_penguins))
# plt.bar(mean_penguins["species"], mean_penguins["body_mass_g"], color="blue", alpha = 0.7, label="Bar Chart")
# sns.scatterplot(x="bill_length_mm", y="bill_depth_mm", data=penguins, hue="species", palette="deep",) # 산점도
# sns.catplot(x="island", y="body_mass_g", data=penguins, kind="violin",)
# plt.show()
'''



# 실습 2

'''
flights = sns.load_dataset("flights")
# print(flights.tail())
# print(flights.info())


#1.
year_passengers_mean = flights.groupby("year")["passengers"].mean().round(1).reset_index()
# print(year_passengers_mean.head())
plt.plot(year_passengers_mean["year"], year_passengers_mean["passengers"], color="green", marker="o", markerfacecolor="black")
plt.show()


#2
flights_pivot = flights.pivot(index="month", columns="year", values="passengers") # 데이터 재구조화

sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="crest") #, cmap="crest": 색깔 퍼렇게

plt.show()



#3

# print(flights.head())
# print(type(flights["year"][0]))


flights_1958 = flights[flights["year"] == 1958]

print(flights_1958.head())
sns.barplot(x="month", y="passengers", data=flights_1958)
plt.show()


# plt.bar(flights["month"], flights[1958]["passengers"], color = ["r", "g"], alpha=0.7, label="Bar Chart")
# plt.show()
'''

# 실습 3
titanic = sns.load_dataset("titanic")
# print(titanic.head())
# print(titanic.info())

# #1
# sns.catplot(x="class", hue="survived", data=titanic, kind="count")
# plt.show()

# 2
sns.kdeplot(x="age", hue="survived",data=titanic)
plt.show()