# 마틴님 풀이
# 뉴스 스크랩

from bs4 import BeautifulSoup
import requests

# html_url = "https://www.yna.co.kr/view/AKR20250117007100007?section=sports/index"
# res = requests.get(html_url)

# soup = BeautifulSoup(res.text, "html.parser")
# title = soup.select_one("header > h1.tit")
# print("제목: ", title.text.strip())
# time = soup.select_one("#newsUpdateTime01")
# date = time.select_one("*:not(span)")
# print(time.text.strip().replace("송고시간", ""))
# content = soup.select(".article.story-news p")
# # print(content)
# for i in content:
#     print(i.text.strip())

# # 실습 3.
# html_url = "https://finance.naver.com/marketindex/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")
# usd = soup.select_one("#exchangeList .usd .value")
# print("USD: ", usd.text.strip())
# jpy = soup.select_one("#exchangeList .jpy .value")
# print("JPY(100엔): ", jpy.text.strip())
# eur = soup.select_one("#exchangeList .eur .value")
# print("EUR: ", eur.text.strip())
# cny = soup.select_one("#exchangeList .cny .value")
# print("CNY: ", cny.text.strip())

# 실습 4. 주식정보
def stock(code):
    html_url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = requests.get(html_url)
    soup = BeautifulSoup(res.text, "html.parser")

    company = soup.select_one(".wrap_company > h2 > a")
    print(f"회사명 : {company.text.strip()}")

    price = soup.select_one(".today > .no_today > .no_up > .blind")
    print(f"종가 : {price.text}")

    prev = soup.select_one(".today > .no_exday > .no_up > .blind")
    print(f"전일대비 : {prev.text.strip()}원")

    per = soup.select(".today > .no_exday > .no_up")
    result = per[1].find("span", attrs={"class":"blind"})
    print(result.text)

stock("000680")
stock("024830")