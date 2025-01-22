import matplotlib.pyplot as plt
from matplotlib import font_manager
'''
# # 폰트 경로(한글 폰트 경로 맞춰줌)
# path = "Pretendard-Medium.ttf" # f2눌러서 복사
# font = font_manager.FontProperties(fname=path).get_name()
# plt.rc('font', family=font)


#-----------
# 기본 사용법
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# plt.plot(x, y, color="red", linestyle="--", linewidth=3, label="Sample graph") # 일반적인 선
plt.plot(x,y, marker="*",markersize=20, markerfacecolor="red", markeredgecolor="blue", label="marker sample")  # 마커 표시, # edgecolor는 별 테두리색깔

# plt.title("Matplotlib", pad=10, fontsize=20, color="white", backgroundcolor="green") # 제목, pad는 제목과 그래프 사이 간격. 예전 방법
font = {
    "size": 20,
    "color": "white",
    "backgroundcolor": "black",
    "weight": "bold",

} # 폰트 설정. 키값들은 그냥 외우자!!!! weight은 굵기


plt.title("Matplotlib Dict", pad=10, fontdict=font) # 최근 방법. 여러군데에서 폰트 똑같이 쓰기 위함

plt.legend(title="legend", fontsize=13, loc="lower center") # 범례표시
plt.grid(True, axis="both", linestyle="--", color="blue",alpha=0.1) # 그리드. axis는 x,y 또는 both(both가 기본값), alpha는 조도?

# x, y 축 레이블
plt.xlabel("x axis", fontdict=font, labelpad=10) # 간격은 labelpad. pad아님
plt.ylabel("y axis", fontdict=font)

# 축 범위 설정
# plt.xlim([1,10])
# plt.ylim([0, 20])
# plt.axis([1,10,0,20])
# plt.axis("equal") # x축과 y축 간격을 동일하게 설정
# plt.axis("tight") # 그래프가 모든 영역을 채우도록 설정
# plt.axis("scaled") # 각 축의 데이터의 비율에 따라서 설정
# plt.axis("auto") # 자동으로 축 범위 설정


# plt.show()
'''

'''
################---------------
# 그래프 여러개 그리기
# 하나의 창에 여러개 그리기
x = [1,2,3,4]
y1=[1,2,3,4]
y2=[2,4,6,8]
y3=[3,6,9,12]
y4=[4,8,12,16]

plt.plot(x,y1,label="y=x", color="red")
plt.plot(x,y2,label="y=2x", color="orange")
plt.plot(x,y3,label="y=3x", color="green")
plt.plot(x,y4,label="y=4x", color="blue")

plt.legend(title="4graph",loc="upper center", ncol=2) # 범례. ncol=4: column을 4개로 한다는 뜻
plt.title("graph sample")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
'''

'''
# 하나씩 여러개 그리기. 방법1
x = [1,2,3,4]
y1=[1,2,3,4]
y2=[2,4,6,8]
y3=[3,6,9,12]
y4=[4,8,12,16]

plt.subplot(2,2,1)
plt.plot(x,y1)
plt.title("x=y")

plt.subplot(2,2,2)
plt.plot(x,y2)
plt.title("y=2x")

plt.subplot(2,2,3)
plt.plot(x,y3)
plt.title("y=3x")

plt.subplot(2,2,4)
plt.plot(x,y4)
plt.title("y=4x")

plt.suptitle("sample graph")
plt.tight_layout()
plt.show()
'''


'''
# 하나씩 여러개 그리기. 방법2

x = [1,2,3,4]
y1=[1,2,3,4]
y2=[2,4,6,8]
y3=[3,6,9,12]
y4=[4,8,12,16]
fig, axis = plt.subplots(2,2) #axis로 접근가능?

axis[0,0].plot(x,y1)
axis[0,0].set_title("y=x")

axis[0,1].plot(x,y2)
axis[0,1].set_title("y=2x")

axis[1,0].plot(x,y3)
axis[1,0].set_title("y=3x")


axis[1,1].plot(x,y4)
axis[1,1].set_title("y=4x") 


plt.suptitle("sample graph") 
plt.tight_layout()
plt.show()
'''
# 설정할 때 set이 붙어야됨. 그리드랑 legend(범례)는 set 안들어감

'''
#----------------------------------------------------------------
# 막대 그래프
# 수직
categories = ["A", "B", "C"]
values = [10, 15, 7]

# plt.bar(categories, values, width=0.5, color=["r","g","b"], alpha=0.5, edgecolor="black", linewidth=5, align="center") # legend, ylabel 등등은 모든 그래프들이 동일하게 쓸수있어

bars = plt.bar(categories, values, color="orange", label="Bar Graph")
plt.xticks(categories, ["2023", "2024", "2025"]) # 바꿔놓을 수 있음 #rotation: 글자 각도 바뀜

# 바 그래프별 텍스트 넣기
for bar in bars:
    plt.text( bar.get_x() + bar.get_width()/2, # x좌표(막대의 중심)
              bar.get_height() + 0.5,            # y좌표
              #str(bar.get_height()), # 높이 값(y좌표) 을 넣음
              "Siuu",
              ha="center", # height array
              va="top",
              color="black",
    )

plt.title("Bar graph")
plt.show()
'''

# 수평
categories = ["A", "B", "C"]
values = [10, 15, 7]

bars = plt.barh(categories, values, color=["r", "g", "b"]) # barh: 수평막대

for bar in bars:
    plt.text(bar.get_width() + 0.5, # x좌표
             bar.get_y() + bar.get_height()/2, #y 좌표의 중심
             str(bar.get_width()),
             ha = "right",
             va="center",
             color="black",

             )
plt.legend(bars, ["2023", "2024", "2025"], title = "year", ncol=3)

# 기준선
plt.axvline(x=values[0], linestyle="--") # 10이 기준선
# plt.axhline 수직 그래프에서 수평 기준선

plt.title("Bar graph", pad=10)
plt.xlabel("category")
plt.ylabel("year")

# plt.show()
 
# 저장
plt.savefig("bar.jpg", format="jpg")

