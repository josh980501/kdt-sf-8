import pandas as pd


'''
# 리스트 형식으로 생성
data = [10, 20, 30, 40]
# series = pd.Series(data) # 기본 인덱스 . 시리즈는 1차원
series = pd.Series(data, index=["a", "b", "c", "d"]) # 커스텀 인덱스
print(series)
'''



'''
# 딕셔너리 형식으로 생성
data = {
    "a": 10,
    "b": True,
    "c": 3.14,
    "d": "Python"
}
series = pd.Series(data, name="딕셔너리")
print(series) 
# a        10
# b      True
# c      3.14
# d    Python
# dtype: object  => numpy랑 다르게 자료형 다 달라도 됨
print(series.index) 
print(series.values) 
print(series.shape) # 길이가 나옴. # (4,)
'''

'''
data = ('민지', '여', False) # 자료형이 다 다르면 object타입으로 나옴
member = pd.Series(data, index=["이름", "성별", "결혼여부"])
print(member)
print(member["이름"])
print(member[["성별", "결혼여부"]]) # 이차원 리스트 형태로 출력

data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(series[0]) # 나오긴 나오지만 인덱스 바꿨으니까 그 인덱스값 써라라고 나옴!
print(series['a']) # 인덱스를 변경했으면 그 인덱스를 사용 (권장)
print(series[series > 20]) # 인덱스값이랑 같이 나옴
series['c'] = 100
print(series)
print("a" in series) # 인덱스 'a'가 존재하는지 검색
print(series.sum()) # 합계
print(series.mean()) # 평균값
print(series.max()) # 최대값
print(series.astype(float)) # 타입을 변경해버림
'''


# pandas vs numpy
# 인덱스: 커스텀 가능 vs 숫자(0부터 시작)
# 데이터 타입: 혼합 가능 vs 단일 자료형
'''
# 실습1. Series 만들기. MArtin
data = ["4 cups", "1 cup", "2 large", "1 can"]
index = ["밀가루", "우유", "계란", "참치캔"] # 이렇게도 할 수 있다
series = pd.Series(data, index=index, name="Dinner")
print(series)
'''
#----------------------------------------------------------Series
# 데이터 프레임
index = ['2020', '2021', '2022', '2023', '2024', '2025']
younghee = pd.Series([140, 150, 160, 170, 180, 190], index=index)
cheolsu = pd.Series([200, 210, 220, 230, None, 250], index=index)

result = pd.DataFrame({
    "영희": younghee,
    "철수": cheolsu
})

# print(result)
# print(result.head()) #head는 기본적으로 위에서부터 0~5까지. 제대로 들어가있는지 확인만 하기 위해서 씀. head(10)은 10개
# print(result.tail()) # tail은 아래에서부터 기본 5개 가져와줌
# print(result.shape) # (6, 2)=> 6행 2열 얘는 메서드 아님
# print(result.info()) # 요약 정보. Non-Null Count: 결치값.(값이 몇개 있냐). non-null: null이 없다. 만약에 데이터 중에 None 있으면 하나 빠짐. # 맨 밑에 none은 반환값이 없다는 뜻
# result.info() # 이러면 none은 안나옴
# print(result.columns) # 컬럼 출력 시켜줌. 열 이름
# print(result.values) # 행 값. 이차원 행렬로 출력
# print(result.index) # 인덱스값
# print(result.dtypes) # 데이터 타입
# print(result["철수"]) # 컬럼값은 같이 안나옴
# print(result[["철수"]]) # coulumn 값 같이 나옴.영희도 같이 나오려면 어떻게?




