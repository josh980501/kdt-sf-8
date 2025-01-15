# 파일 입출력
# 파일 쓰기

# with open("test.txt", "w", encoding = "utf-8") as file:
#     file.write("안녕하세요\n")
#     file.write("파이썬파일쓰기 연습\n") # 붙여서나옴


# 내용 추가
# with open("test.txt", "a", encoding = "utf-8") as file:
#     file.write("내용추가\n")
#     file.write("1111") # string만 써야됨

# writelines()
# lines = ["첫번째 내용\n", "두번째내용\n", "세번째내용\n"]

# with open("test2.txt", "w", encoding="utf-8") as file:
#     file.writelines(lines)

# 사용자로부터 입력받은 내용을 파일로 만들기
# with open("user.txt", "w", encoding="utf-8") as file:
#     while True:
#         line = input("파일에 넣을 문자열입력(종료하려면 '종료' 입력): ")
#         if line == "종료":
#             print("\n입력을 종료합니다")
#             break

#         file.write(line + "\n")

# 파일 읽기
# with open("user.txt", "r", encoding = "utf-8") as file:
#     print(file.read()) # 파일 전체 읽기

# with open("user.txt", "r", encoding= "utf-8") as file:
#     print(file.readline()) # 파일 한줄씩
#     print(file.readline()) # 파일 한줄씩
#     print(file.readline()) # 파일 한줄씩

# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.readlines()) # 파일을 리스트 형태로 반환

# 한줄씩 가져와서 반복문으로 읽음
# with open("user.txt", "r", encoding="utf-8") as file:
#     line = file.readline()
#     while line: # line이 끝날때까지 반복
#         print(line.strip()) # 이건 엔터 없애려고..#.strip()은 양쪽 공백을 없앰 .rstrip()은 오른쪽 공백 없앰 .lstrip()은 좌측 공백 없앰
#         line = file.readline() 

# enumerate() # 리스트를 튜플 형태로 반환(반환값이 두개)
# with open("user.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     # (0, "동해물과\n"), (1, "백두산이\n") <= ["동해물과\n", "백두산이\n"]
#     for idx, value in enumerate(lines): # lines의 요소
#         print(f"{idx} 인덱스의 값은 {value.strip()}입니다.")



#============================바이너리 파일==================================
# with open("owl.png", "rb") as file:
#     # data = file.read()
#     # print(f"{len(data)} 바이트")
#     header = file.read(10) # 파일 확장자를 찾는 방법
#     print(f"{header}") #b'\x89PNG\r\n\x1a\n\x00\x00' <= 이게 바이너리 파일.  x89PNG 은 png 파일 앞에 다 붙어있음

# def files(file_path):
#     with open(file_path, "rb") as file: # 영문& 문자열이라서 인코딩 안해줘도됨
#         header = file.read(4) # 4바이트가 확장자의 매직넘버
#         print(header)
#         if header == b"\x89PNG": #png는 첫 4바이트가 89 50 4e 47 # 여기서 b: 바이너리 파일이라는 의미
#             return "png"
#         elif header == b"\xff\xd8\xff\xe0": # jpg는 2바이트이기 떄문에 뒤에 2바이트를 삭제. xff\xe0 는 필요없음. 원래는 header[:2] 만큼 해야됨
#             return "jpg"
#         else:
#             return "unknown"

# print(files("Cat03.jpg"))


# 바이너리 파일 쓰기 (읽고 복사)
with open("owl.png", "rb") as file:
    data = file.read()

with open("owl_copy.png", "wb") as file:
    file.write(data)

