import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 실습 1

penguins = sns.load_dataset("penguins")
# print(penguins.info())
# print(penguins.head())
#1
# sns.barplot(data=penguins, x="species",y="body_mass_g")
#2
# sns.scatterplot(data=penguins,x="bill_length_mm", y="bill_depth_mm", hue="species")

#3
# sns.violinplot(data=penguins, x="island", y="body_mass_g")
# plt.show()


# 실습 2
flights = sns.load_dataset("flights")
print(flights.info())

avg = flights.groupby("year")["passengers"].mean().reset_index() # 인덱스 초기화, 기존 인덱스를 데이터 프레임의 열로 변환
# print(avg)

# 1
# plt.plot(avg["year"], avg["passengers"])

#2
# # pivot() : 데이터를 재구조화, index, column, value
# pivot = flights.pivot(index="month", columns="year", values="passengers")
# sns.heatmap(pivot, annot=True, fmt="d") # "f": 실수, "d": 정수 "s": 문자

#3
# year_1958 = flights[flights["year"] == 1958]
# sns.barplot(x="month", y="passengers", data=year_1958)


# 실습 3
titanic = sns.load_dataset("titanic")
print(titanic.info()) # 결측값도 있음
print(titanic.head())


# 1
# sns.catplot(data=titanic, x="class", hue="survived", kind="count")


#2
# sns.kdeplot(data=titanic, x="age", hue="survived", fill=True)

# plt.show()