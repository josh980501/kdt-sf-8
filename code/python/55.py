# 실습. 공공데이터 활용
import pandas as pd

# 1. 공원별 총 운동기구 설치 수
file_name = "서울시 공원 내 운동기구 설치 현황_201231.csv"
df = pd.read_csv(file_name, encoding="cp949") # 데이터프레임 형태로 불러옴
df.columns= df.columns.str.strip() # df.columns :열 이름 나타내는 index 객체. 열 이름 앞뒤 공백 제거
df = df.map(lambda x: x.strip() if isinstance(x, str) else x) # 모든 셀의 앞뒤 공백 제거
df['구분'] = df["구분"].str.strip() # 이렇게도 공백 제거 가능

result = df.groupby("구분")["운동기구 수량"].sum()
new_file1 = "공원별 총 운동기구 설치 수.csv"
with open(new_file1, "w", encoding="utf-8") as file:
    file.write(result.to_csv())
# write에는 str만 넣을 수 이씅ㅁ
# print(result.head())

# print(df.columns)


# print(type(df))
# df = df.map(lambda x: x.strip() if isinstance(x, str) else x) # 모든 셀의 앞뒤 공백 제거

# print(df.head())
# print(df.info())

# 2. 운동 기구 종류 별 설치 개수
file_name = "서울시 공원 내 운동기구 설치 현황_201231.csv"
df = pd.read_csv(file_name, encoding="cp949") # 데이터프레임 형태로 불러옴
df.columns= df.columns.str.strip() # df.columns :열 이름 나타내는 index 객체. 열 이름 앞뒤 공백 제거
df = df.map(lambda x: x.strip() if isinstance(x, str) else x) # 모든 셀의 앞뒤 공백 제거

result = df.groupby("운동기구 기종명")["운동기구 수량"].sum()
new_file2 = "운동기구 종류별 설치 개수.csv"
with open(new_file2, "w", encoding="utf-8") as file:
    file.write(result.to_csv())
# print(df.columns)

# 3. 관리기관별 총 운동기구 설치 수 
file_name = "서울시 공원 내 운동기구 설치 현황_201231.csv"
df = pd.read_csv(file_name, encoding="cp949") # 데이터프레임 형태로 불러옴
df.columns= df.columns.str.strip() # df.columns :열 이름 나타내는 index 객체. 열 이름 앞뒤 공백 제거
df = df.map(lambda x: x.strip() if isinstance(x, str) else x) # 모든 셀의 앞뒤 공백 제거

result = df.groupby("관리기관")["운동기구 수량"].sum()
new_file3 = "관리기관별 총 운동기구 설치 수.csv"
with open(new_file3, "w", encoding="utf-8") as file:
    file.write(result.to_csv(header=True))
# print(df.columns)

# 4. 특정 공원 데이터 필터링
file_name = "서울시 공원 내 운동기구 설치 현황_201231.csv"
df = pd.read_csv(file_name, encoding="cp949") # 데이터프레임 형태로 불러옴
df.columns= df.columns.str.strip() # df.columns :열 이름 나타내는 index 객체. 열 이름 앞뒤 공백 제거
df = df.map(lambda x: x.strip() if isinstance(x, str) else x) # 모든 셀의 앞뒤 공백 제거


filtered_df = df[df["구분"] == "남산공원(회현)"]
print(filtered_df.head())
new_file4 = "남산공원(회현) 데이터.csv"
with open(new_file4, "w", encoding="utf-8") as file:
    file.write(filtered_df.to_csv(header=True))

# print(df.columns)
# result = df.groupby().filter(lambda x: x[])
# filtered_df = df.groupby("구분").filter(lambda x: x['구분'] == "남산공원(회현)")############################다시복습!!!!

# 실습 5. 특정 운동기구 종류 데이터 필터링(스텝사이클)
file_name = "서울시 공원 내 운동기구 설치 현황_201231.csv"
df = pd.read_csv(file_name, encoding="cp949") # 데이터프레임 형태로 불러옴
df.columns= df.columns.str.strip() # df.columns :열 이름 나타내는 index 객체. 열 이름 앞뒤 공백 제거
df = df.map(lambda x: x.strip() if isinstance(x, str) else x) # 모든 셀의 앞뒤 공백 제거


filtered_df = df[df["운동기구 기종명"] == "스텝사이클"]
print(filtered_df.head())
new_file5 = "스텝사이클 있는 곳.csv"
with open(new_file5, "w", encoding="utf-8") as file:
    file.write(filtered_df.to_csv(header=True))

# print(df.columns)
# result = df.groupby().filter(lambda x: x[])

# 실습6. 운동기구 수량 기준 내림차순 정렬

file_name = "서울시 공원 내 운동기구 설치 현황_201231.csv"
df = pd.read_csv(file_name, encoding="cp949") # 데이터프레임 형태로 불러옴
df.columns= df.columns.str.strip() # df.columns :열 이름 나타내는 index 객체. 열 이름 앞뒤 공백 제거
df = df.map(lambda x: x.strip() if isinstance(x, str) else x) # 모든 셀의 앞뒤 공백 제거

df.sort_values(by="운동기구 수량", inplace=True, ascending=False)
print(df.head())
new_file6 = "운동기구 수량 기준 내림차순 정렬.csv"
with open(new_file6, "w", encoding="utf-8") as file:
    file.write(df.to_csv(header=True))

# print(df.columns)
# result = df.groupby().filter(lambda x: x[])
# filtered_df = df[df["운동기구 기종명"] == "스텝사이클"]