'''
data = {
    "Name": ["홍길동", "임꺽정", "성춘향"],
    "Age": [25, 30, 27],
    "City": ["서울", "부산", "인천"]
}
df = pd.DataFrame(data, index=["a", "b", "c"]) # 보통 이렇게 많이 씀
print(df)

# 데이터 값 추출하는 방법################

# loc(index, column): 라벨 기반 접근. 이름 기반

# print(df.loc["b"])
# print(df.loc["b", "Age"])
# print(df.loc["a":"c", "Name":"Age"]) # a~c까지, name부터 age까지
# print(df.loc[df['Age'] >= 30]) 
# print(df.loc[~(df['Age'] >= 30)]) # 위에 거의 부정 (30 미만)
# print(df.loc[:, "Name"]) # name값 전체. :은 전체라는 뜻
# print(df.loc["a", :]) # a값 전체. :은 전체라는 뜻 . 앞에는 인덱스, 뒤에는 컬럼값


# 숫자 기반

# print(df.iloc[1])
# print(df.iloc[1, 1]) # b의 Age 값
# print(df.iloc[0:2, 0:1]) # 끝값이 포함되지 않음
# print(df.iloc[[0, 2], [1, 2]])#####################
# print(df.iloc[df[1] >= 30]) # 앤 오류. 부등호는 안됨
# print(df.iloc[:, 0]) #
# print(df.iloc[0, :]) #

# 데이터를 넣고 추가/수정하는 방법##################

# # 행 추가
# new_data = {'Name': "이몽룡", "Age": 31, "City": "포항"}
# result = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True) # concat은 합칠 때 쓰는 메서드. a, b, c, d로 하려면 인덱스 리셋해야됨
# print(result)

# 인덱스와 같이 행 추가
new_data = pd.DataFrame({'Name': "이몽룡", "Age": 31, "City": "포항"}, index=["d"])
#concat 이용방법
result = pd.concat([df, new_data])
# loc 이용방법
result.loc["e"] = ["전우치", 28, "대전"]
# print(result)


# 열 추가
result["직업"] = ["엔지니어", "개발자", "디자이너", "기획자", "데이터 분석가"]
# print(result)

# 요소값 수정
result.at["b", 'City'] = '천안'
result.loc[result['Name'] == '임꺽정', 'Age'] = 28 # result name의 임꺽정 값을 찾아서 그 age를 31로 바꿈
# print(result)

# 컬럼값 변경
result.rename(columns={"Name": "이름", "Age":"나이", "City": "도시"}, inplace=True) # 딕셔너리 형태
# inplace=True 옵션값: 원본데이터 수정

# 데이터 정렬(# 기본이 오름차순)
result.sort_values(by="나이", inplace=True, ascending=False) # ascending=False: 내림차순

# 컬럼 삭제
result.drop(columns=["도시"], inplace=True) # 리스트 형태
print(result)
'''

'''
# 실습2. 데이터 프레임 만들기
data = {
    "이름": ["홍길동", "임꺽정", "성춘향"],
    "수학": [85, 90, 78],
    "영어": [88, 76, 92],
    "과학": [95, 89, 84]
}
df = pd.DataFrame(data)
new_data = {'이름': "이몽룡", "수학": 88, "영어": 85, "과학": 90}
df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True) # ignore_index=True 은 초기화되는걸 방지
df["Total"] = [268, 255, 254, 263]
# df = df.rename(columns={"수학":"Math"}) # 이러면 inplace=True 안써도됨. 원본 변경
df.rename(columns={"수학":"Math"},inplace=True)
df.loc[df["영어"] == 76, "영어"] = 80
print(df)
df["Total"] = df["Math"] + df["영어"] + df["과학"] ## 중요!! 그냥 더하면 됨.
'''

