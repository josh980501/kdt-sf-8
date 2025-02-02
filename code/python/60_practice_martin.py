# lambda 식을 쓰기 위해서는 apply() 안에다가 씀
# axis = 1 : 열단위로 작업하라는 뜻

# iterrow()에서 index, value 쌍 반환...값 안쓸땐 '_' 쓰면됨...
# 웬만하면 방법1 쓸것. 속도 더 빠름..lambda 웬만하면 써라!

# 실습
# 서울 지하철 5개

import folium
import pandas as pd
from geojson import Feature, FeatureCollection, Point, Polygon

'''
data = {
    "Station": ["서울역", "공덕역", "응암역", "홍대입구역", "디지털미디어시티역"],
    "Latitude": [37.555044, 37.542723, 37.598571, 37.557412, 37.576269],
    "Longitude": [126.970741, 126.951833, 126.915525, 126.924493, 126.901534],
}
subway = pd.DataFrame(data)
# csv파일저장
subway.to_csv("subway.csv", encoding="EUC-KR", index=False)
# folium 지도제작
my_map = folium.Map(location=[37.580307, 126.928719], zoom_start=12)
# 방법1
# subway.apply(
#     lambda x: folium.Marker(
#         location=[x["Latitude"], x["Longitude"]],
#         popup=x["Station"],
#         icon=folium.Icon(color="blue", icon="home"),
#     ).add_to(my_map),
#     axis=1, # 열단위로 작업. axis=0 행단위로 작업
# )
# 방법2
# iterrow() : 데이터프레임에서 행단위로 반복하면서 인덱스와 행의 쌍을 반환하는 함수
for _, x in subway.iterrows():
    folium.Marker(
        location=[x["Latitude"], x["Longitude"]],
        popup=x["Station"],
        icon=folium.Icon(color="blue", icon="star"),
    ).add_to(my_map)

my_map.save("my_map.html")
'''
#-------------------------------------- 폴리곤

polygon = Feature(geometry=Polygon([[
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
]]), properties={"name": "수도권"}
                  )

geojson_data = FeatureCollection([polygon])

my_map = folium.Map(location=[37.475479, 127.269366], zoom_start=7)

folium.GeoJson(
    geojson_data,
    name="GeoJson Data",

    tooltip=folium.GeoJsonTooltip( 
        fields=["name"], # 표시할 속성
        aliases=["영역 이름: "]), # 속성의 별칭
        style_function=lambda _: {
            "fillColor":"yellow",
            "color": "black",
            "weight": 2,
            "fillOpacity": 0.5
        }
    
).add_to(my_map)
my_map.save("my_map.html")

