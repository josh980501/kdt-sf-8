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



print(type(77)) #int: 숫자형 > 정수타입/integer
print(type(7.2)) #float: 숫자형 > 실수타입
print(type('i\'ve'))
print(type("i\"ve"))
print('i\'ve') #i've
print("i\"ve") #i"ve

print("i've") #i"ve


a= 77
print(type(a))
a = 7.2
print(type(a))
a = 'ive'
print(type(a)) #str: 문자열


print("111\n111") # \n: 줄바꿈
print("111\t111") #\t: 탭 (8칸 띄움)

print("|\_/|\n|q p|\t/}\n( 0 )\"\"\"\\\n|\"^\"'\t |\n||_/=\\\\__|")

num = 10 #10진수
b_num = 0b1010 #2진수
h_num = 0xA #16진수

print(num)
print(b_num)
print(h_num)

print(bin(10)) #10진수 to 2진수
print(hex(10)) #10진수 to 16진수

print(type(bin(10))) #문자열
print(type(hex(10))) #문자열

print(ord("0")) #ord(): 주어진 문자를 해당하는 유니코드 정수값으로 변환
print(ord("A")) 
print(chr(48))  #chr() : 주어진 유니코드 정수값을 문자로 변환환
print(chr(65))

