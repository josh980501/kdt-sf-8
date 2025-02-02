import folium
import pandas as pd
#geojson
from geojson import Feature, FeatureCollection, Point, Polygon

# # 지도 열기
# my_map = folium.Map(
#     location=[37.525094, 126.980483], zoom_start=12, tiles="CartoDB Positron"
# )

# -----------------------------------기본


# 지도 스타일 추가
# my_map = folium.Map(location=[37.525094, 126.980483], zoom_start=12, tiles="CartoDB Positron" #회색 배경
#                     )
# my_map.save("my_map.html")

# 지도에 마커 추가
# my_map = folium.Map(location=[37.525094, 126.980483], zoom_start=12, tiles="CartoDB Positron")
# folium.Marker([37.537783, 126.977783], popup="전쟁기념관").add_to(my_map) # 기본 마커
# folium.Marker([37.540506, 126.998898], popup="리움미술관", icon=folium.Icon(color="red", icon="arrow-right")).add_to(my_map) # 기본 마커


# my_map.save("my_map.html")

# 지도에 여러개 마커 딕셔너리 형태로 추가

# map_info = [
#     {"location": [37.537783, 126.977783], "popup": "전쟁기념관"},
#     {"location": [37.538791, 126.950443], "popup": "강의실"}
# ]

# for info in map_info:
#     folium.Marker(location=info["location"], popup=info["popup"], icon=folium.Icon(color="green", icon="star")).add_to(my_map)

# my_map.save("my_map.html")

# 지도에 영역 표시

# 원형 영역

# folium.Circle(  # Circle, Rectangle, Polygon
#     location=[37.579835, 126.977113],
#     radius=1000, # 반지름(미터 단위)
#     color="blue",
#     popup="경복궁 일대",
#     fill=True,
#     fill_color= "yellow"
# ).add_to(my_map)

# my_map.save("my_map.html")
'''
data = {
    "location": [[37.530246, 126.964894], [37.518119, 126.894548], [37.525479, 126.896529], [37.534810, 126.902596], [37.549607, 126.913831]],
     "popup": ["용산역", "문래역", "영등포구청역","당산역", "합정역"]
}
df = pd.DataFrame(data)

new_file1 = "서울 지하철역 5개.csv"

with open(new_file1, "w", encoding="utf-8") as file:
    file.write(df.to_csv())

# folium.Marker(location=df["location"], popup=df["popup"], icon=folium.Icon(color="green", icon="star")).add_to(my_map)
for idx, row in df.iterrows():
    folium.Marker(
        location=row["location"],
        popup=row["popup"],
        icon=folium.Icon(color="green", icon="star"),
    ).add_to(my_map) # add_to 매우 중요

my_map.save("my_map.html")
'''

# iterrow(): 데이터 프레임에서 행단위로 반복하면서 인덱스와 행의 쌍을 반환하는 함수

#--------------------------------------------------------------
# GeoJSON
'''
# 데이터 생성
feature1 = Feature(geometry=Point((126.996281, 37.554527)), properties={"name":"서울", "population":"970만"})
feature1_2 = {"type": "Feature",
 "geometry": {"coordinates": [126.996281, 37.554527], "type": "Point"
              }, 
 "properties": {"name": "서울", "population": "970만"}, 
 }
feature2 = Feature(geometry=Point((129.158088, 35.178437)), properties={"name":"부산", "population":"340만"})
feature3 = Feature(geometry=Point((127.515632, 36.341815)), properties={"name":"대전", "population":"150만"})
feature4 = Feature(geometry=Point((128.663703, 35.853578)), properties={"name":"대구", "population":"240만"})
print(feature1)
print(feature1_2)


# 데이터 하나로 묶기
geojson_data = FeatureCollection([feature1, feature2, feature3, feature4])
# print(geojson_data)


#  지도 생성
my_map = folium.Map(location=[36.917494, 127.894916], zoom_start=7)

# 데이터를 지도에 추가
folium.GeoJson(
    geojson_data,
    name="GeoJson Data", 

    tooltip=folium.GeoJsonTooltip( # 툴팁이 뭐지?
        fields=["name", "population"], # 표시할 속성
        aliases=["도시이름: ", "인구: "] # 속성의 별칭
    ),
).add_to(my_map)
my_map.save("my_map.html")
'''


# GeoJSON Polygon
'''
polygon_data = [
          [
            [
              126.76663551646118,
              37.88489486477819
            ],
            [
              126.60053032088024,
              37.49866208866018
            ],
            [
              126.72673909141668,
              37.12888978360337
            ],
            [
              126.93267311027125,
              36.754823422414546
            ],
            [
              127.6895501081649,
              37.10255438303601
            ],
            [
              127.8052991872811,
              37.62484275882876
            ],
            [
              127.20487081555746,
              38.0599799208901
            ],
            [
              126.76663551646118,
              37.88489486477819
            ]
          ]
        ]
geojson_data = Feature(geometry=Polygon(polygon_data), properties={"name": "수도권"})
final_data = FeatureCollection([geojson_data])
#  지도 생성
my_map = folium.Map(location=[36.917494, 127.894916], zoom_start=7)

folium.GeoJson(
    final_data,
    name="GeoJson Data",

    tooltip=folium.GeoJsonTooltip( # 툴팁이 뭐지?
        fields=["name"], # 표시할 속성
        aliases=["영역 이름: "] # 속성의 별칭
    ),
).add_to(my_map)
my_map.save("my_map.html")
'''


'''
# 실무 실습

my_map = folium.Map(location=[37.549553, 127.066119],zoom_start=7, titles="CartoDB Positron")

# geojson
geojson_data = "HangJeongDong_ver20241001.geojson"

folium.GeoJson(
    geojson_data,
    name="대한민국 경계",
    style_function=lambda _: {
        "fillColor": "blue",
        "color":"black",
        "weight": 1,
        "fillOpacity": 0.1
    }
).add_to(my_map)
my_map.save("my_map.html")
'''


