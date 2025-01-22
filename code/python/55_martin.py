# 실습. 공공데이터 활용
import pandas as pd

file_name = "서울시 공원 내 운동기구 설치 현황_201231.csv"
df = pd.read_csv(file_name, encoding="cp949")

print(df.head())
print(df.info())
df.columns = df.columns.str.strip()  # df.columns 열이름 나타내는 index 객체
# print(df.columns)
df["구분"] = df["구분"].str.strip()
df["운동기구 기종명"] = df["운동기구 기종명"].str.strip()

# part_counts = df.groupby("구분")["운동기구 수량"].sum()
# print(part_counts)
# with open("park_counts.txt", "w", encoding="utf-8") as file:
#     file.write("공원별 총 운동기구 설치수\n")
#     file.write(part_counts.to_string())

# equipment_counts = df["운동기구 기종명"].value_counts() ###################################################복습할것
# # print(equipment_counts)
# with open("equipment_counts.txt", "w", encoding="utf-8") as file:
#     file.write("운동기구 종류별 설치 개수\n")
#     file.write(equipment_counts.to_string())

# manage_counts = df.groupby("관리기관")["운동기구 수량"].sum()
# print(manage_counts)
# with open("manage_counts.txt", "w", encoding="utf-8") as file:
#     file.write("관리기관별 운동기구 설치 수\n")
#     file.write(manage_counts.to_string())

# filter_park = df[df["구분"] == "남산공원(회현)"]
# print(filter_park)
# with open("filter_park.txt", "w", encoding="utf-8") as file:
#     file.write("남산공원(회현) 데이터\n")
#     file.write(filter_park.to_string())

# filter_equipment = df[df["운동기구 기종명"] == "스텝사이클"]
# print(filter_equipment)
# with open("filter_equipment.txt", "w", encoding="utf-8") as file:
#     file.write("스텝사이클 데이터\n")
#     file.write(filter_equipment.to_string())


# sort_df = df.sort_values(by="운동기구 수량", ascending=False)
# with open("sort_df.txt", "w", encoding="utf-8") as file:
#     file.write("운동기구 수량 내림차순 정렬\n")
#     file.write(sort_df.to_string())






