# 실습. 야구 데이터

import requests
import numpy as np
from bs4 import BeautifulSoup

url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")


table = soup.select_one("table.tData")
trs = table.select("tr")[1:] # tr에 있는 것만 가져옴
# print(trs)

lists = []
for tr in trs:
    td = tr.select("td")
    td = [i.text.strip() for i in td] # td랑 공백 지우기
    lists.append([td[0], td[1], td[3], td[4], td[5], td[6]])
    # print(td)
print(lists)
array = np.array(lists)

file_name = "kbo_2024_ranking.txt"
header = "순위\t팀\t승\t패\t무\t승률"

with open(file_name, "w", encoding="utf-8") as file:
    file.write(header + "\n")
    for data in array:
        file.write("\t".join(data) + "\n")

# join() 메서드: 문자열 리스트를 하나의 문자열로 결합할 때 사용
# word = ["홍길동", "성춘향", "이몽룡"]
# print("||".join(word))

with open(file_name, "r", encoding="utf-8") as file:
    print(file.read())
