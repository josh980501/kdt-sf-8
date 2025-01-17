from bs4 import BeautifulSoup
import requests # 사이트 주소를 가져오기 위함

# html_str = """
# <html>
#     <body>
#         <div id="content">
#             <ul class="industry">
#                 <li>인공지능</li>
#                 <li>빅데이터</li>
#                 <li>스마트팩토리</li>
#             </ul>
#             <ul class="language">
#                 <li>Python</li>
#                 <li>C++</li>
#                 <li>Javascript</li>
#             </ul>
#         </div>
#     </body>

# </html>
# """

# soup = BeautifulSoup(html_str, "html.parser") # 파싱을 함 => 태그에 접근 가능
# print(soup)
# lxml => 속도가 빠름. pip install lxml 설치 필요
# html5lib => 속도 느림. pip install html5lib. html5의 규격을 엄격히 지킴

# first_ul = soup.find('ul')
# print(first_ul)
# print(first_ul.text) # => 텍스트만 나옴. 태그 다 사라짐

# all_ul = soup.find_all('ul') # 리스트 형태로 반환. 컴마(,)가 있음
# print(all_ul[1])
# print(all_ul[1].text)

# class_ul = soup.find('ul', attrs={'class': 'language'})
# print(class_ul)
# print(class_ul.text)

# class industry를 가져오는 selector
# 1. ul.industry
# 2. #content > .industry
# 3. #content .industry
# 4. #content:first-child

# first_ul = soup.select_one("ul.industry")
# print(first_ul.text)

# all_ul = soup.select("#content > ul") # 여기서는 "#content  ul" 해도됨
# print(all_ul)

# 서울시청 웹크롤링
# html_url = "https://www.seoul.go.kr/main/index.jsp"
# res = requests.get(html_url)
# # print(res.text)

# soup = BeautifulSoup(res.text, "html.parser")
# # print(soup)

# all_nav = soup.select("nav > ul > li > a") # nav a라고 해도됨. 이게 젤 어렵
# # print(all_nav)
# for i in all_nav:
#     print(i.text)

# # 국립중앙박물관 관람 정보
# html_url = "https://www.museum.go.kr/site/main/content/tour_guidance"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")

# all_div = soup.select("div.page-content-type1 > ul.display-content-area > li > ul.display-content:first-child")
# for i in all_div:
#     print(i.text)

#마틴 리더님 풀이.
html_url = "https://www.museum.go.kr/site/main/home"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

# # 전체적으로 가져오는 방법
# infos = soup.select("ul.main-info-area > li")
# # print(infos)
# for i in infos:
#     print(i.text.strip())

# 관람시간
times = soup.select(".info-time > ul > li")
print(times)
# for i in times:
#     print("관람시간 : ", i.text.strip())

# # 관람료
# pay = soup.select(".info-admission > ul > li > strong")
# print(pay[0])



# # kbs 뉴스 크롤링
# html_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8153501"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")
# # print(soup)
# title = soup.select_one(".headline-title")
# print("제목 : ", title.text.strip())

# # 내용
# content = soup.select_one("#cont_newstext")
# print("내용 : ", content.text.strip())

# with open("news.txt", "w", encoding="utf-8") as file:
#     file.write(title.text.strip() + "\n")
#     file.write(content.text.strip())


# # 명언 크롤링
# html_url = "https://quotes.toscrape.com/page/2/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")
# quote = soup.select(".quote > span.text") # 명언 내용
# # print(quote) # 리스트 내용

# # for i in quote:
# #     print(i.text.strip())
# text = [i.text.strip() for i in quote]
# # print(text)

# speaker = soup.select(".quote .author") # 후손일 땐 부등호 > 안씀. 후손(자손의 자손)
# print(speaker)
# author = [i.text.strip() for i in speaker] # 리스트 길이는 위와 동일
# # print(len(text))
# # print(len(author))
# # print(len(speaker))
# zipped = list(zip(text, author))
# print(zipped)
# for text, speak in zipped:
#     print(f"명언자: {speak} \n내용: {text}")