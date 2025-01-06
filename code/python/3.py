# song = input("너의 최애 노래는?")
# print(song)
# print(type(song)) # <class 'str'> => "문자열"

# a= input("") #형변환

#형변환(type casting)
#1. 정수형으로 변환
# print(int("10"), type(int("10")))
# print(int(10.9), type(int(10.9)))

# 2. 실수형으로 변환

#print(float("11.2", ))

#3. 형변환 안되는 예시
#print(int("11.2"))

# math_score = 80
# eng_score = 85
# total_score = math_score + eng_score
# avg_score = total_score / 2

# print("합계: " + str(total_score))
# print("평균: " + str(avg_score))

# #1번
# name= input("이름을 입력하세요. ")
# age = input("나이를 입력하세요. ")
# print(f"안녕하세요! {name}님 ({age}세)")
# print("안녕하세요! " + name + "님 (" + age + "세)")
# print("안녕하세요!", name + "님", "(" + age + "세)")


# #2번
# name= input("이름을 입력하세요. ")
# born = input("태어난 년도를 입력하세요. ")
# year = input("올해 년도를 입력하세요. ")
# age = int(year) - int(born) + 1
# print(f"올해는 {year}년, {name}님의 나이는 {str(age)}세입니다") #print(f"")
# print("올해는 " + year +"년, " + name + "님의 나이는 " + str(age) + "세입니다") #print(+)
# print("올해는", year + "년,", name + "님의 나이는", str(age) + "세입니다") # print (, +)