'''
# -------------------------------------------------------------
# 결측값
data = {
    "Name": ["홍길동", "임꺽정", "성춘향"],
    "Age": [25, None, 20], # Nan이라고 나옴. 숫자 들어갈 곳에 문자 들어갔기 때문
    "City": ["서울", "부산", None]
}

df = pd.DataFrame(data)
# print(df)
# print(df.isnull()) # 결측값 여부
print(df.isnull().sum()) # 결측값 갯수의 합
print(df.info())
df_drop = df.dropna() # 결측값 있는 행을 모두 제거
df_drop_column = df.dropna(axis=1) # 결측값들이 있는 열들을 모두 삭제. axis=1은 열을 의미
df_fill = df.fillna(0) # 결측값들이 있는 항을 모두 0으로 채움
df_fill_prev = df.fillna(method="ffill") # 이전에 있는 값으로 채움
df_fill_next = df.fillna(method="bfill") # 이후에 있는 값으로 채움. 그래서 맨 마지막 항은 안채워짐
print(df_fill_next)
'''



#------------------------------------------------------------
# 주요 메서드

# isin() ####################################
s = pd.Series(["홍길동", "임꺽정", "성춘향", "이몽룡"])
result = s.isin(["홍길동", "이몽룡"])
print(result)

data = {
    'Name': ["홍길동", "임꺽정", "성춘향", "이몽룡"],
    'Age': [25, 30, 20, 31]
}
df = pd.DataFrame(data)
# result = df.isin(["성춘향", "홍길동", 20]) # True/False 찾기
result = df[df["Name"].isin(["성춘향", "홍길동", 31])] # True 값만 필터링
print(result)
'''

s = pd.Series([1, 2, None])
result = s.isin([None, 2])
print(result) # None값은 무시하므로 그냥 False로 뜸

#value_counts()###############################333
s = pd.Series(['사과', '바나나', '사과', '오렌지', '바나나', '사과'])
print(s.value_counts()) # 빈도수

df = pd.DataFrame(
    {
    "과일": ['사과', '바나나', '사과', '오렌지', '바나나', None, '사과'],
    '수량': [1, 2, 3, 4, 5, 6, 7],
    }
)
# print(df["과일"].value_counts(normalize = True)) # 빈도수를 비율로(%)
# print(df["과일"].value_counts(ascending = True)) # 오름차순
# print(df["과일"].value_counts(dropna = False)) # 결측값도 모두 나옴


# agg()####################################################
s = pd.Series([1,2,3,4,5])
result = s.agg(['sum', 'mean', 'max']) # 원하는 통계 지표를 요약해서 나타냄
print(result)

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [11, 12, 13],
})
print(df.agg(['sum', 'mean']))
print(df.agg({"A": 'sum', 'B': 'mean'}))

# 사칙연산, 부등호
s1 = pd.Series([10, 20, 30])
s2 = pd.Series([5, 15, 25])

print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 / s2)
print(s1 > 15) # true/false

#통계연산
print(s1.sum())
print(s1.mean()) #평균
print(s1.max())
print(s1.min())
print(s1.std()) # 표준편차
print(s1.var()) # 분산
print(s1.median()) # 중앙값
# agg로도 나타낼 수 있음

# 통계 지표
print(s1.describe()) 
'''

# 그룹화
# data = {
#     'group': ['A', "A", "B", "B", "C"],
#     'value': [10, 20, 30, 40, 50]
# }
# df = pd.DataFrame(data)
# result = df.groupby('group')["value"].sum()
# result = df.groupby('group')["value"].agg(['sum', 'mean', 'var'])

# print(result)
#        sum  mean   var
# group
# A       30  15.0  50.0
# B       70  35.0  50.0
# C       50  50.0   NaN

'''
data = {
    'group': ['A', "A", "B", "B", "C"],
    'value1': [10, 20, 30, 40, 50],
    'value2': [5, 15, 25, 35, 45],
}
df = pd.DataFrame(data)
# result = df.groupby('group').agg({
#     'value1': "sum",
#     'value2': ["mean", "max"]
# })
# 위의 결과.
#       value1 value2    
#          sum   mean max
# group
# A         30   10.0  15
# B         70   30.0  35
# C         50   45.0  45


result = df.groupby("group").filter(lambda x: x['value2'].mean() <= 10) # 특정 그룹내 value2끼리의 평균이 10이하일 때 그 그룹의 value1, value2 전체
print(result)
'''

