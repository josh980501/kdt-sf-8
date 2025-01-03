#한줄 주석
# python 파일 실행 단축키: ctrl +F5
'''
여기는
여러개
주석
'''
"""
쌍따옴표표 세개도
여러줄
주석
"""
# 한줄 주석(ctrl + /)하하하하


print("Hello World")
print("Hello", "World", "Kyungrok", sep="") #seperate, 구분자자
print("010", "1234","4321",sep="-")
print("Hello", "Python", 1, 2, sep="_") #자료형 달라도 됨
print() #print 함수 안에 아무것도 안 넣으면 줄바꿈
print("1111")
print("안녕하세요, ", end="") #end 옵션: 문장끝에 넣고 싶은 것
print("코딩온입니다.")
print("안녕하세요", end=", ") #결과 동일일
print("코딩온입니다.")
ive = 'I AM'
print(ive)
ive = "장원영"
print(ive)
print(f"제가 좋아하는 가수는 {ive}입니다.") #f 문자열 포매팅
print("제가 좋아하는 가수는 ", ive, "입니다.", sep="") #위와 결과 동일
