import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

'''
# 한글 설정
path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path)
# plt.rc('font', family=font)

file_name = "연령별인구현황_월간.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")

# print(data.head())
# print(data.info())
region_name = input("검색하고 싶은 지역명을 입력하세요: ")

# 우리가 원하는 나이 컬럼 리스트
age_columns = [col for col in data.columns if "세" in col] # 세가 붙어있는 것들만(컬럼)
# print(age_columns)

# 숫자로 변환
for col in age_columns:
    data[col] = data[col].str.replace(",", "").astype(int) # 컴마 없애고 int 형으로 바꿈

# 필터링
# contains() : 문자열 데이터 필터링, 특정 패턴을 찾을 때
# 옵션값
# na: 결측값을 포함할지 결정, 기본값 True
# case : 영문의 대소문자를 구분, 기본값 True
region_data = data[ data["행정구역"].str.contains(region_name, na=False)] # 결측값 포함 안한다는 뜻

if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")
    exit()

# 데이터 추출
# 2024년12월_계_0~9세 
age_groups = [col.split("_계_")[1] for col in age_columns] # ["2024년12월", "0~9세"] 이렇게 쪼개짐

# 결과값
result = region_data[age_columns].iloc[0].values
print(result)

# 그래프 그리기
plt.figure(figsize=(10,7))
plt.plot(age_groups, result, marker="o", label=region_name)
plt.title(f"{region_name}의 연령별 인구수", fontsize=16, pad=10)
plt.xlabel("나이")
plt.ylabel("인구수")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.legend()
plt.show()
'''

'''
# 행정안전부 남녀 연령별 인구

file_name = "남녀_연령별인구현황_월간.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")
# print(data.head())
# print(data.info())

region_name = input("어느 지역의 인구수가 궁금하신가요?: ")
age_columns_male = [col for col in data.columns if "세" in col and "남" in col]
age_columns_female = [col for col in data.columns if "세" in col and "여" in col]
# print(age_columns_male)

# 숫자로 변환
for col in age_columns_male:
    data[col] = data[col].astype(str)
    data[col] = data[col].str.replace(",", "").astype(int) # 컴마 없애고 int 형으로 바꿈

for col in age_columns_female:
    data[col] = data[col].astype(str)
    data[col] = data[col].str.replace(",", "").astype(int)

region_data = data[data["행정구역"].str.contains(region_name, na=False)]


age_groups = [col.split("_남_")[1] for col in age_columns_male]
# print(region_data[age_columns_male])

# 결과
result_male = region_data[age_columns_male].iloc[0].values
# print(result_male)
result_female = region_data[age_columns_female].iloc[0].values

# 그래프 그리기
plt.figure(figsize=(10,6))

plt.plot(age_groups, result_male, marker="o", label="male")
plt.plot(age_groups, result_female, marker="o", label="female")
plt.title(f"Population of {region_name} by Age & Gender", fontsize=16, pad=10)
plt.xlabel("Age")
plt.ylabel("Population")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.legend(loc="upper right")
plt.show()
'''

# Martin
# 행정안전부 남녀 연령별 인구

file_name = "남녀_연령별인구현황_월간.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")
# print(data.head())
# print(data.info())

region_name = input("어느 지역의 인구수가 궁금하신가요?: ")
# 지역 검색
region_data = data[data["행정구역"].str.contains(region_name, na=False)]
if region_data.empty:
    print(f"{region_name} 지역은 없어연")
    exit()

age_columns_male = [col for col in data.columns if "세" in col and "남" in col]
age_columns_female = [col for col in data.columns if "세" in col and "여" in col]
# print(age_columns_male)

# 숫자로 변환

'''이렇게 써도 무관
for col in age_columns_male:

    region_data[col] = region_data[col].astype(str).str.replace(",", "").astype(int) # 컴마 없애고 int 형으로 바꿈
for col in age_columns_female:
    region_data[col] = region_data[col].str.replace(",", "").astype(int) # 컴마 없애고 int 형으로 바꿈
'''
male_result = region_data[age_columns_male].iloc[0].astype(str).str.replace(",", "").astype(int) # 마포구 첫번째행(엑셀 파일 열어보면 가장 첫번째 행에 마포구 총계 나옴)
female_result = region_data[age_columns_female].iloc[0].apply(lambda x: int(str(x).replace(",", "")))
#  판다스는 반복문이 아니어도 알아서 처리해줌. 판다스의 특징. 이게 첫번째 방법보다 나아
#iloc : Series에 벡터화 연산을 적용하여 효율적이고 간결한 코드 작성이 가능
# apply(): 사용자 함수 정의. 안에 람다식 넣음. 위 아래 동일한 코드

age_groups = [col.split("_남_")[1] for col in age_columns_male]
# print(region_data[age_columns_male])

# 그래프 그리기
plt.figure(figsize=(10,6))
plt.plot(age_groups, male_result, marker="o", label="남성", color= "blue")
plt.plot(age_groups, female_result, marker="o", label="여성", color= "red")
plt.title(f"{region_name}의 연령별 인구수", fontsize=16, pad=10)
plt.xlabel("Age")
plt.ylabel("Population")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.legend(loc="upper right")
plt.show()
