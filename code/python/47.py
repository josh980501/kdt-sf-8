# requests

import requests
import json

url = "https://api.sampleapis.com/avatar/info" # 리스트 안에 json 값이 담겨짐
res = requests.get(url)

# print(res.json())

# print(res.status_code)
if res.status_code == 200:
    data = res.json() # json()값으로 가져오기
    print(data[0]["synopsis"]) # 0번 데이터에 있는 시놉시스 갖고옴
    # print(data[0].synopsis) # synopsis 값 모름. 그럴땐 위에처럼
    print(res.text) # 응답의 본문내용 전부 가져오기(text로 가져옴)
    print(res.url) # 요청 주소 가져옴


